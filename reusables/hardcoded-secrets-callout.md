!!! warning "Avoid to hardcode your secrets in your code"
    It's usually not recommended to hardcode secrets like Client ID and Secret in your code like this. If your code gets published on the web, for example on GitHub, the security of your instance would be compromised.

    Besides, it'll be harder if you need to deploy on several environments, like a staging or testing one, in addition to your production environment.

    A standard and widely-used approach is to use [environment variables](https://12factor.net/config).
