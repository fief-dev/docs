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

We have two Fief containers: one for the **web server** and one for the **worker**.

We also defined a dedicated database container, PostgreSQL, and a broker for passing job messages, Redis. Note how we defined and linked a **volume** for both of them. By doing this, we make sure we persist our data in a dedicated Docker volume that will persist even if we delete the containers.

The `.env` file will contain all the [environment variables](../environment-variables.md) for configuring Fief. You can have more details about the configuration of your database and email provider in the dedicated sections.

[Setup database](setup-database.md){ .md-button }
[Setup email provider](setup-email-provider.md){ .md-button }
{: .buttons }

!!! warning "Backup the volumes"
    You should probably think about a proper **backup method** for those volumes. A convenient solution is to use [`docker-volume-backup`](https://github.com/jareware/docker-volume-backup), a dedicated Docker image capable of archiving Docker volumes and send them to a distant storage.

!!! tip "You'll probably want a reverse proxy"
    In general, we don't directly expose the web server to the internet. A common pattern is to use a **reverse proxy**, which takes care of routing the incoming requests. It's also a great candidate to manage [HTTPS/SSL](./ssl.md). A common choice is [Traefik Proxy](https://doc.traefik.io/traefik/), which is very convenient to use with Docker containers.
