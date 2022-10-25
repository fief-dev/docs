The examples we showed previously are working well in a pure REST API context: a frontend, like interactive documentation, a JavaScript application or a mobile app will take care of the OAuth2 authentication flow to retrieve an access token before making request to your API.

Another common context is **traditional web application**, where the server takes care of generating HTML pages before returning it to the browser. In this case, we'll need some routes to redirect the user to the Fief login page if they're not authenticated and take care of storing the access token somewhere. This is what'll show in this example.

Besides, we'll usually need the basic information about the authenticated user, like its email or the values of the custom [user fields](/getting-started/user-fields). We'll see how we can use it.

Basically, here's what we'll do:

1. This time, we'll expect the access token to be passed through a traditional **cookie** instead of an HTTP header. Cookies are very convenient when designing web apps because they are handled automatically by the browser.
2. If the cookie is not present, we'll **redirect the user to the Fief login page**. Once again, the browser will help us a lot here since it'll automatically follow the redirection.
3. Upon successful login, Fief will automatically **redirect the user to the callback route**. This callback route will take care of **setting a new cookie containing the access token**. It means that the access token will be safely stored in the browser memory.
4. Finally, the user is redirected back to the protected route. The browser will automatically send the cookie containing the access token: our request is now authenticated!
