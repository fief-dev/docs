from fastapi import Depends, FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

fief = FiefAsync(
    "https://fief.mydomain.com",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)

scheme = OAuth2AuthorizationCodeBearer(
    "https://fief.mydomain.com/authorize",
    "https://fief.mydomain.com/api/token",
    scopes={"openid": "openid", "offline_access": "offline_access"},
    auto_error=False,
)

auth = FiefAuth(fief, scheme)

app = FastAPI()


@app.get("/user")
async def get_user(
    access_token_info: FiefAccessTokenInfo = Depends(
        auth.authenticated(scope=["openid", "required_scope"])
    ),
):
    return access_token_info
