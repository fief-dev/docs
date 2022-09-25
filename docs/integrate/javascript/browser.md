# Browser

It's possible to manage authentication with Fief entirely within the browser, using a bit of JavaScript.

To help you in this task, the Fief JavaScript client provides tools dedicated to the browser environment. Let's see how to use them!

## Install the client

The recommended way to install the client is to use `npm`:

```bash
npm install @fief/fief
```

However, if you don't use a JavaScript bundler, like Webpack, you can include the package directly in a browser script, thanks to [UNPKG CDN](https://unpkg.com):

```html
<script src="https://unpkg.com/@fief/fief"></script> <!-- (1)! -->
<script>
    console.log(fief); // Module is available globally under the `fief` variable
</script>
```

1. **This will always load the latest version**

    You should pin the version to avoid problems when we update the client and improve the loading time.

    For example, to load the version `0.6.1`:

    ```html
    <script src="https://unpkg.com/@fief/fief@0.6.1/build/index.umd.js"></script>
    ```

## Application example

!!! question "This is for you if..."
    - [x] You want to handle all the OAuth authentication in the browser.

!!! abstract "Prerequisites"
    - [x] Make sure your Fief Client is [Public](../
    ../getting-started/clients.md#public-clients).
    - [x] Allow the following [Redirect URI](../../getting-started/clients.md#redirect-uris) on your Fief Client: `http://localhost:8080/callback.html`
    - [x] Install [http-server](https://www.npmjs.com/package/http-server), a simple NodeJS HTTP server: `npm i --global http-server`

In this example, we'll show you a very simple HTML and JavaScript application to perform the OAuth2 authentication. We'll define two pages:

* `index.html`: it'll show if the user is logged in or not, and display a Login button.
* `callback.html`: the page Fief will redirect the user to after a successful login to complete the OAuth authentication.

Let's see the first one:

```html title="index.html"
--8<-- "examples/javascript/browser/index.html"
```

1. **HTML block for when the user is not logged in**

    It simply contains a generic title and a **login button**.

2. **HTML block for when the user is logged in**

    We greet the logged in user with their email address and show them a **logout button**.

3. **Fief client instantiation**

    As we showed in the [JavaScript section](./index.md), we instantiate here a Fief client here with the base tenant URL and client credentials.

    Notice here that we omit the **Client Secret**. Indeed, the secret can't be kept safe in the browser: the end-user can easily find it in the source code.

    That's why we set the Fief Client as [Public](../
    ../getting-started/clients.md#public-clients): we allow it to make authentication requests without the Client Secret.

4. **Fief helper for the browser**

    This is the helper doing the tedious work for you in the browser. All it needs is an instance of the Fief client.

    Under the hood, `FiefAuth` will store the user session data on the browser [SessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage). This is how we'll maintain the logged-in state of the user during its visit.

5. **When the login button is clicked, redirect to Fief login page**

    We simply add an event listener on the button to start the authorization process when it's clicked.

    We use the `FiefAuth` helper for this. All it needs is the redirect URL where the user will be redirected after a successful authentication on Fief: the `callback.html` page.

    Under the hood, `FiefAuth` takes care of generating a [PKCE code challenge](../../going-further/pkce.md) for maximum security!

6. **When the logout button is clicked, clear session and redirect to Fief logout page**

    We simply add an event listener on the button to logout the user.

    The `FiefAuth` helper takes care of clearing the local session and redirect to the Fief logout page so that the session on Fief's side can also be cleared.

    All it needs is the redirect URL where the user will be redirected after a successful logout. Here, we go back to the `index.html` page.

7. **Get user information in session**

    The `getUserinfo` method of `FiefAuth` allows to retrieve the user information stored in session, if any.

8. **User information is available**

    The user is logged in 👍 We can show the right HTML block and fill the user email to greet them properly.

9. **User information is not available**

    The user is not logged in 😔 We can show the right HTML block with the login button.

As you can see, the JavaScript code is quite short! Most of the tedious work is done by the `FiefAuth` helper, which takes care of storing the session in the browser and authenticating the client with PKCE.

Let's now see the `callback.html` page:

```html title="callback.html"
--8<-- "examples/javascript/browser/callback.html"
```

1. **This doesn't change**

    We once again instantiate a Fief client and the browser helper.

2. **We call the `authCallback` method**

    This method takes care of everything: retrieving the authorization code in the query parameters, exchanging it with a fresh access token and save it in the browser session.

    Once the promise is resolved, all we have to do is to redirect back to the `index.html` page.

That's it! Assuming you have both files in a directory named `app-directory`, you can run this application using `http-server`:

```bash
http-server app-directory/
```

It'll make it available on [http://localhost:8080](http://localhost:8080). The first time you open it, you'll be logged out:

![Logged out in browser application](/assets/images/browser-logged-out.png)

If you click on the **Login** button, you'll be redirected to Fief to authenticate. Once done, you'll be redirected to your application and should be properly logged in:

![Logged in in browser application](/assets/images/browser-logged-in.png)

You can also try the **Logout** button to see how the session is cleared.
