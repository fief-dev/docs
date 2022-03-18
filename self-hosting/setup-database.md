---
description: Instructions to configure your Fief server on a PostgreSQL or MySQL database.
---

# Setup database

For production environments, your Fief server should store its data in a proper database server for better performance and reliability. Fief is compatible with **PostgreSQL** and **MySQL** databases.

## Setup PostgreSQL

We'll assume that you have a working PostgreSQL database running, either locally or in the cloud. All you need to do is to set the corresponding environment variables with your database credentials.

```systemd
DATABASE_TYPE=POSTGRESQL
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=fief
DATABASE_PASSWORD=fiefpassword
DATABASE_NAME=fief
```

{% hint style="info" %}
You can read about different ways of setting environment variables in the [dedicated section](environment-variables.md#set-environment-variables).
{% endhint %}

## Setup MySQL

We'll assume that you have a working MySQL database running, either locally or in the cloud. All you need to do is to set the corresponding environment variables with your database credentials.

```systemd
DATABASE_TYPE=MYSQL
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USERNAME=fief
DATABASE_PASSWORD=fiefpassword
DATABASE_NAME=fief
```

{% hint style="info" %}
You can read about different ways of setting environment variables in the [dedicated section](environment-variables.md#set-environment-variables).
{% endhint %}

## Create main workspace and admin user

Once your database is configured, don't forget to create the main workspace and admin user, as described in the [Quickstart](quickstart.md) section.
