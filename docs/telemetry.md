---
hide:
  - navigation
---

# Telemetry

To better understand how Fief is used and improve the project, we collect some analytics on your instances.

This data is collected and analyzed on [PostHog](https://posthog.com/), on the European data center.

## What we collect?

We collect analytics information about:

* The server:
    * Its version
    * The type of database used (PostgreSQL, MySQL or SQLite)
    * If it runs on localhost
    * The number of users
* The admin dashboard:
    * Page views
    * Page clicks interactions
    * Browser language and version

The server will push this data **every hour** to our analytics.

## What we do **not** collect?

We do not collect:

* Your self-hosted server host
* Data about your users
* Analytics data on the authentication pages (login, register, forgot password...)

## Opt-out telemetry

If you don't wish to send analytics data when deploying your Fief server, you can set the [environment variable](./self-hosting/environment-variables.md) `TELEMETRY_ENABLED` to `False`.

## Can I see the source code for this?

For sure! The interesting parts for telemetry are:

* [`fief/services/posthog.py`](https://github.com/fief-dev/fief/blob/main/fief/services/posthog.py)
* [`fief/tasks/heartbeat.py`](https://github.com/fief-dev/fief/blob/main/fief/tasks/heartbeat.py)
* [`fief/scheduler.py`](https://github.com/fief-dev/fief/blob/main/fief/scheduler.py#L13-L16)
* [`fief/templates/admin/base.html`](https://github.com/fief-dev/fief/blob/main/fief/templates/admin/base.html#L14-L25)
