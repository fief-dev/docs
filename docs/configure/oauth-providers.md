# OAuth Providers

This is where you'll see and manage the OAuth Providers of your workspace.

--8<-- "reusables/oauth-provider-callout.md"

![OAuth Providers from admin dashboard](/assets/images/admin-oauth-providers.png)

## Create a new OAuth Provider

You can create a new OAuth Provider by clicking the **Create OAuth Provider** button. A modal will open where you'll be able to input its different properties.

You can choose the **Provider** from the list of available providers, a custom name and [scopes](#scopes).

The most important part is the **Client ID** and **Client Secret**: it allows to uniquely identify *your* application on the OAuth Provider. That's why you need to "declare" it beforehand on their service. We provide [guidelines](#supported-oauth-providers) on how to create and configure a client on the OAuth Providers we support.

![Create OAuth Provider from admin dashboard](/assets/images/admin-oauth-providers-create.png)

!!! tip "Don't forget to enable it on your tenant"
    OAuth Providers are enabled per tenant, so you can finely customize which authentication methods can be used on each one. To do so, [edit your tenant](./tenants.md#edit-an-existing-tenant) and enable the OAuth Provider.

## Edit an existing OAuth Provider

If you click on one of the OAuth Provider in the list, you'll see its details on the right and be able to change its properties.

![Edit OAuth Provider from admin dashboard](/assets/images/admin-oauth-providers-edit.png)

## Delete an existing OAuth Provider

If one of your OAuth Provider is not useful anymore, you can delete it: click on the one you want to delete in the list and click on the **Delete** button.

![Delete OAuth Provider from admin dashboard](/assets/images/admin-oauth-providers-delete.png)

!!! danger "Associated OAuth accounts will be deleted as well"
    When you delete a provider, the **associated OAuth accounts** will be deleted as well. The associated users won't be deleted, but they will have to sign in with another method.

## Scopes

For each OAuth Providers you define, you'll be able to specify the list of **scopes** you want to ask when the user authenticates to the external service.

Those scopes tell the actions and data your application will be able to interact with on the external service API. For example, you might ask to get access to the Google Calendar of the user so your application can automatically add meetings to their agenda.

Each provider has its own list of scopes, corresponding to specific parts of the API.

!!! tip "Fief already asks for basic scopes"
    If you just want to authenticate users and nothing more, you can leave the scopes list empty. Fief takes care of asking for the scopes needed to authenticate the user and get their basic profile.

## Supported OAuth Providers

Currently, Fief supports the following OAuth Providers. You'll find below steps to configure your application integration on those platforms.

### Discord

* Go to: [https://discord.com/developers/applications](https://discord.com/developers/applications)
* Click on **New Application** and type the name of your application/website.
* Go to the **OAuth2** menu on the left.
* Copy the **Client ID** and paste it into Fief.
* Click on **Reset Secret** to generate a new client secret. Copy and paste it into Fief.
* Below, add your **Redirect URI**.

--8<-- "reusables/oauth-provider-redirect-uri-callout.md"

![Discord OAuth2 client configuration](/assets/images/oauth-providers-configuration-discord.png)

### Facebook

* Go to: [https://developers.facebook.com/apps/create/](https://developers.facebook.com/apps/create/)
* Select **Consumer** as app type.
* In **Display name**, type the name of your application/website.
* When the application is created, click on **Add product** in the left menu and in the **Facebook Login** box, click **Set up**.
* You don't need to go through the quickstart, just click on **Settings** in the left menu, right under **Facebook Login**.
* Add your **Redirect URI** in the field **Valid OAuth Redirect URIs**.
* You can find your **Client ID** and **Client Secret** (called App ID and App secret here) in the **Settings** ➡️ **Basic** menu. Copy and paste it into Fief.

--8<-- "reusables/oauth-provider-redirect-uri-callout.md"

![Facebook OAuth2 client configuration](/assets/images/oauth-providers-configuration-facebook-client.png)
![Facebook redirect URI OAuth2 client configuration](/assets/images/oauth-providers-configuration-facebook-redirect-uri.png)

!!! tip "Live mode"
    By default, Facebook apps are in development mode, so only you can use it. When you're ready to go in production, click on **Live** toggle on top. Facebook will require you to provide a link to a **Privacy Policy** and will manually review your app.

### GitHub

* Go to: [https://github.com/settings/apps/new](https://github.com/settings/apps/new)
* In **GitHub App name**, type the name of your application/website.
* In **Homepage URL**, type the URL of your application/website.
* In **Callback URL**, add your **Redirect URI**.
* Ensure **Expire user authorization tokens** and **Request user authorization (OAuth) during installation** are checked.
* By default **Webhook** is enabled. If use GitHub just for authenticating users, you can disable it.
* In the **User permissions** list, make sure **Email addresses** has **Read-only** access.
* Finally, at the bottom, select **Any account** to make your app available to any user.
* On the app settings, copy the **Client ID** and paste it into Fief.
* Click on **Generate a new client secret**. Copy and paste it into Fief.

--8<-- "reusables/oauth-provider-redirect-uri-callout.md"

![GitHub OAuth2 client configuration](/assets/images/oauth-providers-configuration-github.png)

### Google

* Go to: [https://console.cloud.google.com/apis/credentials/oauthclient](https://console.cloud.google.com/apis/credentials/oauthclient)
  * If it's the first time you go to the Google Cloud Console, you'll have to create a new project.
* If you never did it before, you'll be asked to configure your consent screen. Click on **Configure consent screen**.
  * Select **External** as **User Type**.
  * In **App name**, type the name of your application/website.
  * In **User support email**, type your support email address.
  * You can provide a logo and links to your legal terms.
  * In **Authorized domains**, add the top-level domain of Fief, **fief.dev**.
  * In **Developer contact information**, type your developer email address.
  * In **Scopes**, click on **Add or remove scopes** and select the three following scopes:
    * `/auth/userinfo.email`
    * `/auth/userinfo.profile`
    * `openid`
  * In **Test users**, you can add your own email address and the ones of your colleagues. While the app has not been approved, only those emails will be allowed to use it.
* Once done, you can go back to [https://console.cloud.google.com/apis/credentials/oauthclient](https://console.cloud.google.com/apis/credentials/oauthclient).
   * Choose **Web application** as **Application type**.
   * In **Name**, type a name to recognize this client. For example, **Fief Client**.
   * In **Authorized redirect URIs**, add your **Redirect URI**.
   * Your **Client ID** and **Client Secret** will then appear in a modal. Copy and paste them into Fief.
* If not already, you should enable the **People API** in your Google Cloud project. Go to [https://console.developers.google.com/apis/api/people.googleapis.com/overview](https://console.developers.google.com/apis/api/people.googleapis.com/overview) and click on **Enable**.

--8<-- "reusables/oauth-provider-redirect-uri-callout.md"

![Google OAuth2 client configuration](/assets/images/oauth-providers-configuration-google-client.png)
![Google redirect URI OAuth2 client configuration](/assets/images/oauth-providers-configuration-google-redirect-uri.png)
![Google enable People API](/assets/images/oauth-providers-configuration-google-people-api.png)

!!! tip "Production mode"
    By default, your consent screen is in **testing mode**, so only the test users can use it. When you're ready to go in production, click on the **Publish app** button. Google will require you to provide some explanations about what you're doing with the app and manually review it. They are *picky*, so make sure to add lot of details and videos of how your app works.

### LinkedIn

* Go to: [https://www.linkedin.com/developers/apps/new](https://www.linkedin.com/developers/apps/new)
* In **App name**, type the name of your application/website.
* You need to have a LinkedIn company page associated. If you don't have one, create one before.
* In **App logo**, add your application/website logo.
* In the **Auth** tab, you can find your **Client ID** and **Client Secret**. Copy and paste them into Fief.
* Below, in **Authorized redirect URLs for your app**, add your **Redirect URI**.

--8<-- "reusables/oauth-provider-redirect-uri-callout.md"

![LinkedIn OAuth2 client configuration](/assets/images/oauth-providers-configuration-linkedin.png)

### Microsoft

* Go to: [https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/true](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/true)
    * If you don't have an Azure account, you'll be asked to create one.
* In **Name**, type the name of your application/website.
* In **Supported account types**, select **Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**. This will allow any kind of Microsoft users to authenticate.
* In **Redirect URI**, add your **Redirect URI** with the type **Web**.
* You can find your **Client ID** (called Application ID here) in the **Overview**. Copy and paste them into Fief.
* Click on **Certificates & secrets** on the left menu. In the **Client secrets** tab, click on **New client secret**.
* In **Description**, type a name to recognize this secret. For example, **Fief client**.
* In **Expires**, choose the lifetime duration of this secret. You can choose **24 months**.
* Copy the **Value** of the client secret. Paste it into Fief.

--8<-- "reusables/oauth-provider-redirect-uri-callout.md"

![Microsoft OAuth2 redirect URI client configuration](/assets/images/oauth-providers-configuration-microsoft-redirect-uri.png)
![Microsoft OAuth2 client ID](/assets/images/oauth-providers-configuration-microsoft-client-id.png)
![Microsoft OAuth2 client secret](/assets/images/oauth-providers-configuration-microsoft-client-secret.png)

!!! warning "Client Secret expires"

    The Client Secret expires after the duration you set when creating it. When it happens, remember to generate a new one and update it in Fief; otherwise, users won't be able to authenticate with their Microsoft account.

### Reddit

* Go to: [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
    * The page is bugged and ugly but don't worry, it's normal 😅
* Click on the button **are you a developer? create an app...**
* In **name**, type the name of your application/website.
* Select **web app** as type.
* In **redirect uri**, add your **Redirect URI**.
* Your **Client ID** is right under the name of the application. Copy and paste it into Fief.
* The field named **secret** is your **Client Secret**. Copy and paste it into Fief.

--8<-- "reusables/oauth-provider-redirect-uri-callout.md"

![Reddit redirect URI OAuth2 client configuration](/assets/images/oauth-providers-configuration-reddit-redirect-uri.png)
![Reddit OAuth2 client configuration](/assets/images/oauth-providers-configuration-reddit-client.png)

### Generic OpenID

Fief is compatible with any [OpenID Connect](https://openid.net/connect/) compliant identity providers. All you need to give is:

* The OpenID configuration endpoint. Usually, the path looks like this: **https://auth.provider.com/.well-known/openid-configuration**.
* The **Client ID** and **Client Secret**.

On the OpenID provider side, don't forget to add your **Redirect URI**.

--8<-- "reusables/oauth-provider-redirect-uri-callout.md"
