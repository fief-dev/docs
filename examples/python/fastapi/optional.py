from typing import Optional

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


@app.get("/optional-user")
async def get_optional_user(
    access_token_info: Optional[FiefAccessTokenInfo] = Depends(
        auth.authenticated(optional=True)
    ),
):
    if access_token_info is None:
        return {"message": "Anonymous user"}
    return access_token_info
