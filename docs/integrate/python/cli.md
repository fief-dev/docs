# CLI

Command Line Tools are really useful for tech users to easily interact with your product and integrate it in scripts or workflows.

The Fief Python client provides tools to help you integration Fief authentication in your CLI application. Let's see how to use them!

## Install the client

Install the Fief client with the optional CLI dependencies:

```bash
pip install "fief-client[cli]"
```

## Example

!!! question "This is for you if..."
    - [x] You want your CLI to make authenticated requests to your backend.

!!! abstract "Prerequisites"
    - [x] Make sure your Fief Client is [Public](../
    ../configure/clients.md#public-clients).
    - [x] Check that the following [Redirect URI](../../configure/clients.md#redirect-uris) is allowed on your Fief Client: `http://localhost:51562/callback`

For this example, we used [Click](https://click.palletsprojects.com/), a widely used library to build CLI tools in Python.

```py title="app.py"
--8<-- "examples/python/cli/app.py"
```

1. **Fief client instantiation**

    As we showed in the [standard Python section](./index.md), we instantiate here a Fief client here with the base tenant URL and client ID.

    Notice here that we **don't set the client secret**. Since the CLI app will be installed on the user's machine, it can't be considered as safe. That's why you have to use a [public client](../
    ../configure/clients.md#public-clients).

2. **Fief helper for CLI tools**

    This is the helper doing the tedious work for you. It first needs an instance of the Fief client we created above and **the path where the credentials will be saved** on the user's machine.

    We put here directly in the current working directory, but a proper way to manage this is probably to use the operating sytem directories dedicated for this kind of data. Libraries like [appdir](https://github.com/ActiveState/appdirs) can help you to determine a reasonable path depending on the user's operating system.

3. **Authenticate the user**

    The method [`authorize`](https://fief-dev.github.io/fief-python/fief_client/integrations/cli.html#FiefAuth.authorize) on the helper performs all the operations needed to authenticate your CLI application: it'll open the authorization page in the browser, catch the redirection, get tokens and save them on disk.

    Under the hood, it'll temporarily open a web server to catch the redirection. By default, it'll be opened on `localhost:51562`. You can customize this but don't forget then to update your client's [redirect URI](../../configure/clients.md#redirect-uris).

4. **Get info about the authenticated user**

    The method [`current_user`](https://fief-dev.github.io/fief-python/fief_client/integrations/cli.html#FiefAuth.current_user) returns you a [`FiefUserInfo`](https://fief-dev.github.io/fief-python/fief_client.html#FiefUserInfo) dictionary containing the data of the user.

5. **`FiefAuthNotAuthenticatedError` is raised if the CLI is not authenticated**

    If there is no credentials saved on disk, [`FiefAuthNotAuthenticatedError`](https://fief-dev.github.io/fief-python/fief_client/integrations/cli.html#FiefAuthNotAuthenticatedError) is raised. In this case, you can explain the problem to the user and ask them to authenticate.

6. **Get the access token**

    In general, you'll need an access token to make authenticated request to your server. The method `access_token_info` returns you a [`FiefAccessTokenInfo`](https://fief-dev.github.io/fief-python/fief_client.html#FiefAccessTokenInfo) dictionary, containing the access token.

    By default, if the access token is expired, it'll automatically ask for a fresh one using the refresh token and update it on disk.

That's it! The tedious work is mostly done by the helper. If you run the following command, you'll be taken through the authentication process:

<script id="asciicast-H6DJ45jEIMX9qOAR5Ez6liAUQ" src="https://asciinema.org/a/H6DJ45jEIMX9qOAR5Ez6liAUQ.js" async></script>

A browser window will automatically open to the Fief authentication page. After signing in, you can go back to the CLI: you're now authenticated!

<script id="asciicast-RMTdezrY61H8d1JKzcAASHVfW" src="https://asciinema.org/a/RMTdezrY61H8d1JKzcAASHVfW.js" async></script>
