# Clients

This is where you'll see and manage the clients of your workspace.

--8<-- "reusables/client-callout.md"

![Clients from admin dashboard](/assets/images/admin-clients.png)

## View client details

If you click on one of the client in the list, you'll see its details on the right. Especially, you'll be able to copy its ID and Secret by using the clipboard buttons.

![Client details from admin dashboard](/assets/images/admin-clients-detail.png)

## Create a new client

You can create a new client by clicking the **Create Client** button. A modal will open where you'll be able to input its name, if it's a first-party, its redirect URIs and its associated tenant.

![Create client from admin dashboard](/assets/images/admin-clients-create.png)

!!! tip "When should I create a new client?"
    If you have several applications authenticating to your Fief workspace, you should consider creating new clients. Typically, if you have both a web and a mobile application, it's usually a good idea to have a client for each one.

    This way, it's easier to track down where the tokens come from and mitigates the risk of compromising data if one of the application has a security breach.

## Edit an existing client

You can edit an existing client by opening its details and click on the **Edit Client** button. A modal will open where you'll be able to change its name, if it's a first-party and its redirect URIs

![Edit client from admin dashboard](/assets/images/admin-clients-edit.png)

## First-party clients

You probably noticed that your first client has a **first-party** badge. It means that this client is intended to be used by your own, official application.

In this context, when users log in to your application, the traditional **OAuth2 consent screen is bypassed**. Since you are the developer of the application, it makes sense to not ask the user for their consent to use their data on the same application!

For third-party applications, like developers from another company who want to integrate your API in their product, you'll provide them a client without this first-party flag. In this context, we want the user consent to be explicit.

## Redirect URIs

During an [OAuth2 authentication flow](./oauth2.md), after the user has successfully logged in, Fief will redirect them to your application with a temporary code. At that point, your application will use this temporary code to obtain a valid token.

For security reasons, Fief **won't allow the user to be redirected to any URI**. Instead, you have to explicitly allow every URI you'll need in your applications.

For HTTP URIs, they need to use the `https` scheme; `http` URL are not allowed. The only exception to this rule is `localhost`, which can be in `http` for local development purposes.
