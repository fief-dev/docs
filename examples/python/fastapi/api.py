from fastapi import Depends, FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

fief = FiefAsync(  # (1)!
    "https://fief.mydomain.com",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)

scheme = OAuth2AuthorizationCodeBearer(  # (2)!
    "https://fief.mydomain.com/authorize",  # (3)!
    "https://fief.mydomain.com/api/token",  # (4)!
    scopes={"openid": "openid", "offline_access": "offline_access"},
    auto_error=False,  # (5)!
)

auth = FiefAuth(fief, scheme)  # (6)!

app = FastAPI()


@app.get("/user")
async def get_user(
    access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated()),  # (7)!
):
    return access_token_info
