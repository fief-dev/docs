---
description: Start your local Fief instance in a few minutes.
---

# Quickstart

We provide a [Docker](https://www.docker.com/get-started) image to help you start the Fief server locally in no time!

Run the following command:

```bash
docker run --rm ghcr.io/fief-dev/fief:latest fief quickstart --docker
```

The result of this command is a complete **`docker run` command** with the required **secrets** generated and environment variables to help you get started. It'll look like the following:

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

!!! warning "Save those secrets somewhere safe!"
    If you need restart or recreate your container, you'll probably need to set the same secrets again. If you lose them, you'll likely lose access to data or have a bad configuration. [Read more about secrets and environment variables.](environment-variables.md)

!!! info
    The container is exposed on the port **8000** of your local machine by default.

## Create main workspace

Next, you'll need to create the main **workspace**. Simply run the following command:

```bash
docker exec fief-server fief workspaces create-main
```

You should see the following output:

```
Main Fief workspace created
```

## Create admin user

Finally, you need to create an **admin user** for this main workspace that'll have access to the admin dashboard. Run the following command:

```bash
docker exec -it fief-server fief workspaces create-main-user --user-email anne@bretagne.duchy
```

!!! tip
    Of course, make sure to replace `--user-email` value with your own email address!

You'll then be prompted for a password. If everything goes well, you should see the following output:

```
Main Fief user created
```

## Good to go!

At this point, your Fief server should be up-and-running! Open [http://localhost:8000/admin/](http://localhost:8000/admin/) to access the admin dashboard. You'll be redirected to a login page. Authenticate with the user credentials you created in the previous section.

![Fief login page](/assets/images/fief-login.png)

You'll then be redirected to the admin dashboard.

![Admin dashboard](/assets/images/admin-dashboard.png)

Congratulations! Your Fief server instance is up-and-running 🎉 You can now try Fief features and start to integrate authentication in your app.

!!! tip
    For production deployment, we strongly recommend you to read the next sections.

## Limitations

While quick and convenient, this way of running Fief is **not suitable for production environments**. Under the hood, it stores the data in the form of **SQLite databases**. If you ever happen to destroy your container, you'll lose all your data.

The best way is of course to configure a proper PostgreSQL or MySQL database for your Fief server, as described in the dedicated section.

[Setup database](setup-database.md){ .md-button }
{: .buttons }

### Use a Docker volume to persist SQLite data

If you really want to use SQLite, or mitigate the risk of losing data in your local environment, you can attach your container to a [Docker volume](https://docs.docker.com/storage/volumes/). This way, even if the container is destroyed, you can create a new one and attach again the data.

The first thing to do is to create a Docker volume:

```
docker volume create fief-server-data
```

Then, create your Fief server container and attach this volume to the `/data` folder on the container:

```bash
docker run \
  --name fief-server \
  -p 8000:8000 \
  -d \
  -v fief-server-volume:/data \
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

!!! warning
    If you created your container with the instructions in the previous section, you'll need to recreate one from scratch to bind the volume.

## Custom local domain and port

The quickstart command assume your Fief server will be served over `localhost:8000`. Besides, additional workspaces will be automatically assigned a subdomain like `bretagne.localhost:8000`.

However, you might want to serve it locally on a custom domain you have wired manually on your local machine, like `fief.test`. In this case, you can use the `--host` parameter of the quickstart command to slightly adapt the Docker command.

```bash
docker run --rm ghcr.io/fief-dev/fief:latest fief quickstart --docker --host fief.test
```

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
  -e "ROOT_DOMAIN=fief.test:8000" \
  -e "FIEF_DOMAIN=fief.test:8000" \
  -e "CSRF_COOKIE_SECURE=False" \
  -e "LOGIN_SESSION_COOKIE_SECURE=False" \
  -e "SESSION_COOKIE_SECURE=False" \
  -e "FIEF_ADMIN_SESSION_COOKIE_SECURE=False" \
  ghcr.io/fief-dev/fief:latest
```

You can also customize the exposed port by using the `--port` parameter of the quickstart command:

```bash
docker run --rm ghcr.io/fief-dev/fief:latest fief quickstart --docker --host fief.test --port 9000
```

```bash
docker run \
  --name fief-server \
  -p 9000:9000 \
  -d \
  -e "SECRET=XXX" \
  -e "FIEF_CLIENT_ID=XXX" \
  -e "FIEF_CLIENT_SECRET=XXX" \
  -e "ENCRYPTION_KEY=XXX" \
  -e "PORT=9000" \
  -e "ROOT_DOMAIN=fief.test:9000" \
  -e "FIEF_DOMAIN=fief.test:9000" \
  -e "CSRF_COOKIE_SECURE=False" \
  -e "LOGIN_SESSION_COOKIE_SECURE=False" \
  -e "SESSION_COOKIE_SECURE=False" \
  -e "FIEF_ADMIN_SESSION_COOKIE_SECURE=False" \
  ghcr.io/fief-dev/fief:latest
```

Notice how the different variables changed to adapt to the custom port.
