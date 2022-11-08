---
description: List of environment variables available and how to set them.
---

# Environment variables

Fief server relies heavily on environment variables for configuration. You'll likely need to adjust those settings for your deployment.

## Set environment variables

### Using Docker

When running Fief server with Docker, the most straightforward way is to use the `-e` option on the command line, as shown in the [Quickstart](quickstart.md) section.

```bash
docker run \
  --name fief-server \
  -p 8000:8000 \
  -d \
  -e "SECRET=XXX" \
  -e "FIEF_CLIENT_ID=XXX" \
  -e "FIEF_CLIENT_SECRET=XXX" \
  -e "ENCRYPTION_KEY=XXX" \
  -e "PORT=8000" \
  -e "ROOT_DOMAIN=localhost:8000" \
  -e "FIEF_DOMAIN=localhost:8000" \
  -e "CSRF_COOKIE_SECURE=False" \
  -e "LOGIN_SESSION_COOKIE_SECURE=False" \
  -e "SESSION_COOKIE_SECURE=False" \
  -e "FIEF_ADMIN_SESSION_COOKIE_SECURE=False" \
  ghcr.io/fief-dev/fief:latest
```

However, it may become hard to maintain when having lot of variables to set. An alternative way is to use a `.env` file. It's a simple file where each line consists of a key and a value separated by an equal sign:

```ini title=".env"
SECRET=XXX
FIEF_CLIENT_ID=XXX
FIEF_CLIENT_SECRET=XXX
ENCRYPTION_KEY=XXX
PORT=8000
ROOT_DOMAIN=localhost:8000
FIEF_DOMAIN=localhost:8000
CSRF_COOKIE_SECURE=False
LOGIN_SESSION_COOKIE_SECURE=False
SESSION_COOKIE_SECURE=False
FIEF_ADMIN_SESSION_COOKIE_SECURE=False
```

Then, you can reference this file in the Docker command:

```bash
docker run \
  --name fief-server \
  -p 8000:8000 \
  -d \
  --env-file .env \
  ghcr.io/fief-dev/fief:latest
```

### Other methods of deployment

Depending on your method of deployment, the way of setting environment variables will be different. We show you several ways of deploying Fief in production in the previous section.

## Reference

For each variable, we'll try to provide a sensible example value to help you configure it correctly. Throughout the examples, we'll assume that you host your Fief server on the sub-domain `fief.bretagne.duchy`.

### General

| Name                  | Description                                                                                                                                             | Default                     | Allowed values                   | Example                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------------------------- | ---------------------------- |
| `ENVIRONMENT`         | Name of the deployment environment                                                                                                                      | development                 | development, staging, production | production                   |
| `LOG_LEVEL`           | Log verbosity                                                                                                                                           | INFO                        | DEBUG, INFO, WARNING, ERROR      | INFO                         |
| `ROOT_DOMAIN`         | Root domain where your server will be running. Mainly used for generating workspace subdomains.                                                         | localhost:8000              |                                  | bretagne.duchy               |
| `ALLOW_ORIGIN_REGEX`  | Regex used to control CORS access to your API                                                                                                           | http://.\*localhost:\[0-9]+ |                                  | https://.\*\\.bretagne.duchy |
| `PORT`                | Internal port on which the Fief server is exposed                                                                                                       | 8000                        |                                  | 8000                         |
| `FORWARDED_ALLOW_IPS` | Comma separated list of IPs to trust with proxy headers. If you serve Fief behind a proxy handling SSL, you'll likely need to set this to value to `*`. | 127.0.0.1                   |                                  |                              |

### Secrets

| Name                 | Description                                                                     | Default | Allowed values                      | Example |
| -------------------- | ------------------------------------------------------------------------------- | ------- | ----------------------------------- | ------- |
| `SECRET`             | Secret value used to sign reset password tokens.                                |         | Any sufficiently long string        |         |
| `ENCRYPTION_KEY`     | Key used to encrypt the external databases credentials inside the main database |         | A valid Fernet key encoded in UTF-8 |         |
| `GENERATED_JWK_SIZE` | Size in bits of the generated RSA key pair used to sign JWT.                    |         | 4096                                |         |

--8<-- "reusables/fernet-key-generator.md"

### Database

| Name                            | Description                                                                                                                                                                                                                                 | Default                   | Allowed values            | Example      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------------- | ------------ |
| `DATABASE_TYPE`                 | Type of the main database                                                                                                                                                                                                                   | SQLITE                    | POSTGRESQL, MYSQL, SQLITE | POSTGRESQL   |
| `DATABASE_HOST`                 | Host of the main database                                                                                                                                                                                                                   |                           |                           | localhost    |
| `DATABASE_PORT`                 | Listening port of the main database                                                                                                                                                                                                         |                           |                           | 5432         |
| `DATABASE_USERNAME`             | Main database user                                                                                                                                                                                                                          |                           |                           | fief         |
| `DATABASE_PASSWORD`             | Main database user's password                                                                                                                                                                                                               |                           |                           | fiefpassword |
| `DATABASE_NAME`                 | Main database name                                                                                                                                                                                                                          | fief.db                   |                           | fief         |
| `DATABASE_SSL_MODE`             | Main database SSL mode                                                                                                                                                                                                                      |                           | Varies by database type   | require      |
| `DATABASE_LOCATION`             | For SQLite databases, path where to store the database files                                                                                                                                                                                | Current working directory |                           |              |
| `DATABASE_POOL_RECYCLE_SECONDS` | Maximum lifetime in seconds of a database connection in the connection pool. Useful for servers cutting idle connections after some time. [Read more](https://docs.sqlalchemy.org/en/14/core/pooling.html#disconnect-handling-pessimistic). | 600 *(10 minutes)*        |                           |              |
| `DATABASE_POOL_PRE_PING`        | Whether to always issue a query before returning a database connection to make sure it's alive. [Read more](https://docs.sqlalchemy.org/en/14/core/pooling.html#disconnect-handling-pessimistic).                                           | False                     |                           |              |
| `DATABASE_URL`                  | Full database connection string, useful for some cloud providers. It'll take precedence over the single parameters above.                                                                                                                   |                           |                           |              |

More details about how to setup a database in the dedicated section.

[Setup database](./deployment/setup-database.md){ .md-button }
{: .buttons }

### Redis

We use a Redis instance to manage background jobs (send emails, heavy computations...). A Redis instance is already up-and-running in the official Docker image, but you can provide your own one if needed.

| Name        | Description           | Default                | Allowed values | Example |
| ----------- | --------------------- | ---------------------- | -------------- | ------- |
| `REDIS_URL` | URL of a Redis server | redis://localhost:6379 |                |         |

### Email provider

| Name                    | Description                                    | Default | Allowed values                 | Example                      |
| ----------------------- | ---------------------------------------------- | ------- | ------------------------------ | ---------------------------- |
| `EMAIL_PROVIDER`        | Type of email provider                         | NULL    | NULL, SMTP, POSTMARK, SENDGRID | POSTMARK                     |
| `EMAIL_PROVIDER_PARAMS` | Configuration dictionary of the email provider | {}      |                                | {"server\_token": "XXX-XXX"} |

More details about how to setup an email provider in the dedicated section.

[Setup email provider](./deployment/setup-email-provider.md){ .md-button }
{: .buttons }

### CSRF cookie

To protect against [Cross-Site-Request-Forgery](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html) attacks on authentication pages, we use the [double-submit cookie](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html#double-submit-cookie) pattern.

| Name                 | Description                                                                       | Default         | Allowed values | Example |
| -------------------- | --------------------------------------------------------------------------------- | --------------- | -------------- | ------- |
| `CSRF_CHECK_ENABLED` | Whether to enable the CSRF protection. In most cases, this should remain enabled. | True            |                |         |
| `CSRF_COOKIE_NAME`   | Name of the CSRF token cookie                                                     | fief\_csrftoken |                |         |
| `CSRF_COOKIE_SECURE` | Secure flag of the login session cookie                                           | True            |                |         |

--8<-- "reusables/cookie-secure-callout.md"

### Login session

A login session is a cookie used to maintain the state of the login flow of a user, from the login page until they're redirected to your application.

| Name                             | Description                                     | Default              | Allowed values | Example |
| -------------------------------- | ----------------------------------------------- | -------------------- | -------------- | ------- |
| `LOGIN_SESSION_COOKIE_NAME`      | Name of the login session cookie                | fief\_login\_session |                |         |
| `LOGIN_SESSION_COOKIE_DOMAIN`    | Domain of the login session cookie              | _Empty string_       |                |         |
| `LOGIN_SESSION_COOKIE_SECURE`    | Secure flag of the login session cookie         | True                 |                |         |
| `LOGIN_SESSION_LIFETIME_SECONDS` | Lifetime of the login session cookie in seconds | 600 _(10 minutes)_   |                |         |

--8<-- "reusables/cookie-secure-callout.md"

### Registration session

A registration session is a cookie used to maintain the state of the registration flow of a new user, from the registration page until their account is created.

| Name                                    | Description                                            | Default                     | Allowed values | Example |
| --------------------------------------- | ------------------------------------------------------ | --------------------------- | -------------- | ------- |
| `REGISTRATION_SESSION_COOKIE_NAME`      | Name of the registration session cookie                | fief\_registration\_session |                |         |
| `REGISTRATION_SESSION_COOKIE_DOMAIN`    | Domain of the registration session cookie              | _Empty string_              |                |         |
| `REGISTRATION_SESSION_COOKIE_SECURE`    | Secure flag of the registration session cookie         | True                        |                |         |
| `REGISTRATION_SESSION_LIFETIME_SECONDS` | Lifetime of the registration session cookie in seconds | 600 _(10 minutes)_          |                |         |

--8<-- "reusables/cookie-secure-callout.md"

### OAuth session

An OAuth session is used to maintain the state of an OAuth authentication with an [OAuth Provider](../admin-dashboard/oauth-providers.md), from the moment they click on the *Sign in with...* button until they're redirected.

| Name                             | Description                              | Default            | Allowed values | Example |
| -------------------------------- | ---------------------------------------- | ------------------ | -------------- | ------- |
| `OAUTH_SESSION_LIFETIME_SECONDS` | Lifetime of the OAuth session in seconds | 600 _(10 minutes)_ |                |         |

### Session

A session is a cookie used to maintain the session of a user **on the Fief authentication pages**. It's different from the session you'll maintain in your own application.

Its purpose is to allow a user to re-authenticate quickly to your app without having them to input their credentials again.

| Name                       | Description                               | Default                 | Allowed values | Example |
| -------------------------- | ----------------------------------------- | ----------------------- | -------------- | ------- |
| `SESSION_COOKIE_NAME`      | Name of the session cookie                | fief\_session           |                |         |
| `SESSION_COOKIE_DOMAIN`    | Domain of the session cookie              | _Empty string_          |                |         |
| `SESSION_COOKIE_SECURE`    | Secure flag of the session cookie         | True                    |                |         |
| `SESSION_LIFETIME_SECONDS` | Lifetime of the session cookie in seconds | 86400 \* 30 _(30 days)_ |                |         |

--8<-- "reusables/cookie-secure-callout.md"

### Authorization codes and tokens

Authorization codes are temporary codes generated during the [OAuth2 authentication flow](../getting-started/oauth2.md).

Access tokens, ID tokens and refresh tokens are generated after a successful [OAuth2 authentication flow](../getting-started/oauth2.md#access-token-and-id-token).

| Name                                  | Description                                                                                                                                                                                                              | Default             | Allowed values | Example |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | -------------- | ------- |
| `AUTHORIZATION_CODE_LIFETIME_SECONDS` | Lifetime of the authorization code in seconds. For security reasons, this value should remain low. OAuth2 specification [recommends a value of 10 minutes](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2). | 600 _(10 minutes)_  |                |         |
| `ACCESS_ID_TOKEN_LIFETIME_SECONDS`    | Lifetime of the access token and ID token in seconds.                                                                                                                                                                    | 3600 _(1 hour)_     |                |         |
| `REFRESH_TOKEN_LIFETIME_SECONDS`      | Lifetime of the refresh token in seconds.                                                                                                                                                                                | 2592000 _(30 days)_ |                |         |

### Fief-ception

Fief-ception is a mind-fucking concept describing the fact that we actually use Fief to authenticate Fief users to the app 🤯

That's why we set necessary variables to create the main workspace and first admin user, as described in the [Quickstart](quickstart.md) section.

The variables below are here to configure the Fief server with a proper Fief client, as you would do in your own application!

| Name                      | Description                                                                                                                                                                                                           | Default        | Allowed values | Example                      |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------- | ---------------------------- |
| `FIEF_DOMAIN`             | Domain of your main Fief workspace                                                                                                                                                                                    | localhost:8000 |                | fief.bretagne.duchy          |
| `FIEF_CLIENT_ID`          | Client ID in your main Fief workspace                                                                                                                                                                                 |                |                |                              |
| `FIEF_CLIENT_SECRET`      | Client secret in your main Fief workspace                                                                                                                                                                             |                |                |                              |
| `FIEF_ENCRYPTION_KEY`     | Optional RSA key used to encrypt the JWT tokens                                                                                                                                                                       |                |                |                              |
| `FIEF_MAIN_USER_EMAIL`    | Email address of the first admin user in your main workspace. If provided, the user will be created automatically on startup.                                                                                         |                |                | anne@bretagne.duchy          |
| `FIEF_MAIN_USER_PASSWORD` | Password of the first admin user in your main workspace. If `FIEF_MAIN_USER_EMAIL` is provided, the user will be created automatically on startup with this password. Otherwise, a random password will be generated. |                |                | SuperSecretAndStrongPassword |

### Admin session

An admin session is a cookie used to maintain the session of a user on the Fief admin dashboard.

| Name                               | Description                             | Default              | Allowed values | Example |
| ---------------------------------- | --------------------------------------- | -------------------- | -------------- | ------- |
| `FIEF_ADMIN_SESSION_COOKIE_NAME`   | Name of the admin session cookie        | fief\_admin\_session |                |         |
| `FIEF_ADMIN_SESSION_COOKIE_DOMAIN` | Domain of the admin session cookie      | _Empty string_       |                |         |
| `FIEF_ADMIN_SESSION_COOKIE_SECURE` | Secure flag of the admin session cookie | True                 |                |         |

--8<-- "reusables/cookie-secure-callout.md"
