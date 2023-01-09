# Express

[Express](https://expressjs.com/) is a highly popular Node.js web framework.

The Fief JavaScript client provides tools to help you integrate Fief authentication in your Express project. Let's see how to use them!

## Install the client

```bash
npm install @fief/fief
```

## API example

!!! question "This is for you if..."
    - [x] Your Express backend will work as a pure REST API.
    - [x] You have a separate frontend, like a JavaScript or mobile app, that'll take care of the OAuth2 flow.

In this first example, we won't implement routes to perform the OAuth2 authentication. The goal here is just to show you **how to protect your API route with a Fief access token**.

```js title="app.js"
--8<-- "examples/javascript/express/api.js"
```

1. **Fief client instantiation**

    As we showed in the [standard JavaScript section](../index.md), we instantiate here a Fief client here with the base tenant URL and client credentials.

2. **Middleware helper**

    The `fiefExpress` module exposes the `createMiddleware` function which returns a proper middleware to use in your Express routes.

3. **The Fief client**

    The first mandatory parameter is the Fief client we just created above.

4. **The token getter**

    The second mandatory parameter is **a function retrieving the access token from an Express request**.

    You can create yours, as long as it follows the [TokenGetter](https://fief-dev.github.io/fief-js/types/server.TokenGetter.html) signature, or you can use the ones we provide.

    Here, we use [`authorizationSchemeGetter`](https://fief-dev.github.io/fief-js/functions/server.authorizationSchemeGetter.html), which will retrieve the token from an `Authorization` header with the `Bearer` scheme: `Authorization: Bearer ACCESS_TOKEN`

5. **Use the middleware in your route**

    If you want to protect a route, all you need to do is to add your `fiefAuthMiddleware` instance as a middleware.

    When your handler is called, you're sure the user is authenticated with a valid session.

6. **`accessTokenInfo` is available in `req`**

    In your route handler, you have access to the `accessTokenInfo` object in `req`.

    `accessTokenInfo` is a [`FiefAccessTokenInfo`](https://fief-dev.github.io/fief-js/interfaces/index.FiefAccessTokenInfo.html) object containing the ID of the user, the list of allowed scopes and permissions and the raw access token.

7. **Check for scopes**

    `fiefAuthMiddleware` accepts an optional `scope` parameter where you can list the scope required to access this route.

    If the access token doesn't have the required scope, the forbidden response is returned.

8. **Check for permissions**

    `fiefAuthMiddleware` accepts an optional `perrmissions` parameter where you can list the permissions required to access this route.

    If the access token doesn't have the required permissions, the forbidden response is returned.

## Web application example

!!! question "This is for you if..."
    - [x] Your Express backend will render HTML pages.
    - [x] Your application is intended to be used in a browser.

!!! abstract "Prerequisites"
    - [x] Allow the following [Redirect URI](../../../configure/clients.md#redirect-uris) on your Fief Client: `http://localhost:3O00/auth-callback`

--8<-- "reusables/web-application-motivation.md"

```js title="app.js"
--8<-- "examples/javascript/express/web.js"
```

1. **Define a session cookie name constant**

    As we said, we'll use a cookie to maintain the user session.

    For convenience, we set its name in a constant.

2. **Define a redirect URI constant**

    After the user has succesfully authenticated on Fief, our user will need to be redirected to our application so we can get the access token and set our session.

    This constant is an absolute URL to our `/auth-callback` route we define below.

    In a production environment, it should corresponds to your actual domain.

3. **Implement a user information cache**

    To make sure we don't call the Fief API every time we want the user data, we'll cache it in our application. It'll be way more performant!

    To do this, we impement a class following the [`IUserInfoCache`](https://fief-dev.github.io/fief-js/interfaces/server.IUserInfoCache.html) interface.

    In this example, we use very simple approach that will just store the data in memory. If your server is rebooted, the cache will be lost.

    It can work quite well when starting, but you'll probably need more robust approaches in the long run, like writing to a Redis store. The good thing is that you'll only need to change this class when the time comes!

4. **This doesn't change from the previous example**

    The `Fief` client is always at the heart of the integration 😉

5. **Define a custom unauthorized response**

    By default, the Express integration will return a 401 response when the user is not authenticated.

    In our case here, we want them to be redirected to Fief authentication page.

6. **We generate an authorization URL on the Fief server**

    Thanks to the [`getAuthURL` method](https://fief-dev.github.io/fief-js/classes/index.Fief.html#getAuthURL) on the Fief client, we can automatically generate the authorization URL on the Fief server.

7. **We build a redirect response**

    We redirect the user to the Fief authorization URL.

8. **We use a cookie getter**

    Contrary to the previous examples, we expect the access token to be passed in a cookie. Thus, we use the provided [`cookieGetter`](https://fief-dev.github.io/fief-js/functions/server.cookieGetter.html) function.

    Notice that we pass it the cookie name, `SESSION_COOKIE_NAME`, as parameter.

9. **We use our custom unauthorized response**

    We tell the middleware about our customer handler we defined above.

10. **We use our user information cache**

    We tell the middleware about our user information cache, so it can use it to save and retrieve the data.

11. **We implement an `/auth-callback` route**

    This is the route that'll take care of exchanging the authorization code with a fresh access token and save it in a cookie.

12. **We generate an access token**

    We finish the OAuth2 flow by exchanging the authorization code with a fresh access token.

13. **We cache the user information**

    When a user has successfully authenticated, we do not only get the access token: we also get an [ID token](../../../getting-started/oauth2.md#access-token-and-id-token) which already contains the user information.

    Hence, we'll take this opportunity to store it in our cache! The ID token is automatically decoded by [`fiefClient.authCallback`](https://fief-dev.github.io/fief-js/classes/index.Fief.html#authCallback) method.

    Thus, we just have to use our cache helper to store it!

14. **We build a new cookie containing the access token**

    The response will contain a `Set-Cookie` header instructing the browser to save the access token in its memory. This method allows us to configure each properties of the cookie.

    You can read more about HTTP cookies on the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).

15. **Set the cookie as `HTTPOnly`**

    For such sensitive values, it's strongly recommended to set the cookie as `HTTPOnly`. It means that it won't be possible to read its value from JavaScript, reducing potential attacks.

16. **Set the cookie as secure in production**

    For such sensitive values, it's strongly recommended to set the cookie as `Secure`. It tells the browser to send the cookie **only on HTTPS (SSL)** connection, reducing the risk of the access token to be stolen by a attacker between the client and the server.

    However, in a local environment, you usually don't serve your application with SSL. That's why we set it to `false` in this example. A common approach to handle this is to have an environment variable to control this parameter, so you can disable it in local and enable it in production.

17. **We implement a `/protected` route**

    Now, we can just use our `fiefAuthMiddleware` to protect our routes.

18. **`user` object is available in `req`**

    If the request is properly authenticated, the middleware will automatically add the `user` obkect to `req`.

    `user` is a [`FiefUserInfo`](https://fief-dev.github.io/fief-js/interfaces/index.FiefUserInfo.html) object containing the user data. If it's not available in cache, it's automatically retrieved from the Fief API.

That's it! If you run this application and go to [http://localhost:3000/protected](http://localhost:3000/protected), you'll be redirected to the Fief login page and experience the authentication flow before getting back to this route with a proper authentication cookie.
