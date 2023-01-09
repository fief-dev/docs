# Try OAuth2 on your workspace

The following exercise is very interesting to see and practice all the aspects of OAuth2 with Fief.

First of all, go to your workspace admin dashboard.

![Admin dashboard](/assets/images/admin-dashboard.png)

## 1. Add a Redirect URI to a Client

On the left menu, click on **Clients**. You'll see here the list of OAuth2 clients defined on your workspace. When getting started, you will have one default client created for you.

--8<-- "reusables/client-callout.md"

![Clients from admin dashboard](/assets/images/admin-clients.png)

**Click on your default client** in the list. You'll see its details on the right. Click on the **Edit Client** button. A modal will open where you'll be able to change some of the properties of this client.

In the **Redirect URIs** part, click on **Add** and add the following URL, using your subdomain:

```
https://MY_WORKSPACE_SUBDOMAIN.fief.dev/docs/oauth2-redirect
```

!!! warning "Don't forget to adapt with your own workspace subdomain"
    If your workspace subdomain is `mysuperapp.fief.dev`, then the Redirect URL will be `https://mysuperapp.fief.dev/docs/oauth2-redirect`.

Click on **Update** to submit your changes.

!!! tip "Keep this tab open"
    You can keep this tab open in your browser, we'll need it right after.

## 2. Open the interactive documentation

Fief comes with an interactive documentation allowing you to easily test its API. Open it in a new window: [https://MY_WORKSPACE_SUBDOMAIN.fief.dev/docs](https://MY_WORKSPACE_SUBDOMAIN.fief.dev/docs)

!!! warning "Don't forget to adapt with your own workspace subdomain"
    If your workspace subdomain is `mysuperapp.fief.dev`, then the Redirect URL will be `https://mysuperapp.fief.dev/docs`.

![Interactive API documentation](/assets/images/try-oauth2-docs.png)

You see there the list of available API endpoints. We'll be able to call them when we'll be properly authenticated.

## 3. Authenticate in the interactive documentation

Click on the **Authorize** button. A modal will open showing you the available methods for authenticating. The one we're interested in is at the bottom of this window and called **OAuth2AuthorizationCodeBearer**.

![Interactive API documentation authorize windows](/assets/images/try-oauth2-docs-authorize.png)

You see a form expecting two things: the **Client ID** and **Client Secret**. Get back to the admin dashboard window and copy and paste them from the client information.

![Copy Client ID and Secret from admin dashboard](/assets/images/try-oauth2-copy-client-id-secret.png)

Don't forget also to **check the `openid` checkbox** (that's the scope we ask for!). Finally, click on the **Authorize** button. You'll be taken to a Fief login page!

![Fief login](/assets/images/try-oauth2-login.png)

Just go through the authentication process. If your workspace is brand new, you'll need to **create a new account**. If everything goes well, you'll be taken back to the interactive documentation. The authorize window now shows you that you are correctly authenticated: we successfully got an **access token** 🎉

![Interactive API documentation authenticated](/assets/images/try-oauth2-docs-authenticated.png)

## 4. Call an API

We can now call one of the API! In particular, we'll try the `/api/userinfo` endpoint: it'll show the information about the current user (you!). Open the one called `GET /api/userinfo`, click on the **Try it out** button and then **Execute**. You'll see an API response showing the information about your user object:

![Interactive API documentation API response](/assets/images/try-oauth2-docs-api-response.png)

Notice how the interactive documentation automatically added the `Authorization` header with the token!

## 5. See your new user in the admin dashboard

Now that you have a user account in your workspace, you can see it from the admin dashboard! Get back to your admin dashboard and, in the left menu, click on **Users**. This is the list of users in your workspace... And you should see the one you just created!

![Users from admin dashboard](/assets/images/admin-users.png)

## You're now an OAuth2 master 👏

Congratulations! You've performed a full OAuth2 authentication from A to Z. Those concepts are important to have in mind because they'll be at the core of Fief integration in your app. The key things to remember are:

* You need a **Client** to make authentication requests, using its **ID** and **Secret**.
* You need to allow the Redirect URL on the **Client** so Fief can redirect to your application.
* You need to request an access token and store it somewhere to authenticate requests.

## What now?

You can now proceed to integrate Fief in your application! We provide libraries and guides for the following languages:

[Python](../integrate/python/index.md){ .md-button }
[JavaScript](../integrate/javascript/index.md){ .md-button }
{: .buttons }

Also, be sure to get familiar with **all the features of Fief** by going through the [admin dashboard documentation](../configure/index.md).
