---
description: >-
  Instructions to configure an email provider to let Fief send transactional
  emails.
---

# Setup email provider

As you surely now, users management imply a lot of transactional emails, like welcome emails or reset password emails. To be able to send them, Fief needs an email provider.

Currently, Fief only supports [Postmark](https://postmarkapp.com), one of the leading email delivery service on the market, but we may support more in the future.

There are two environment variables to configure the email provider: `EMAIL_PROVIDER`, to set the type of provider and `EMAIL_PROVIDER_PARAMS`, a configuration dictionary containing required configuration keys.

## NULL provider

The NULL provider is the default one if you don't set any. It **means that no transactional email will be sent**.

```ini
EMAIL_PROVIDER=NULL
```

## Postmark provider

Postmark provider will send transactional emails using [Postmark](https://postmarkapp.com).

| Parameter      | Description                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------------- |
| `server_token` | Your Postmark [Server API token](https://postmarkapp.com/developer/api/overview#authentication) |

```ini
EMAIL_PROVIDER=POSTMARK
EMAIL_PROVIDER_PARAMS={"server_token": "XXX-XXX"}
```

--8<-- "reusables/environment-variables-callout.md"
