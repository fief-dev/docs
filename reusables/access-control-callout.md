!!! tip "What are permissions and roles?"
    **Permissions** are a way to list the **actions** a user will be allowed to perform in your application. For example, if you have a resource in your application called *Castle*, we can define the permissions *Read Castle* and *Create Castle*.

    Then, those permissions can be **assigned to users**. You'll then be able to control this list of permissions in your app to determine if the current user is able to perform the action they request.

    Assigning permissions directly to users can be tedious and error-prone. To help with this, Fief also supports the concept of **Roles**. A role consists of a **set of permissions**. Following our previous example, we can imagine to have the roles *Castle Visitor*, which only have the *Read Castle* permission and a *Castle Manager* role, which have both *Read Castle* and *Create Castle* permissions.

    Those roles can also be **assigned to users**. Then, they'll be automatically granted with the **set of associated permissions**. The good thing is that if you modify a role to add or remove permissions, it'll be automatically be passed on every users with this role. Said another way, it's a way to easily organize and assing permissions.
