# React

[React](https://fr.reactjs.org) is one of the most popular JavaScript framework to build dynamic applications for the browser.

The Fief JavaScript client provides tools to help you integrate Fief authentication in your React project. Let's see how to use them!

## Install the client

```bash
npm install @fief/fief
```

## Application example

!!! question "This is for you if..."
    - [x] You want to handle all the OAuth authentication in your React application.

!!! abstract "Prerequisites"
    - [x] You have a React project setup.
    - [x] Make sure your Fief Client is [Public](../
    ../getting-started/clients.md#public-clients).
    - [x] Allow the following [Redirect URI](../../getting-started/clients.md#redirect-uris) on your Fief Client: `http://localhost:3000/callback`

In this example, we'll show you how to use the components and hooks provided by Fief to authenticate users and protect routes using [React Router](https://reactrouter.com/).

### Setup `FiefAuthProvider`

The `FiefAuthProvider` is a component providing all the necessary context for Fief, especially the Fief client and user session state. Every component nested inside this component will have access to the Fief hooks.

```ts title="App.tsx"
--8<-- "examples/javascript/react/src/App.tsx"
```

1. **Declare the `FiefAuthProvider`**

    This is necessary to give to nested components the right Fief context and makes the hooks working.

    It takes as properties the same arguments as the `Fief`  client.

2. **A `Header` component**

    Contains the navigation. We'll detail it in a moment.

3. **The `Routes` component from React Router**

4. **A public route**

    This route will be accessible by any visitor, even if not logged in.

5. **A private route**

    This route will be accessible only by logged in users. To do this, we wrap it in a `RequireAuth` component. We'll detail it in a moment.

6. **A callback route**

    The route where Fief will redirect the user to after a successful login to complete the OAuth authentication.

At this point, your React app has everything it needs to use Fief authentication tools!

### Implement callback route

After the user has successfully logged in on Fief, they will be redirected to your callback route. It needs to exchange the authorization code with a proper access token.

The role of this route is then just to perform this task before redirecting to another route.


```ts title="Callback.tsx"
--8<-- "examples/javascript/react/src/Callback.tsx"
```

1. **Hook to get the `FiefAuth` class**

    This is the [browser helper](./browser.md#fiefauth-reference) provided by the Fief JavaScript client.

2. **We call the `authCallback` method**

    This method takes care of everything: retrieving the authorization code in the query parameters, exchanging it with a fresh access token and save it in the browser session.

    Once the promise is resolved, all we have to do is to redirect back to the index page.

### Protect private routes

Usually, you'll need to prevent visitors from accessing a page if they're not logged in.

To do this, we implement a simple component that'll check for the authentication state and automatically redirect to the Fief authentication page if the user is not logged in.

```ts title="RequireAuth.tsx"
--8<-- "examples/javascript/react/src/RequireAuth.tsx"
```

1. **Hook to get the `FiefAuth` class**

    This is the [browser helper](./browser.md#fiefauth-reference) provided by the Fief JavaScript client.

2. **Hook to get the authentication state**

    This hook simply returns a boolean stating if a user is logged in or not.

3. **Redirect to Fief authentication page**

    With this effect, we automatically redirect the user to the Fief authentication page so that they can log in.

    The `redirectToLogin` method only needs the redirect URL where the user will be redirected after a successful authentication on Fief: the `/callback` route.

### Manage authentication

You have access to a set of hooks to help you manage the authentication state of the user, like retrieving their information, redirect them to the authentication page or logout them.

In the example below, we show a simple header with navigation links and a login or logout button.

```ts title="Header.tsx"
--8<-- "examples/javascript/react/src/Header.tsx"
```

1. **Hook to get user information**

    It'll return you an object with the user information, or `null` if no user is authenticated.

2. **Callback to redirect to Fief authentication page**

    When the login button is clicked, this callback will redirect to the Fief authentication page. This is exactly the same thing we showed in the `RequireAuth` component.

3. **Callback to logout**

    When the logout button is clicked, this callback will start the logout process.

    The `FiefAuth` helper takes care of clearing the local session and redirect to the Fief logout page so that the session on Fief's side can also be cleared.

    All it needs is the redirect URL where the user will be redirected after a successful logout. Here, we go back to the index route.

## React reference

### Components

#### `FiefAuthProvider`

Provides all the necessary context for Fief, especially the Fief client and user session state. Every component nested inside this component will have access to the Fief hooks.

!!! abstract "Parameters"
    * `baseURL: string`: Base URL of your Fief tenant.
    * `clientID: string`: ID of your Fief client.
    * `clientSecret: string | undefined`: Secret of your Fief client. **It's not recommended to use it in the context of a browser app, since it can be easily found by the end-user in the source code. The recommended way is to use a [Public client](../../getting-started/clients.md#public-clients).**
    * `encryptionKey: string | undefined`: Encryption key of your Fief client. Necessary only if [ID Token encryption](../../going-further/id-token-encryption.md) is enabled.

### Hooks

#### `useFiefAuth`

Returns an instance of the [`FiefAuth` browser helper](./browser.md#fiefauth-reference).

!!! example
    ```ts
    const fiefAuth = useFiefAuth();
    ```

#### `useFiefIsAuthenticated`

Returns whether there is a valid user session.

!!! example
    ```ts
    const isAuthenticated = useFiefIsAuthenticated();
    ```

#### `useFiefTokenInfo`

Returns the token information object available in session, or `null` if no current session.

!!! example
    ```js
    const tokenInfo = useFiefTokenInfo()
    console.log(tokenInfo); // {"access_token": "ACCESS_TOKEN", "id_token": "ID_TOKEN", "token_type": "bearer", "expires_in": 3600}
    ```

#### `useFiefUserinfo`

Returns the user information object available in session, or `null` if no current session.

!!! example
    ```js
    const userinfo = useFiefUserinfo();
    console.log(userinfo);
    ```
