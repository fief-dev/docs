---
hide:
  - navigation
---

# Telemetry

To better understand how Fief is used and improve the project, we collect some analytics data both on official Fief instance and self-hosted instances.

This data is collected and analyzed on [PostHog](https://posthog.com/), on the European data center.

## What we collect?

We collect analytics information about:

* The server:
    * Its version
    * The type of database used (PostgreSQL, MySQL or SQLite)
    * If it runs on localhost
* The workspaces:
    * The server they are created on
    * The number of users
    * If it uses the [Bring Your Own Database](./going-further/byod.md) feature and, if it does, the database type (PostgreSQL, MySQL or SQLite)
* The admin dashboard:
    * Associated server and workspace
    * Page views
    * Page clicks interactions
    * Browser language and version

## What we do **not** collect?

We do not collect:

* Your self-hosted server host
* Data about your users
* Analytics data on the authentication pages (login, register, forgot password...)

## Opt-out telemetry on self-hosted server

If you don't wish to send analytics data when deploying your Fief server, you can set the [environment variable](./self-hosting/environment-variables.md) `TELEMETRY_ENABLED` to `False`.
