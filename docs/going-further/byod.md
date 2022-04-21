# Bring your own database

This is one of the most iconic feature of Fief. "Bring your own database" allows you to configure **your very own SQL database**, hosted anywhere you want, and let Fief stores all your data into it. This is especially useful if you have special requirements about where and how your data should be stored.

Then, Fief will execute its logic by reading and writing data to your database, and nowhere else.

!!! tip "I want to host everything myself!"
    If you don't want to use our cloud instance at all, you can also host the entire Fief server on your own! You can find [detailed instructions here](../self-hosting/quickstart.md).

## Setup your database

You can configure your database during the [creation of your workspace](../getting-started/workspace.md). At step 2, select the option **My own database**.

![Select the option My own database](/assets/images/byod-select-type.png)

Then, you'll need to enter the details about your database.

![External database configuration](/assets/images/byod-database-configuration.png)

* **Database type**: you have the choice between a PostgreSQL and MySQL database.
* **Host**
* **Port**
* **Username**
* **Password**
* **Database name**

!!! success "Credentials are encrypted on Fief"
    To protect your database credentials, we encrypt them using the [Fernet method](https://github.com/fernet/spec/). It means that even if a malicious individual achieves to access our systems, they couldn't steal your credentials.

!!! warning "My database server requires external IP to be allowlisted"
    Unfortunately, our current hosting infrastructure doesn't allow us to provide you a stable list of IP addresses to allow. This is something we are aware of and are actively looking for a solution.

    In the meantime, you can try to [self-host](../self-hosting/quickstart.md) the full Fief server.

After this step, we'll try to connect to your database and create the schema Fief needs to work. You'll then be redirected to your admin dashboard, where you'll be able to manage your workspace.

![Admin dashboard](/assets/images/admin-dashboard.png)

## How Fief uses your database?

### Schema

Fief won't directly use the database instance you provide. Instead, it'll create another dedicated **schema**.

* For PostgreSQL servers, it'll create a [schema](https://www.postgresql.org/docs/current/ddl-schemas.html), which could be more or less described as a "sub-database".
* For MySQL servers, it'll create another database instance.

### Migrations

Fief maintain a migration table in your database to keep track of changes to the tables schema. When we deploy updates to Fief that needs to add or modify tables, we'll automatically apply migrations on your database.

### Don't edit data yourself!

When you have access to the database, it might be tempting to manually add or modify data. **DON'T DO THIS**. If you make a mistake, you'll probably break your whole Fief workspace and your users won't be able to authenticate anymore.

If you really need to make a special operation on your data, please [ask us first](https://github.com/fief-dev/fief/discussions), we'll help you to do it safely.
