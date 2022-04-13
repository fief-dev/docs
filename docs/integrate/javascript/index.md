# JavaScript

We provide an official client for JavaScript. You can install it with `npm`:

```bash
npm install @fief/fief
```

## Create a `Fief` client

The Fief client provides all the necessary methods to manage OAuth2 authentication, validate access tokens and refresh them.

```js
const fief = new Fief({
  baseURL: 'https://example.fief.dev',  // (1)!
  clientId: 'YOUR_CLIENT_ID',  // (2)!
  clientSecret: 'YOUR_CLIENT_SECRET', // (3)!
});
```

1. **Base URL of your Fief tenant**

    You can find it in the admin dashboard, in the **Tenants** list. [More info](../../getting-started/tenants.md#base-url)

    ![Find base URL in admin dashboard](/assets/images/admin-tenants.png)

2. **ID of your Fief client**

    You can find it in the admin dashboard, in the **Clients** list. [More info](../../getting-started/clients.md)

    ![Find Client ID in admin dashboard](/assets/images/admin-clients-detail.png)

    !!! info
        A first client is always created for you when you create your workspace. When getting started, you should use this one.

3. **Secret of your Fief client**

    You can find it in the admin dashboard, in the **Clients** list. [More info](../../getting-started/clients.md)

    ![Find Client Secret in admin dashboard](/assets/images/admin-clients-detail.png)

    !!! info
        A first client is always created for you when you create your workspace. When getting started, you should use this one.

--8<-- "reusables/client-secret-browser-callout.md"

## What's next?

JavaScript being a vast ecosystem both for browsers and servers, integration paths can be quite different following your use-case.

To help you further, we provide you helpers and examples for popular JavaScript frameworks and technologies, like React.

[Integrate in browser with plain JavaScript](browser.md){ .md-button }
[Integrate with React](react.md){ .md-button }
{: .buttons }

## `Fief` reference

!!! abstract "Constructor"
    * `baseURL: string`: Base URL of your Fief tenant.
    * `clientID: string`: ID of your Fief client.
    * `clientSecret: string | undefined`: Secret of your Fief client. **It's not recommended to use it in the context of a browser app, since it can be easily found by the end-user in the source code. The recommended way is to use a [Public client](../../getting-started/clients.md#public-clients).**
    * `encryptionKey: string | undefined`: Encryption key of your Fief client. Necessary only if [ID Token encryption](../../going-further/id-token-encryption.md) is enabled.

### `getAuthURL`

Returns an authorization URL.

!!! abstract "Parameters"
    * `redirectURI: string`: Your callback URI where the user will be redirected after Fief authentication.
    * `state: string | undefined`: Optional string that will be returned back in the callback parameters to allow you to retrieve state information.
    * `scope: string[] | undefined`: Optional list of scopes to ask for.
    * `codeChallenge: string | undefined`: Optional code challenge for [PKCE process](.../../../../going-further/pkce.md).
    * `codeChallengeMethod: 'plain' | 'S256' | undefined`: Method used to hash the PKCE code challenge.
    * `extras_params: Record<string, string> | undefined`: Optional object containing specific parameters.

!!! example
    ```ts
    const authURL = await fief.getAuthURL({
        redirectURI: 'http://localhost:8000/callback',
        scope: ['openid'],
    );
    ```

### `authCallback`

Returns valid tokens and user info in exchange of an authorization code.

!!! abstract "Parameters"
    * `code: string`: The authorization code.
    * `redirectURI: string`: The exact same `redirectURI` you passed to the authorization URL.
    * `codeVerifier: string | undefined`: The raw [PCKE](../../going-further/pkce.md) code used to generate the code challenge during authorization.

!!! example
    ```ts
    const [tokens, userinfo] = await fief.authCallback('CODE', 'http://localhost:8000/callback');
    ```

### `authRefreshToken`

Returns fresh tokens and user info in exchange of a refresh token.

!!! abstract "Parameters"
    * `refresh_token: string`: A valid refresh token.
    * `scope: string[] | undefined`: Optional list of scopes to ask for. If not provided, the access token will share the same list of scopes as requested the first time. Otherwise, it should be a subset of the original list of scopes.

!!! example
    ```ts
    const [tokens, userinfo] = await fief.authRefreshToken('REFRESH_TOKEN');
    ```

### `validateAccessToken`

Checks if an access token is valid and optionally that it has a required list of scopes.

!!! abstract "Parameters"
    * `accessToken: string`: The access token to validate.
    * `requireScopes: string[] | undefined`: Optional list of scopes to check for.

!!! example
    ```ts
    import { FiefAccessTokenExpired, FiefAccessTokenInvalid, FiefAccessTokenMissingScope} from '@fief/fief';

    try {
        accessTokenInfo = await fief.validateAccessToken('ACCESS_TOKEN', required_scope=['required_scope']);
        console.log(accessTokenInfo); // {"id": "USER_ID", "scope": ["openid", "required_scope"], "access_token": "ACCESS_TOKEN"}
    } catch (err) {
        if (err instanceof FiefAccessTokenInvalid) {
            console.error('Invalid access token');
        } else if (err instanceof FiefAccessTokenExpired) {
            console.error('Expired access token');
        } else if (err instanceof FiefAccessTokenMissingScope) {
            console.error('Missing required scope');
        }
    }
    ```

### `userinfo`

Returns fresh user information from the Fief API using a valid access token.

!!! abstract "Parameters"
    * `accessToken: string`: A valid access token

!!! example
    ```ts
    userinfo = await fief.userinfo('ACCESS_TOKEN');
    ```

### `getLogoutURL`

Returns a logout URL. If you redirect the user to this page, Fief will clear the session stored on its side.

**You're still responsible for clearing your own session mechanism if any.**

!!! abstract "Parameters"
    * `redirectURI: string`: A valid URL where the user will be redirected after the logout process.

!!! example
    ```ts
    const logoutURL = await fief.getLogoutURL({
        redirectURI: 'http://localhost:8000',
    });
    ```
