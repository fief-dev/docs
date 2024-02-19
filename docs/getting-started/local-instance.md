---
hide:
  - toc
---

# 1. Start your local Fief instance

We provide a [Docker](https://www.docker.com/get-started) image to help you start the Fief server locally in no time!

## Quickstart command

Run the following command:

```bash
docker run -it --rm ghcr.io/fief-dev/fief:latest fief quickstart --docker
```

The command will ask you to give an email address for the first **admin user**. It'll be automatically created when starting the server.

```bash
User email: anne@bretagne.duchy
User password: XXX
Repeat for confirmation: XXX
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
  -e "FIEF_MAIN_USER_EMAIL=anne@bretagne.duchy" \
  -e "FIEF_MAIN_USER_PASSWORD=XXX" \
  -e "CSRF_COOKIE_SECURE=False" \
  -e "SESSION_DATA_COOKIE_SECURE=False" \
  -e "USER_LOCALE_COOKIE_SECURE=False" \
  -e "LOGIN_SESSION_COOKIE_SECURE=False" \
  -e "SESSION_COOKIE_SECURE=False" \
  -e "FIEF_ADMIN_SESSION_COOKIE_SECURE=False" \
  ghcr.io/fief-dev/fief:latest
```

!!! warning "Save those secrets somewhere safe!"
    If you need to restart or recreate your container, you'll need to set the same secrets again. If you lose them, you'll likely lose access to data or have a bad configuration. [Read more about secrets and environment variables.](../self-hosting/environment-variables.md)

!!! info
    The container is available on the port **8000** of your local machine by default.

## Good to go!

At this point, your Fief server should be up-and-running! Open [http://localhost:8000/admin/](http://localhost:8000/admin/) to access the admin dashboard. You'll be redirected to a login page. Authenticate with the user credentials you specified in the previous section.

![Fief login page](/assets/images/fief-login.png)

You'll then be redirected to the admin dashboard.

![Admin dashboard](/assets/images/admin-dashboard.png)

Congratulations! Your Fief server instance is up-and-running 🎉 You can now try Fief features and start to integrate authentication in your app.

!!! tip
    For production deployment, we strongly recommend you to go through the [self-hosting](../self-hosting/index.md) documentation.
