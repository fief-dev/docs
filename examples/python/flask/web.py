from datetime import datetime

from fief_client import Fief
from fief_client.integrations.flask import (
    FiefAuth,
    FiefAuthForbidden,
    FiefAuthUnauthorized,
    get_cookie,
)
from flask import Flask, g, redirect, request, url_for

SESSION_COOKIE_NAME = "user_session"


fief = Fief(  # (1)!
    "https://example.fief.dev",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)

auth = FiefAuth(fief, get_cookie(SESSION_COOKIE_NAME))  # (2)!
app = Flask(__name__)


@app.errorhandler(FiefAuthUnauthorized)  # (3)!
def fief_unauthorized_error(e):
    redirect_uri = url_for("auth_callback", _external=True)  # (4)!
    auth_url = fief.auth_url(redirect_uri, scope=["openid"])  # (5)!
    return redirect(auth_url)  # (6)!


@app.errorhandler(FiefAuthForbidden)
def fief_forbidden_error(e):
    return "", 403


@app.get("/auth-callback")  # (7)!
def auth_callback():
    redirect_uri = url_for("auth_callback", _external=True)
    code = request.args["code"]
    tokens, _ = fief.auth_callback(code, redirect_uri)  # (8)!

    response = redirect(url_for("protected"))  # (9)!
    response.set_cookie(  # (10)!
        SESSION_COOKIE_NAME,
        tokens["access_token"],
        expires=int(datetime.now().timestamp() + tokens["expires_in"]),
        httponly=True,  # (11)!
        secure=False,  # ❌ Set this to `True` in production (12)!
    )

    return response


@app.get("/protected")
@auth.current_user()  # (13)!
def protected():
    user = g.user
    return f"<h1>You are authenticated. Your user ID is {user['id']}</h1>"
