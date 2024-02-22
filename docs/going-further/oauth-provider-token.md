# OAuth Provider token

When configuring an [OAuth Provider](../configure/oauth-providers.md) for your app, you allow users to authenticate using their existing account on this particular service.

But there is more: when you do this, and if you asked for the right [scopes](../configure/oauth-providers.md#scopes), you gain access to the API of this provider, so you can make actions **on behalf of the user**. For example, you could build a search engine indexing files from their Google Drive or an application to help manage GitHub issues.

When a user authenticates using their external account, Fief automatically retrieves a valid **access token** that can be used to query the API of the external service.

## Getting a fresh access token

To help you integrate clever workflows into your application, Fief Admin API allows you to retrieve an access token for a given user and OAuth Provider. All you need is an [Admin API key](../configure/api-keys.md), the ID of the OAuth Provider (the one in Fief, not the Client ID) and the ID of the user. Then, you just have to make an HTTP request like this:

```bash
curl \
-X GET \
-H 'Authorization: Bearer FIEF_ADMIN_API_KEY' \
'https://fief.mydomain.com/admin/api/oauth-providers/OAUTH_PROVIDER_ID/access-token/USER_ID'
```

You'll then get a JSON response including a valid access token ready for you to use in the external API:

```json
{
  "id": "8c735912-c5d6-4722-852e-f817a0d81282",
  "account_id": "people/100817388859897448986",
  "access_token": "ACCESS_TOKEN",
  "expires_at": "2022-09-08T13:37:00.000Z"
}
```

Fief takes care of **refreshing** the access token if it expires. If the OAuth Provider supports it, and if you asked for the adequate scope, Fief also stores a refresh token allowing to generate fresh access tokens. This operation is done automatically when calling the endpoint above.
