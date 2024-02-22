!!! tip "What is a client?"
    A client is a central part of the OAuth2 protocol. It's the **definition of an application authorized to request for access tokens and user information** on Fief. In other words, your application will need one of those client to be able to authenticate users from your Fief instance.

    Each client has a Client ID and a Client Secret. Those values are used during OAuth2 authentification to recognize the client.

    Each instance comes with one client, tied to the default [tenant](/configure/tenants).
