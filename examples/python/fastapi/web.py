from fastapi import Depends, FastAPI, HTTPException, Query, Request, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import APIKeyCookie
from fief_client import FiefAsync, FiefUserInfo
from fief_client.integrations.fastapi import FiefAuth


class CustomFiefAuth(FiefAuth):  # (1)!
    client: FiefAsync

    async def get_unauthorized_response(self, request: Request, response: Response):
        redirect_uri = request.url_for("auth_callback")  # (2)!
        auth_url = await self.client.auth_url(redirect_uri, scope=["openid"])  # (3)!
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,  # (4)!
            headers={"Location": str(auth_url)},
        )


fief = FiefAsync(  # (5)!
    "https://fief.mydomain.com",
    "YOUR_CLIENT_ID",
    "YOUR_CLIENT_SECRET",
)

SESSION_COOKIE_NAME = "user_session"
scheme = APIKeyCookie(name=SESSION_COOKIE_NAME, auto_error=False)  # (6)!
auth = CustomFiefAuth(fief, scheme)  # (7)!
app = FastAPI()


@app.get("/auth-callback", name="auth_callback")  # (8)!
async def auth_callback(request: Request, response: Response, code: str = Query(...)):
    redirect_uri = request.url_for("auth_callback")
    tokens, _ = await fief.auth_callback(code, redirect_uri)  # (9)!

    response = RedirectResponse(request.url_for("protected"))  # (10)!
    response.set_cookie(  # (11)!
        SESSION_COOKIE_NAME,
        tokens["access_token"],
        max_age=tokens["expires_in"],
        httponly=True,  # (12)!
        secure=False,  # ❌ Set this to `True` in production (13)!
    )

    return response


@app.get("/protected", name="protected")
async def protected(
    user: FiefUserInfo = Depends(auth.current_user()),  # (14)!
):
    return HTMLResponse(
        f"<h1>You are authenticated. Your user email is {user['email']}</h1>"
    )
