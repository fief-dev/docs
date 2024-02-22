# Admin API

Fief exposes a REST API allowing you to **manage almost everything in your instance** programmatically.

!!! bug "Clients not available"
    For the time being, we do not provide any official client for this API. However, it's quite simple so it should fairly easy to integrate with your favorite HTTP client.

## Base URL

The Admin API lives under the `/admin/api` path of your instance:

```
https://fief.mydomain.com/admin/api
```

## Authentication

To authenticate your API requests, you'll need to generate an [API Key](../configure/api-keys.md).

Then, you need to pass it as a `Bearer` credential in the `Authorization` header.

**Example**

```bash
curl \
-X GET \
-H "Authorization: Bearer ${FIEF_API_KEY}" \
https://fief.mydomain.com/admin/api/users/
```

## OpenAPI & Swagger

The Admin API is documented with OpenAPI and usable interactively with Swagger. It lives under the `/admin/api/docs` path of your instance:

```
https://fief.mydomain.com/admin/api/docs
```
