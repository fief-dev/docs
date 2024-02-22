!!! tip "What is a Webhook?"
    A Webhook is a way for your application to **be notified automatically when something happens on your instance**.

    For example, you can configure a Webhook so your application get a notification when a new user registers. This way, you can run your own business logic, like add the user to a mailing list or a marketing tool.

    Technically, it works with **HTTP requests**: Fief will make requests to the URL you give it with the relevant data for the event. On your side, you'll need to accept this request and implement the logic you need accordingly.
