# Flask

[Flask](https://flask.palletsprojects.com/) is probably the most popular Python web framework.

The Fief Python client provides tools to help you integrate Fief authentication in your Flask project. Let's see how to use them!

## Install the client

Install the Fief client with the optional Flask dependencies:

```bash
pip install "fief-client[flask]"
```

## API example

!!! question "This is for you if..."
    - [x] Your Flask backend will work as a pure REST API.
    - [x] You have a separate frontend, like a JavaScript or mobile app, that'll take care of the OAuth2 flow.

In this first example, we won't implement routes to perform the OAuth2 authentication. The goal here is just to show you **how to protect your API route with a Fief access token**.

```py title="app.py"
--8<-- "examples/python/flask/api.py"
```

1. **Fief client instantiation**

    As we showed in the [standard Python section](./index.md), we instantiate here a Fief client here with the base tenant URL and client credentials.

2. **Fief helper for Flask**

    This is the helper doing the tedious work for you with Flask. It first needs an instance of the Fief client we created above and **a function retrieving the access token from the Flask request**.

    It's a simple function which can use the global `request` object to retrieve the access token.

    For convenience, we provide two of them: `get_authorization_scheme_token` and `get_cookie`.

3. **Error handler for `FiefAuthUnauthorized`**

    When a protected route is called without a valid access token, the Fief helper will raise the `FiefAuthUnauthorized`.

    By registering a Flask error handler, we can catch this error and customize the response returned to the user. Here, we just return an empty response with the 401 status code.

4. **Error handler for `FiefAuthForbidden`**

    When a request is made with a valid access token but without the required scope, the Fief helper will raise the `FiefAuthForbidden`.

    By registering a Flask error handler, we can catch this error and customize the response returned to the user. Here, we just return an empty response with the 403 status code.

5. **`authenticated` decorator**

    This is where the magic happens: `FiefAuth` gives you a `authenticated` decorator to check for the access token and optionally for required scopes.

    If everything goes well, the route logic will be executed.

6. **`access_token_info` dictionary is available in `g`**

    When a valid access token is found in the request, the `access_token_info` decorator will automatically add the `access_token_info` property to the global [`g` application context of Flask](https://flask.palletsprojects.com/en/api/#flask.g).

    This `access_token_info` property is a [`FiefAccessTokenInfo`](https://fief-dev.github.io/fief-python/fief_client.html#FiefAccessTokenInfo) dictionary containing the ID of the user, the list of allowed scopes and permissions and the raw access token.

7. **Check for scopes**

    The `access_token_info` decorator accepts an optional `scope` argument where you can list the scope required to access this route.

    If the access token doesn't have the required scope, `FiefAuthForbidden` error is raised.

8. **Check for permissions**

    The `access_token_info` decorator accepts an optional `permissions` argument where you can list the permissions required to access this route.

    If the user doesn't have the required permissions, `FiefAuthForbidden` is raised.

And that's about it!

### Optional user

Sometimes, you need to have a route retrieving the user if there is one authenticated, but **still working** if there none. To do this, you can leverage the `optional` parameter of the `authenticated` decorator.

```py title="app.py" hl_lines="32"
--8<-- "examples/python/flask/optional.py"
```

## Web application example

!!! question "This is for you if..."
    - [x] Your Flask backend will render HTML pages.
    - [x] Your application is intended to be used in a browser.

!!! abstract "Prerequisites"
    - [x] Allow the following [Redirect URI](../../admin-dashboard/clients.md#redirect-uris) on your Fief Client: `http://localhost:8000/auth-callback`

--8<-- "reusables/web-application-motivation.md"

```py title="app.py"
--8<-- "examples/python/flask/web.py"
```

1. **Define a secret key for Flask**

    We'll use the [Sessions mechanism from Flask](https://flask.palletsprojects.com/en/2.1.x/api/#sessions) to keep user information in cache. To enable it, we need to set a secret key for Flask.

    Generate a **strong** passphrase and **don't share it**.

    --8<-- "reusables/hardcoded-secrets-callout.md"

2. **This doesn't change from the previous example**

    The `Fief` client is always at the heart of the integration 😉

3. **We define a function to retrieve user information from cache**

    To make sure we don't call the Fief API every time we want the user data, we'll cache it in our application. It'll be way more performant!

    To do this, we implement a simple function allowing us to retrieve the user information given a user ID.

    In this example, we simply use the [Sessions mechanism from Flask](https://flask.palletsprojects.com/en/2.1.x/api/#sessions), but it can be something more complex, like reading from a Redis store.

4. **We define a function to set user information in cache**

    As you probably have guessed, we need the other side of the operation: saving user information in cache.

    To do this, we implement a simple function accepting a user ID and a [`FiefUserInfo`](https://fief-dev.github.io/fief-python/fief_client.html#FiefUserInfo) dictionary as arguments. There, you'll need to store this data in cache.

    In this example, we simply use the [Sessions mechanism from Flask](https://flask.palletsprojects.com/en/2.1.x/api/#sessions), but it can be something more complex, like writing to a Redis store.

5. **We use a cookie getter**

    Contrary to the previous examples, we expect the access token to be passed in a cookie. Thus, we use the `get_cookie` getter.

    Notice that we set the name of this cookie through the `SESSION_COOKIE_NAME` constant.

6. **We pass both `get_userinfo_cache` and `set_userinfo_cache` as arguments**

    Basically, we tell `FiefAuth` to use the caching functions we implemented when we want to get the user information.

    That's why it's important to strictly follow the functions signature presented above: `FiefAuth` will call them inside its logic.

7. **We change the error handler for `FiefAuthUnauthorized`**

    This time, we'll generate a redirect response so the user can login on Fief.

8. **We build the redirect URL**

    This points to our `/auth-callback` route that we define below.

9.  **We generate an authorization URL on the Fief server**

    Thanks to the `auth_url` method on the Fief client, we can automatically generate the authorization URL on the Fief server.

10. **We build a redirect response**

    We redirect the user to the Fief authorization URL.

11. **We implement an `/auth-callback` route**

    This is the route that'll take care of exchanging the authorization code with a fresh access token and save it in a cookie.

12. **We generate an access token**

    We finish the OAuth2 flow by exchanging the authorization code with a fresh access token.

13. **We build a redirection to the `/protected` route**

    The user will now be correctly authenticated to our web application. Thus, we can redirect them to a protected page.

14. **We build a new cookie containing the access token**

    The response will contain a `Set-Cookie` header instructing the browser to save the access token in its memory. This method allows us to configure each properties of the cookie.

    You can read more about HTTP cookies on the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).

15. **Set the cookie as `HTTPOnly`**

    For such sensitive values, it's strongly recommended to set the cookie as `HTTPOnly`. It means that it won't be possible to read its value from JavaScript, reducing potential attacks.

16. **Set the cookie as secure in production**

    For such sensitive values, it's strongly recommended to set the cookie as `Secure`. It tells the browser to send the cookie **only on HTTPS (SSL)** connection, reducing the risk of the access token to be stolen by a attacker between the client and the server.

    However, in a local environment, you usually don't serve your application with SSL. That's why we set it to `False` in this example. A common approach to handle this is to have an environment variable to control this parameter, so you can disable it in local and enable it in production.

17. **We cache the user information**

    When a user has successfully authenticated, we do not only get the access token: we also get an [ID token](../../getting-started/oauth2.md#access-token-and-id-token) which already contains the user information.

    Hence, we'll take this opportunity to store it in our cache! The ID token is automatically decoded by [`fief.auth_callback`](https://fief-dev.github.io/fief-python/fief_client.html#Fief.auth_callback) method.

    Thus, we just have to use our cache function to store it!

18. **Use the `current_user` decorator**

    This time, we use the `current_user` decorator instead of `authenticated`. Under the hood, it'll stil call `authenticated` and check if the cookie is available in the request and proceed if everything goes well. However, it'll return you a [`FiefUserInfo`](https://fief-dev.github.io/fief-python/fief_client.html#FiefUserInfo) dictionary containing the data of the user.

    If the request is not authenticated, an `FiefAuthUnauthorized` error will be raised and the user will be redirected to the Fief login page.

19. **`user` dictionary is available in `g`**

    If the request is properly authenticated, the `current_user` decorator will automatically add the `user` property to the global [`g` application context of Flask](https://flask.palletsprojects.com/en/api/#flask.g).

    This `user` property is a [`FiefUserInfo`](https://fief-dev.github.io/fief-python/fief_client.html#FiefUserInfo) dictionary containing the user data. If it's not available in cache, it's automatically retrieved from the Fief API.

That's it! If you run this application and go to [http://localhost:8000/protected](http://localhost:8000/protected), you'll be redirected to the Fief login page and experience the authentication flow before getting back to this route with a proper authentication cookie.

!!! tip "`current_user` can also check for scope and permissions"
    In a similar way as we shown in the [API example](#api-example), you can also require the access token to be granted a list of **scopes** or the user to be granted a list of **permissions**.

    ```py
    @app.get("/protected")
    @auth.current_user(scope=["openid", "required_scope"])
    def protected():
        ...
    ```

    ```py
    @app.get("/protected")
    @auth.current_user(permissions=["castles:read"])
    def protected():
        ...
    ```

!!! tip "You can also optionally require the user"
    In a similar way as we shown in the [API example](#optional-user), you can leverage the `optional` parameter to make the route works even if no user is authenticated.

    ```py
    @app.get("/protected")
    @auth.current_user(optional=True)
    def protected():
        user = g.user
        if user is None:
            return f"<h1>You are an anonymous user.</h1>"
        return f"<h1>You are authenticated. Your user email is {user['email']}</h1>"

    ```
