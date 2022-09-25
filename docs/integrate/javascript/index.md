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
