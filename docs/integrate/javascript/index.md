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

## Reference

### `Fief` client

!!! abstract "Constructor"
    * `baseURL: string`: Base URL of your Fief tenant.
    * `clientID: string`: ID of your Fief client.
    * `clientSecret: string | undefined`: Secret of your Fief client. **It's not recommended to use it in the context of a browser app, since it can be easily found by the end-user in the source code. The recommended way is to use a [Public client](../../getting-started/clients.md#public-clients).**
    * `encryptionKey: string | undefined`: Encryption key of your Fief client. Necessary only if [ID Token encryption](../../going-further/id-token-encryption.md) is enabled.

#### `getAuthURL`

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

#### `authCallback`

Returns a [`FiefTokenResponse`](#fieftokenresponse) and [`FiefUserInfo`](#fiefuserinfo) in exchange of an authorization code.

!!! abstract "Parameters"
    * `code: string`: The authorization code.
    * `redirectURI: string`: The exact same `redirectURI` you passed to the authorization URL.
    * `codeVerifier: string | undefined`: The raw [PCKE](../../going-further/pkce.md) code used to generate the code challenge during authorization.

!!! example
    ```ts
    const [tokens, userinfo] = await fief.authCallback('CODE', 'http://localhost:8000/callback');
    ```

#### `authRefreshToken`

Returns fresh [`FiefTokenResponse`](#fieftokenresponse) and [`FiefUserInfo`](#fiefuserinfo) in exchange of a refresh token.

!!! abstract "Parameters"
    * `refresh_token: string`: A valid refresh token.
    * `scope: string[] | undefined`: Optional list of scopes to ask for. If not provided, the access token will share the same list of scopes as requested the first time. Otherwise, it should be a subset of the original list of scopes.

!!! example
    ```ts
    const [tokens, userinfo] = await fief.authRefreshToken('REFRESH_TOKEN');
    ```

#### `validateAccessToken`

Checks if an access token is valid and optionally that it has a required list of scopes, or a required list of [permissions](../../getting-started/access-control.md). Returns a [`FiefAccessTokenInfo`](#fiefaccesstokeninfo).

!!! abstract "Parameters"
    * `accessToken: string`: The access token to validate.
    * `requiredScopes: string[] | undefined`: Optional list of scopes to check for.
    * `requiredPermissions: string[] | undefined`: Optional list of permissions to check for.

!!! example "Example: Validate access token with required scopes"
    ```ts
    import { FiefAccessTokenExpired, FiefAccessTokenInvalid, FiefAccessTokenMissingScope} from '@fief/fief';

    try {
        accessTokenInfo = await fief.validateAccessToken('ACCESS_TOKEN', ['required_scope']);
        console.log(accessTokenInfo);
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

!!! example "Example: Validate access token with required scopes"
    ```ts
    import { FiefAccessTokenExpired, FiefAccessTokenInvalid, FiefAccessTokenMissingPermission} from '@fief/fief';

    try {
        accessTokenInfo = await fief.validateAccessToken('ACCESS_TOKEN', undefined, ['castles:create', 'castles:read']);
        console.log(accessTokenInfo);
    } catch (err) {
        if (err instanceof FiefAccessTokenInvalid) {
            console.error('Invalid access token');
        } else if (err instanceof FiefAccessTokenExpired) {
            console.error('Expired access token');
        } else if (err instanceof FiefAccessTokenMissingPermission) {
            console.error('Missing required permission');
        }
    }
    ```

#### `userinfo`

Returns fresh [`FiefUserInfo`](#fiefuserinfo) from the Fief API using a valid access token.

!!! abstract "Parameters"
    * `accessToken: string`: A valid access token

!!! example
    ```ts
    userinfo = await fief.userinfo('ACCESS_TOKEN');
    ```


#### `updateProfile`

Updates user information with the Fief API using a valid access token.

!!! abstract "Parameters"
    * `accessToken: string`: A valid access token
    * `data: Record<string, any>`: An object containing the data to update

!!! example "Update email address"
    ```ts
    userinfo = await fief.updateProfile('ACCESS_TOKEN', { email: 'anne@nantes.city' })
    ```

!!! example "Update password"
    ```ts
    userinfo = await fief.updateProfile('ACCESS_TOKEN', { password: 'hermine1' })
    ```

!!! example "Update user field"
    To update [user field](../../getting-started/user-fields.md) values, you need to nest them into a `fields` object, indexed by their slug.

    ```ts
    userinfo = await fief.update_profile('ACCESS_TOKEN', { fields: { first_name: 'Anne' } })
    ```

#### `getLogoutURL`

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

### `FiefTokenResponse`

Object containing the tokens and related information returned by Fief after a successful authentication.

!!! abstract "Structure"
    * `access_token: string`: Access token you can use to call the Fief API
    * `id_token: string`: ID token containing user information
    * `token_type: string`: Type of token, usually `bearer`
    * `expires_int: number`: Number of seconds after which the tokens will expire
    * `refresh_token: string | undefined`: Token provided only if scope `offline_access` was granted. Allows you to retrieve fresh tokens using the [`authRefreshToken`](#authrefreshtoken) method.


### `FiefAccessTokenInfo`

Object containing information about the access token.

!!! abstract "Structure"
    * `id: string`: ID of the user
    * `scope: string[]`: Array of granted scopes for this access token
    * `permissions: string[]`: List of [granted permissions](../../getting-started/access-control.md) for this user
    * `access_token: string`: Access token you can use to call the Fief API


!!! example
    ```js
    {
        id: 'aeeb8bfa-e8f4-4724-9427-c3d5af66190e',
        scope: ['openid', 'required_scope'],
        permissions: ['castles:read', 'castles:create', 'castles:update', 'castles:delete'],
        access_token: 'ACCESS_TOKEN',
    }
    ```

### `FiefUserInfo`

Object containing user information.

!!! abstract "Structure"
    * `sub: string`: ID of the user
    * `email: string`: Email address of the user
    * `tenant_id: string`: ID of the [tenant](../../getting-started/tenants.md) associated to the user
    * Available [user fields](../../getting-started/user-fields.md) values for this user, indexed by their slug.

!!! example
    ```js
    {
        sub: 'aeeb8bfa-e8f4-4724-9427-c3d5af66190e',
        email: 'anne@bretagne.duchy',
        tenant_id: 'c91ecb7f-359c-4244-8385-51ecd6c0d06b',
        first_name: 'Anne',
        last_name: 'De Bretagne',
    }
    ```
