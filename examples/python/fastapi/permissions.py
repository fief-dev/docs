from fastapi import Depends, FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

fief = FiefAsync(
    "https://example.fief.dev",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)

scheme = OAuth2AuthorizationCodeBearer(
    "https://example.fief.dev/authorize",
    "https://example.fief.dev/api/token",
    scopes={"openid": "openid", "offline_access": "offline_access"},
    auto_error=False,
)

auth = FiefAuth(fief, scheme)

app = FastAPI()


@app.get("/user")
async def get_user(
    access_token_info: FiefAccessTokenInfo = Depends(
        auth.authenticated(permissions=["castles:read"])
    ),
):
    return access_token_info
