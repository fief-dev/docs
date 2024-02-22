from fief_client import Fief
from fief_client.integrations.flask import (
    FiefAuth,
    FiefAuthForbidden,
    FiefAuthUnauthorized,
    get_authorization_scheme_token,
)
from flask import Flask, g

fief = Fief(
    "https://fief.mydomain.com",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)

auth = FiefAuth(fief, get_authorization_scheme_token())

app = Flask(__name__)


@app.errorhandler(FiefAuthUnauthorized)
def fief_unauthorized_error(e):
    return "", 401


@app.errorhandler(FiefAuthForbidden)
def fief_forbidden_error(e):
    return "", 403


@app.get("/authenticated")
@auth.authenticated(optional=True)
def get_authenticated():
    if g.access_token_info is None:
        return {"message": "Anonymous user"}
    return g.access_token_info
