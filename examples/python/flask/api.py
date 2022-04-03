from fief_client import Fief
from fief_client.integrations.flask import (
    FiefAuth,
    FiefAuthForbidden,
    FiefAuthUnauthorized,
    get_authorization_scheme_token,
)
from flask import Flask, g

fief = Fief(  # (1)!
    "https://example.fief.dev",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)

auth = FiefAuth(fief, get_authorization_scheme_token())  # (2)!

app = Flask(__name__)


@app.errorhandler(FiefAuthUnauthorized)  # (3)!
def fief_unauthorized_error(e):
    return "", 401


@app.errorhandler(FiefAuthForbidden)  # (4)!
def fief_forbidden_error(e):
    return "", 403


@app.get("/user")
@auth.current_user()  # (5)!
def get_user():
    return g.user  # (6)!


@app.get("/user-scope")
@auth.current_user(scope=["openid", "required_scope"])  # (7)!
def get_user_scope():
    return g.user
