import uuid
from datetime import datetime
from typing import Dict, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, Request, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import APIKeyCookie
from fief_client import FiefAsync, FiefUserInfo
from fief_client.integrations.fastapi import FiefAuth


class CustomFiefAuth(FiefAuth):
    client: FiefAsync

    async def get_unauthorized_response(self, request: Request, response: Response):
        redirect_uri = request.url_for("auth_callback")
        auth_url = await self.client.auth_url(redirect_uri, scope=["openid"])
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            headers={"Location": auth_url},
        )


class MemoryUserInfoCache:  # (1)!
    def __init__(self) -> None:
        self.storage: Dict[uuid.UUID, FiefUserInfo] = {}  # (2)!

    async def get(self, user_id: uuid.UUID) -> Optional[FiefUserInfo]:  # (3)!
        return self.storage.get(user_id)

    async def set(self, user_id: uuid.UUID, userinfo: FiefUserInfo) -> None:  # (4)!
        self.storage[user_id] = userinfo


memory_userinfo_cache = MemoryUserInfoCache()  # (5)!


async def get_memory_userinfo_cache() -> MemoryUserInfoCache:  # (6)!
    return memory_userinfo_cache


fief = FiefAsync(
    "https://example.fief.dev",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)

SESSION_COOKIE_NAME = "user_session"
scheme = APIKeyCookie(name=SESSION_COOKIE_NAME, auto_error=False)
auth = CustomFiefAuth(
    fief, scheme, get_userinfo_cache=get_memory_userinfo_cache  # (7)!
)
app = FastAPI()


@app.get("/auth-callback", name="auth_callback")
async def auth_callback(
    request: Request,
    response: Response,
    code: str = Query(...),
    memory_userinfo_cache: MemoryUserInfoCache = Depends(  # (8)!
        get_memory_userinfo_cache
    ),
):
    redirect_uri = request.url_for("auth_callback")
    tokens, userinfo = await fief.auth_callback(code, redirect_uri)

    response = RedirectResponse(request.url_for("protected"))
    response.set_cookie(
        SESSION_COOKIE_NAME,
        tokens["access_token"],
        expires=int(datetime.now().timestamp() + tokens["expires_in"]),
        httponly=True,
        secure=False,
    )

    await memory_userinfo_cache.set(uuid.UUID(userinfo["sub"]), userinfo)  # (9)!

    return response


@app.get("/protected", name="protected")
async def protected(
    user: FiefUserInfo = Depends(auth.current_user()),  # (10)!
):
    return HTMLResponse(
        f"<h1>You are authenticated. Your user email is {user['email']}</h1>"
    )
