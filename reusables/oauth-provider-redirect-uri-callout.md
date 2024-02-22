!!! info "What is my Redirect URI?"
    For security purposes, OAuth2 protocol requires the redirect URI to be declared upfront. Since Fief will handle OAuth2 authentication for you, the redirect URI will target the Fief server.

    If your **instance** URL is **https://fief.mydomain.com**, your redirect URI will be:

    ```
    https://fief.mydomain.com/oauth/callback
    ```

    This URL is common for **every [tenants](/configure/tenants)**. So you don't have to worry about it if you add new tenants, Fief will handle it automatically.
