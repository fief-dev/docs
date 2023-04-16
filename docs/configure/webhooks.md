# Webhooks

This is where you'll see and manage the webhooks of your workspace.

--8<-- "reusables/webhook-callout.md"

![Webhooks from admin dashboard](/assets/images/admin-webhooks.png)

## Create a new Webhook

To create a new Webhook, click on the **Create Webhook** button. A modal will open where you'll be able to input the **URL where you want to receive notifications**. Besides, you'll be able to select the **events you are interested in**.

![Create Webhook from admin dashboard](/assets/images/admin-webhooks-create.png)

When you submit the form, a new modal will open with the **Webhook secret**. For security reasons, it'll be shown **only once**. Copy and paste it somewhere safe before closing the modal. You'll need it to properly **validate the authenticity of the request**.

![Webhook secret from admin dashboard](/assets/images/admin-webhooks-secret.png)

!!! warning "Keep it secret and safe"
    The secret is used to sign and authenticate Webhook requests. Keep it somewhere safe and don't share it with anyone.

When this is done, Fief will start to send events to your URL. You should now read our Webhook integration guide to understand how to handle it in your application.

[Integrate Webhooks in my app](../api/webhooks/guide.md){ .md-button }
{: .buttons }

## Edit an existing Webhook

You can edit an existing Webhook by clicking on it in the list and then click the **Edit Webhook** button. A modal will open where you'll be able to change its URL and enabled events.

![Edit Webhook from admin dashboard](/assets/images/admin-webhooks-edit.png)

## Regenerate secret of an existing Webhook

If you lost your Webhook secret or if it was compromised, you can regenerate it by clicking on the yellow **Regenerate secret** button. A new modal will open with your new secret. For security reasons, it'll be shown **only once**. Copy and paste it somewhere safe before closing the modal.

![Webhook secret from admin dashboard](/assets/images/admin-webhooks-secret.png)

!!! warning "Keep it secret and safe"
    The secret is used to sign and authenticate Webhook requests. Keep it somewhere safe and don't share it with anyone.

## Delete an existing Webhook

If you don't need a Webhook anymore, you can delete it by clicking on it in the list and then click the **Delete Webhook** button.

![Delete Webhook from admin dashboard](/assets/images/admin-webhooks-delete.png)

## View Webhook logs

Fief stores a **log of each request it makes to your URL**. It's useful to make sure your notification is correctly delivered and gives you insights when something goes wrong so you can correct things.

You can access the logs of a specific Webhook by clicking on its **Logs** button in the list.

![Webhook logs from admin dashboard](/assets/images/admin-webhooks-logs.png)
