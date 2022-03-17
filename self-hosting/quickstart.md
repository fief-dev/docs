---
description: Start your local Fief instance in a few minutes.
---

# Quickstart

We provide a [Docker](https://www.docker.com/get-started) image to help you start the Fief server locally in no time!

Run the following command:

```bash
docker run --rm ghcr.io/fief-dev/fief:latest fief quickstart --docker
```

The result of this command is a complete **`docker run` command** with the required **secrets** generated to help you get started. It'll look like the following:

```bash
docker run \
  --name fief-server \
  -d \
  -e "SECRET=XXX" \
  -e "FIEF_CLIENT_ID=XXX" \
  -e "FIEF_CLIENT_SECRET=XXX" \
  -e "ENCRYPTION_KEY=XXX" \
  ghcr.io/fief-dev/fief:latest
```

{% hint style="warning" %}
**Save those secrets somewhere safe!**

If you need restart or recreate your container, you'll probably need to set the same secrets again. If you lose them, you'll likely lose access to data or have a bad configuration.

Read more about secrets and environment variables.
{% endhint %}
