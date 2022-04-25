!!! warning "`_COOKIE_SECURE` flag should be `True` in production"
    Browser cookies support the [`Secure` flag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#secure), which tells the browser to not forward the cookie if the site is not requested in HTTPS.

    For your convenience when starting Fief on your local machine, the [Quickstart](quickstart.md) command will set those flags to `False` for every Fief cookies.

    However, for security reasons, it's **strongly recommended** to set those flags to `True` (the default if not specified) when deploying to production.
