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

5. **`current_user` decorator**

    This is where the magic happens: `FiefAuth` gives you a `current_user` decorator to check for the access token and optionally for required scopes.

    If everything goes well, the route logic will be executed.

6. **`user` dictionary is available in `g`**

    When a valid access token is found in the request, the `current_user` decorator will automatically add the `user` property to the global [`g` application context of Flask](https://flask.palletsprojects.com/en/api/#flask.g).

    This `user` property is a dictionary containing the ID of the user, the list of allowed scopes and the raw access token.

7. **Check for scopes**

    The `current_user` decorator accepts an optional `scope` argument where you can list the scope required to access this route.

    If the access token doesn't have the required scope, the `FiefAuthForbidden` is raised.

And that's about it!

## Web application example

!!! question "This is for you if..."
    - [x] Your Flask backend will render HTML pages.
    - [x] Your application is intended to be used in a browser.

--8<-- "reusables/web-application-motivation.md"

```py title="app.py"
--8<-- "examples/python/flask/web.py"
```

1. **This doesn't change from the previous example**

    The `Fief` client is always at the heart of the integration 😉

2. **We use a cookie getter**

    Contrary to the previous examples, we expect the access token to be passed in a cookie. Thus, we use the `get_cookie` getter.

    Notice that we set the name of this cookie through the `SESSION_COOKIE_NAME` constant.

3. **We change the error handler for `FiefAuthUnauthorized`**

    This time, we'll generate a redirect response so the user can login on Fief.

4. **We build the redirect URL**

    This points to our `/auth-callback` route that we define below.

5. **We generate an authorization URL on the Fief server**

    Thanks to the `auth_url` method on the Fief client, we can automatically generate the authorization URL on the Fief server.

6. **We build a redirect response**

    We redirect the user to the Fief authorization URL.

7. **We implement an `/auth-callback` route**

    This is the route that'll take care of exchanging the authorization code with a fresh access token and save it in a cookie.

8.  **We generate an access token**

    We finish the OAuth2 flow by exchanging the authorization code with a fresh access token.

9.  **We build a redirection to the `/protected` route**

    The user will now be correctly authenticated to our web application. Thus, we can redirect them to a protected page.

10. **We build a new cookie containing the access token**

    The response will contain a `Set-Cookie` header instructing the browser to save the access token in its memory. This method allows us to configure each properties of the cookie.

    You can read more about HTTP cookies on the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).

11. **Set the cookie as `HTTPOnly`**

    For such sensitive values, it's strongly recommended to set the cookie as `HTTPOnly`. It means that it won't be possible to read its value from JavaScript, reducing potential attacks.

12. **Set the cookie as secure in production**

    For such sensitive values, it's strongly recommended to set the cookie as `Secure`. It tells the browser to send the cookie **only on HTTPS (SSL)** connection, reducing the risk of the access token to be stolen by a attacker between the client and the server.

    However, in a local environment, you usually don't serve your application with SSL. That's why we set it to `False` in this example. A common approach to handle this is to have an environment variable to control this parameter, so you can disable it in local and enable it in production.

13. **Use the `current_user` decorator as usual**

    This doesn't change from the previous example. The dependency will check if the cookie is available in the request and proceed if everything goes well.

    Otherwise, an `FiefAuthUnauthorized` error will be raised and the user will be redirected to the Fief login page.

That's it! If you run this application and go to [http://localhost:8000/protected](http://localhost:8000/protected), you'll be redirected to the Fief login page and experience the authentication flow before getting back to this route with a proper authentication cookie.
