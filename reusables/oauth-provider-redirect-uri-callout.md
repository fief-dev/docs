!!! info "What is my Redirect URI?"
    For security purposes, OAuth2 protocol requires the redirect URI to be declared upfront. Since Fief will handle OAuth2 authentication for you, the redirect URI will target the Fief server.

    If your **workspace** URL is **https://example.fief.dev**, your redirect URI will be:

    ```
    https://example.fief.dev/oauth/callback
    ```

    This URL is common for **every [tenants](./tenants.md)**. So you don't have to worry about it if you add new tenants, Fief will handle it automatically.
