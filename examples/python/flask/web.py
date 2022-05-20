import uuid
from datetime import datetime
from typing import Optional

from fief_client import Fief, FiefUserInfo
from fief_client.integrations.flask import (
    FiefAuth,
    FiefAuthForbidden,
    FiefAuthUnauthorized,
    get_cookie,
)
from flask import Flask, g, redirect, request, session, url_for

SESSION_COOKIE_NAME = "user_session"
SECRET_KEY = "SECRET"  # (1)!


fief = Fief(  # (2)!
    "https://example.fief.dev",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)


def get_userinfo_cache(id: uuid.UUID) -> Optional[FiefUserInfo]:  # (3)!
    return session.get(f"userinfo-{str(id)}")


def set_userinfo_cache(id: uuid.UUID, userinfo: FiefUserInfo) -> None:  # (4)!
    session[f"userinfo-{str(id)}"] = userinfo


auth = FiefAuth(
    fief,
    get_cookie(SESSION_COOKIE_NAME),  # (5)
    get_userinfo_cache=get_userinfo_cache,  # (6)!
    set_userinfo_cache=set_userinfo_cache,
)
app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.errorhandler(FiefAuthUnauthorized)  # (7)!
def fief_unauthorized_error(e):
    redirect_uri = url_for("auth_callback", _external=True)  # (8)!
    auth_url = fief.auth_url(redirect_uri, scope=["openid"])  # (9)!
    return redirect(auth_url)  # (10)!


@app.errorhandler(FiefAuthForbidden)
def fief_forbidden_error(e):
    return "", 403


@app.get("/auth-callback")  # (11)!
def auth_callback():
    redirect_uri = url_for("auth_callback", _external=True)
    code = request.args["code"]
    tokens, userinfo = fief.auth_callback(code, redirect_uri)  # (12)!

    response = redirect(url_for("protected"))  # (13)!
    response.set_cookie(  # (14)!
        SESSION_COOKIE_NAME,
        tokens["access_token"],
        expires=int(datetime.now().timestamp() + tokens["expires_in"]),
        httponly=True,  # (15)!
        secure=False,  # ❌ Set this to `True` in production (16)!
    )

    set_userinfo_cache(uuid.UUID(userinfo["sub"]), userinfo)  # (17)!

    return response


@app.get("/protected")
@auth.current_user()  # (18)!
def protected():
    user = g.user  # (19)!
    return f"<h1>You are authenticated. Your user email is {user['email']}</h1>"
