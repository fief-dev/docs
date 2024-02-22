# Email templates

Quite often, Fief needs to **send emails to your users**. More precisely, it will send the following emails:

* The **Welcome** email, after a successful **user registration**;
* The **Forgot password** email, when a user asks to reset its password.

By default, your instance is initialized with **basic templates**. While they can do the job for getting started, you'll likely want to customize them so it matches your branding.

Fief comes with a built-in mechanism to **customize email templates**, based on [Jinja templating language](https://jinja.palletsprojects.com/en/3.0.x/templates/).

## Base template

Fief defines a **Base template** from which every emails will inherit from. It's useful to define common CSS and blocks that will be reused in every emails.

The default template is based on the [Mailmason template](https://github.com/ActiveCampaign/mailmason) from Postmark. It comes with a set of CSS rules that plays well with email clients. You can use it as a base or start from scratch, it's up-to-you! The default template comes with the following blocks:

<div class="excalidraw">
--8<-- "docs/assets/images/email-templates-base-layout.svg"
</div>

* `preheader`: this block allows you to add content that **won't be shown** in the email body. It's used to finely control the email preview in the inbox list.
* `main`: this block will bear the actual content of the email.
* `footer`: this block will appear at the end of the email and can be used to put legal terms or social networks links.

Before the `main` block, notice that we show the name of the tenant.

### Customize

You can customize the Base template from admin dashboard. On the left menu, click on **Customization** and **Email templates**. You'll see the list of all available templates.

![Email templates from admin dashboard](/assets/images/admin-email-templates.png)

Click on the **Update** button in the front of the Base template row. An editor will open, with the HTML code on the left and a preview on the right.

![Update email templates from admin dashboard](/assets/images/admin-email-templates-edit.png)

### Context

The **context** defines the available variables you can use in the template. The Base template gives you access to the following context:

**The tenant of the user, `tenant`, with the following properties**

  * `id` (`uuid.UUID`): ID of the tenant.
  * `created_at` (`datetime`): Creation date of the tenant.
  * `updated_at` (`datetime`): Last update date of the tenant.
  * `name` (`str`): Name of the tenant.
  * `default` (`bool`): Whether it is the default tenant.
  * `slug` (`str`): Slug of the tenant, i.e. the part of the base URL after the domain.
  * `registration_allowed` (`str`): Whether registration are allowed or not for this tenant.


**The recipient user, `user`, with the following properties:**

  * `id` (`uuid.UUID`): ID of the user.
  * `created_at` (`datetime`): Creation date of the user.
  * `updated_at` (`datetime`): Last update date of the user.
  * `email` (`str`): Email address of the user.
  * `tenant_id` (`uuid.UUID`): ID of the associated tenant.
  * `fields` (`dict[str, Any]`): Dictionary giving you the [user fields](../user-fields.md) values for this user, indexed by their slug.

!!! tip "Examples"

    ```html
    <h1>{{ tenant.name }}</h1>
    ```

    ```html
    <p>Hello, {{ user.fields.first_name }} 👋</p>
    ```

## Welcome template

The **Welcome template** is used to send an email when a **new user registers**. It's the ideal message to welcome them, show them the basics of your application or give them relevant information.

The default template looks like this:

```html
{% extends "BASE" %}

{% block preheader %}Welcome to {{ tenant.name }}! We're thrilled to have you on board.{% endblock %}

{% block main %}
<h1>Welcome!</h1>
<p>Welcome to {{ tenant.name }}! We're thrilled to have you on board.</p>
{% endblock %}
```

You can see it's very lightweight: all we need to do is to define the **content of each block**. The magic happens thanks to the `{% extends "BASE" %}` instruction which tells Fief to inherit from the [Base template](#base-template).

### Subject

Using the text input above the code editor, you can customize the **subject** of the email. It accepts the same syntax and has the same context.

### Context

The context is the same as for [Base template](#context).

## Verify email template

The **Verify email template** is used to send an email when a **user needs to verify their email address**. It should contain the code the user should input on Fief to verify their email.

The default template looks like this:

```html
{% extends "BASE" %}

{% block preheader %}Use this code to verify your email address. This code is only valid for 1 hour.{% endblock %}

{% block main %}
  <h1>Verify your email address</h1>
  <p>You recently created or updated your email on your {{ tenant.name }}'s account. To verify your email address, please enter the verification code below.</p>
  <table class="discount" align="center" width="100%" cellpadding="0" cellspacing="0" role="presentation">
    <tr>
      <td align="center">
        <h1 class="f-fallback discount_heading">{{ code }}</h1>
        <p class="f-fallback discount_body">This verification code is only valid for the next hour.</p>
      </td>
    </tr>
  </table>
{% endblock %}
```

You can see it's very lightweight: all we need to do is to define the **content of each block**. The magic happens thanks to the `{% extends "BASE" %}` instruction which tells Fief to inherit from the [Base template](#base-template).

### Subject

Using the text input above the code editor, you can customize the **subject** of the email. It accepts the same syntax and has the same context.

### Context

The context is the same as for [Base template](#context). It also adds:

* `code` (`str`): The verification code the user should input.

## Forgot password template

The **Forgot password template** is used to send an email when a user wants to **reset their password**. The main purpose is to send them the link allowing them to change their password.

The default template looks like this:

```html
{% extends "BASE" %}

{% block preheader %}Use this link to reset your password. This link is only valid for 1 hour.{% endblock %}

{% block main %}
  <h1>Reset your password</h1>
  <p>You recently requested to reset your password for your {{ tenant.name }} account. Use the button below to reset it. <strong>This password reset link is only valid for the next hour.</strong></p>
  <table class="body-action" align="center" width="100%" cellpadding="0" cellspacing="0" role="presentation">
    <tr>
      <td align="center">
        <!-- Border based button
  https://litmus.com/blog/a-guide-to-bulletproof-buttons-in-email-design -->
        <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
          <tr>
            <td align="center">
              <a href="{{reset_url}}" class="f-fallback button button--green" target="_blank" rel="noopener noreferrer">Reset your password</a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
{% endblock %}
```

You can see it's very lightweight: all we need to do is to define the **content of each block**. The magic happens thanks to the `{% extends "BASE" %}` instruction which tells Fief to inherit from the [Base template](#base-template).

### Subject

Using the text input above the code editor, you can customize the **subject** of the email. It accepts the same syntax and has the same context.

### Context

The context is the same as for [Base template](#context). It also adds:

* `reset_url` (`str`): The URL where the user can reset their password.

## Templating language

The template language is based [Jinja templating language](https://jinja.palletsprojects.com/en/3.0.x/templates/), so all constructs accepted by Jinja are supported. In particular, you can insert dynamic values using the `{{ }}` syntax:

```html
<p>{{ user.email }}</p>
```

You can also define conditional blocks based on some values:

```html
{% if user.fields.newsletter %}
    <p>Thank you for subscribing to our newsletter 🎉</p>
{% else %}
    <p>You didn't subscribe to our newsletter 🥲</p>
{% endif %}
```
