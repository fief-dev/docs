!!! tip "What is a user field?"
    Most of the time, you'll need to store data about your users, e.g., their first and last names, their birthdate, their newsletter preferences, etc. Your application will probably need to have quite a lot of data about them!

    To help you with this, Fief allows you to create custom **user fields**. Each one will have a name, an identifier and a type.

    Each user will have attached its values for those fields. They will be available directly through the [ID token](./oauth2.md#access-token-and-id-token) or through the `/userinfo` endpoint.
