---
description: Instructions to configure your Fief server on a PostgreSQL or MySQL database.
---

# Database

For production environments, your Fief server should store its data in a proper database server for better performance and reliability. Fief is compatible with **PostgreSQL** and **MySQL** databases.

## Setup PostgreSQL

We'll assume that you have a working PostgreSQL database running, either locally or in the cloud. All you need to do is to set the corresponding environment variables with your database credentials.

```ini
DATABASE_TYPE=POSTGRESQL
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=fief
DATABASE_PASSWORD=fiefpassword
DATABASE_NAME=fief
```

## Setup MySQL

We'll assume that you have a working MySQL database running, either locally or in the cloud. All you need to do is to set the corresponding environment variables with your database credentials.

```ini
DATABASE_TYPE=MYSQL
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USERNAME=fief
DATABASE_PASSWORD=fiefpassword
DATABASE_NAME=fief
```

## Use a connection string

Some cloud providers like Heroku will provide you a full database connection string like the one below instead of each parts separately:

```
postgresql://fief:fiefpassword@localhost:5432/fief
```

Fief supports this kind of configuration with the `DATABASE_URL` environment variable.

```ini
DATABASE_TYPE=POSTGRESQL
DATABASE_URL=postgresql://fief:fiefpassword@localhost:5432/fief
```

!!! warning
    This variable will **always** take precedence over the single parameters: if you define `DATABASE_URL`, it'll use this variable to connect to your database, even if other parameters are defined.
