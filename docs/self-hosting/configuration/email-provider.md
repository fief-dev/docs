---
description: >-
  Instructions to configure an email provider to let Fief send transactional
  emails.
---

# Email provider

As you surely now, users management imply a lot of transactional emails, like welcome emails or reset password emails. To be able to send them, Fief needs an email provider.

Currently, Fief supports the following providers:

* **SMTP** server.
* **[Postmark](https://postmarkapp.com)**, one of the leading email delivery service on the market.
* **[SendGrid](https://sendgrid.com/)**, another highly popular choice for email delivery.

There are two environment variables to configure the email provider: `EMAIL_PROVIDER`, to set the type of provider and `EMAIL_PROVIDER_PARAMS`, a configuration dictionary containing required configuration keys.

## NULL provider

The NULL provider is the default one if you don't set any. It **means that no transactional email will be sent**.

```ini
EMAIL_PROVIDER=NULL
```

## SMTP provider

SMTP provider will send transactional emails through the configured SMTP server.

| Parameter  | Description                                                | Default |
| ---------- | ---------------------------------------------------------- | ------- |
| `host`     | Hostname of your SMTP server.                              |         |
| `username` | Username to authenticate to your SMTP server.              | `None`  |
| `password` | Password to authenticate to your SMTP server.              | `None`  |
| `port`     | Port of your SMTP server. Typically, `25`, `485` or `587`. | `587`   |
| `ssl`      | Whether to use SSL/TLS to connect to your SMTP server.     | `True`  |

```ini
EMAIL_PROVIDER=SMTP
EMAIL_PROVIDER_PARAMS={"host": "smtp.bretagne.duchy", "username": "anne", "password": "herminetincture"}
```

## Postmark provider

Postmark provider will send transactional emails using [Postmark](https://postmarkapp.com).

| Parameter      | Description                                                                   | Default |
| -------------- | ----------------------------------------------------------------------------- | ------- |
| `server_token` | Your Postmark [Server API token](https://account.postmarkapp.com/api_tokens). |         |

```ini
EMAIL_PROVIDER=POSTMARK
EMAIL_PROVIDER_PARAMS={"server_token": "XXX-XXX"}
```

## SendGrid provider

SendGrid provider will send transactional emails using [SendGrid](https://sendgrid.com/).

| Parameter | Description                                                                          | Default |
| --------- | ------------------------------------------------------------------------------------ | ------- |
| `api_key` | Your SendGrid [API key](https://docs.sendgrid.com/ui/account-and-settings/api-keys). |         |

```ini
EMAIL_PROVIDER=SENDGRID
EMAIL_PROVIDER_PARAMS={"api_key": "XXX-XXX"}
```
