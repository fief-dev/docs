# Render

[Render](https://render.com/) is a very popular Platform as a Service (PaaS). It allows to quickly host and serve your applications without worrying about server management.

We provide an official blueprint creating all the services you need to run Fief.

## Before starting

1. If you don't have one yet, create an account on [Render](https://render.com).
2. Go to [https://dashboard.render.com/env-groups](https://dashboard.render.com/env-groups)
3. Create a **New Environment Group** and name it **fief** (all lowercase)

You can then proceed to the blueprint!

## Apply the blueprint

We provide variations for each **data center locations** supported by Fief. The best practice is to choose the one **closer to you and your users**.

Click on the links below to start creating the blueprint in the region of your choice:

[Deploy to Oregon (US West)](https://render.com/deploy?repo=https://github.com/fief-dev/render/tree/region-oregon){ .md-button }
[Deploy to Ohio (US East)](https://render.com/deploy?repo=https://github.com/fief-dev/render/tree/region-ohio){ .md-button }
[Deploy to Frankfurt (EU)](https://render.com/deploy?repo=https://github.com/fief-dev/render/tree/region-frankfurt){ .md-button }
[Deploy to Singapore (Asia-Pacific)](https://render.com/deploy?repo=https://github.com/fief-dev/render/tree/region-singapore){ .md-button }
{: .buttons }

## Fill the environment variables

We already set most of the environment variables, but you still have to set a few ones.

You can find the reference of those values in the [environment variables](../environment-variables.md) section.

![Fill the environment variables during Render deployment](/assets/images/deployment-render-variables.png)

--8<-- "reusables/fernet-key-generator.md"

## Set the custom domain

When the deployment is done, you need to link your domain with the `fief-server` service. Open the **Settings** of this service and in the **Custom Domains** section, add your domain.

![Custom domain configuration on Render](/assets/images/deployment-render-domain.png)

## Cost estimation

Render bills each service individually. Fief needs **four of them**:

* A server process (starting at 7 USD per month)
* A worker process (starting at 7 USD per month)
* A PostgreSQL database (starting at 7 USD per month)
* A Redis database (starting at 10 USD per month)

For a small or medium sized-instance, the cost should hence be around **31 USD per month**.
