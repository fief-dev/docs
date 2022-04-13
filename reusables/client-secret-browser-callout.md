!!! warning "Client secret is not safe in browser-based applications"
    If you build a browser-based application in JavaScript, the Client Secret is not safe: the end-user can easily find it in the source code.

    To circumvent this, Fief allows to **omit the client secret** for [clients with the public type](/getting-started/clients#client-type). However, a [PKCE code challenge](/going-further/pkce) will be required during the authorization flow.
