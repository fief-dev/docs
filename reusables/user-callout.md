!!! tip "What is a user?"
    A user is the fundamental part of your Fief instance: it represents the actual user that'll have access to your application!

    We store basic information about the user, like its email address and hashed password and take care of verifying its credentials upon login.

    Every user is tied to a [tenant](/configure/tenants). It means that an individual can have several user accounts on your instance, with the same email address, but tied to a different tenant.
