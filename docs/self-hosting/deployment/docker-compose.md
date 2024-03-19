# Docker Compose

The quickstart Docker image is an **all-in-one container** launching the Fief server, the Fief worker for background jobs and a Redis server to schedule those jobs. While suitable for local development and testing, it's usually better in production to have **dedicated containers for each purpose**.

[Docker Compose](https://docs.docker.com/compose/) greatly simplifies the configuration of multiple containers. This is probably the easiest way if you already know Docker and want to deploy on your own server. You'll find below a typical `docker-compose.yml` configuration for Fief.

=== "docker-compose.yml"

    ```yaml
    --8<-- "examples/deployment/docker-compose/docker-compose.yml"
    ```

=== ".env"

    ```ini
    --8<-- "examples/deployment/docker-compose/.env"
    ```

## Fief containers

We have two Fief containers: one for the **web server**, `fief-server`, and one for the **worker**, `fief-worker`. Both are required to make Fief working correctly.

## Database and Redis containers

We also defined a dedicated database container, PostgreSQL, and a broker for passing job messages, Redis. Note how we defined and linked a **volume** for both of them. By doing this, we make sure we persist our data in a dedicated Docker volume that will persist even if we delete the containers.

## Traefik reverse proxy

A reverse proxy is a specialized software able to accept incoming HTTP requests and route them to the underlying applications. It acts as the unique HTTP entrypoint to our system. Here, it'll simply route requests with the domain `fief.mydomain.com` to the `fief-server` container.

It's also in charge for managing **SSL certificates**. In this configuration, Traefik will automatically issue a free [Let's Encrypt](https://letsencrypt.org/) certificate for the domain `fief.mydomain.com`, using the TLS challenge. Traefik supports [other types of challenge](https://doc.traefik.io/traefik/user-guides/docker-compose/acme-tls/) that may be more suitable for your use-case. The volume `letsencrypt-data` is here to store the generated certificates.

We strongly suggest you to read more about how to configure Traefik with Docker Compose: [https://doc.traefik.io/traefik/user-guides/docker-compose/basic-example/](https://doc.traefik.io/traefik/user-guides/docker-compose/basic-example/)

## `.env` file

The `.env` file will contain all the [environment variables](../environment-variables.md) for configuring Fief. You can have more details about the configuration of email provider in the dedicated sections.

[Configure email provider](../configuration/email-provider.md){ .md-button }
{: .buttons }

!!! warning "Backup the volumes"
    You should probably think about a proper **backup method** for those volumes. A convenient solution is to use [`docker-volume-backup`](https://github.com/jareware/docker-volume-backup), a dedicated Docker image capable of archiving Docker volumes and send them to a distant storage.
