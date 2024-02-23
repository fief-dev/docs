# SSL and HTTPS

When deploying into production, you'll need to configure the Fief server so it correctly works with HTTPS/SSL. Usually, cloud providers or container orchestration tools use a **reverse proxy** that takes care of the SSL negotiation before handing over to the actual service. That's why our image doesn't come with a built-in mechanism to handle it.

However, you'll need to set several environment variables to be sure everything works correctly with HTTPS/SSL.

## Trust reverse proxy headers

After the reverse proxy handled the HTTPS/SSL connection, it forwards the HTTP request to the underlying server and usually add `X-Forwarded-*` headers to tell the server it was correctly served over SSL.

For security reasons, those headers are ignored by default. You need to tell Fief server to trust those headers if they come from specific IP addresses. To do this, you need to set the `FORWARDED_ALLOW_IPS` environment variable.

This variable expects a comma separated list of IPs to trust. For example:

```ini
FORWARDED_ALLOW_IPS=10.0.0.2,10.0.0.3
```

In some circumstances, like cloud providers, you don't know the IP of the reverse proxy. In this case, you can set this value to `*` to tell the Fief server to trust any IP.

```ini
FORWARDED_ALLOW_IPS=*
```

!!! danger "Make sure your server is reachable only via the proxy"

    With the value `*`, it's critical to make sure your Fief server is not reachable directly from the internet, without passing by the proxy. Otherwise, malicious users could make requests with arbitrary `X-Forwarded-*` headers.

## Cookie Secure flags

By default, all environment variables ending with `_COOKIE_SECURE` are set to `True`. Make sure you don't set them to `False` in production environment.
