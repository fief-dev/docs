from fief_client import Fief

fief = Fief(
    "https://example.fief.dev",  # (1)!
    "YOUR_CLIENT_ID",  # (2)!
    "YOUR_CLIENT_SECRET",  # (3)!
)

redirect_url = "http://localhost:8000/callback"

auth_url = fief.auth_url(redirect_url, scope=["openid"])
print(f"Open this URL in your browser: {auth_url}")

code = input("Paste the callback code: ")

tokens, userinfo = fief.auth_callback(code, redirect_url)
print(f"Tokens: {tokens}")
print(f"Userinfo: {userinfo}")
