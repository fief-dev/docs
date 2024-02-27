# Railway

Railway is a modern is a very popular Platform as a Service (PaaS). It allows to quickly host and serve your applications without worrying about server management.

We provide an official template creating all the services you need to run Fief.

## Get started

Click on the button below and follow the instructions.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/LO03gz?referralCode=uch-he)
{ .text-center }

You'll be prompted to configure two environment varialbles: [`FIEF_MAIN_USER_EMAIL`](../environment-variables.md#fief-ception) and [`FIEF_MAIN_USER_PASSWORD`](../environment-variables.md#fief-ception). Those are the credentials of the first admin user that'll be created on server startup.

![Configuration variables on Railway template](../../assets/images/deployment-railway-variables.png)

After a few minutes, your Fief server will be up-and-running on the default Railway subdomain!

## Custom domain

By default, the project will be assigned a default Railway subdomain, like `server-production-4018.up.railway.app`.

To add your domain, follow the instructions on Railway documentation: [https://docs.railway.app/guides/public-networking#custom-domains](https://docs.railway.app/guides/public-networking#custom-domains)

!!! warning "Redeploy the server and worker afterwards"
    To make sure Fief correctly takes into account the new domain, it's important to trigger a redeploy on the server and worker process.

## Cost estimation

Railway's pricing is based on memory, CPU and network usage. Thus, the pricing will **highly vary depending on your workload**.

We estimate that for a small or medium sized-instance, the cost should be **around 10 and 20 USD per month**.
