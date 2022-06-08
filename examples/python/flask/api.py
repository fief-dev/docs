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


@app.get("/authenticated")
@auth.authenticated()  # (5)!
def get_authenticated():
    return g.access_token_info  # (6)!


@app.get("/authenticated-scope")
@auth.authenticated(scope=["openid", "required_scope"])  # (7)!
def get_authenticated_scope():
    return g.access_token_info


@app.get("/authenticated-permissions")
@auth.authenticated(permissions=["castles:read"])  # (8)!
def get_authenticated_permissions():
    return g.access_token_info
