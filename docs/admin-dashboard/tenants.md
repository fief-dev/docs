# Tenants

This is where you'll see and manage the tenants of your workspace.

--8<-- "reusables/tenant-callout.md"

![Tenants from admin dashboard](/assets/images/admin-tenants.png)

## Base URL

Each tenant is tied to a **base URL**: each routes, like login or registration, will be derived from this base. When you integrate Fief in your application, you'll need this base URL.

Each workspace has **one default tenant** with a base URL pointing to your root subdomain, like *https://example.fief.dev*.

Other tenants gets a path prefix, like *https://example.fief.dev/other-tenant*.

!!! tip
    You can copy the base URL directly using the clipboard button in the list.


## Create a new tenant

You can create a new tenant by clicking the **Create Tenant** button. A modal will open where you'll be able to input its name. The [base URL](#base-url) is automatically generated from the name.

![Create tenant from admin dashboard](/assets/images/admin-tenants-create.png)

## Edit an existing tenant

If you click on one of the tenant in the list, you'll see its details on the right and be able to change its properties.

![Edit tenant from admin dashboard](/assets/images/admin-tenants-edit.png)

## Disable user registration

You can choose to **disable user registration** on a tenant. To do this, you have to uncheck the **Registration allowed** checkbox in the tenant details.

When registration is disabled, users can't access the registration page and create a new account on this tenant.