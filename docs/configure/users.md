# Users

This is where you'll see and manage the users of your instance.

--8<-- "reusables/user-callout.md"

![Users from admin dashboard](/assets/images/admin-users.png)

## Create a new user

In some circumstances, you might need to create a user manually from the admin dashboard. You can do so by clicking on the **Create User** button. A modal will open where you'll be able to input its email address, password and associated tenant.

You'll also be able to fill the values for your [custom user fields](./user-fields.md).

![Create users from admin dashboard](/assets/images/admin-users-create.png)

!!! info
    User created that way will receive the welcome email, as if they registered themselves.

## Edit an existing user

If you click on one of the user in the list, you'll see its details on the right and be able to update them.

![View user details from admin dashboard](/assets/images/admin-users-view.png)

If you click on the **Edit User** button, you'll be able to update its properties.

![Edit user from admin dashboard](/assets/images/admin-users-edit.png)

## Delete a user

You can delete a user by clicking on it on the list and click on the **Delete** button on the right.

![Delete user from admin dashboard](/assets/images/admin-users-delete.png)

## Assign roles and permissions to a user

--8<-- "reusables/access-control-callout.md"

Fief allows you to define [permissions and roles](./access-control.md) to determine what your users are allowed to do or not in your application. From the dashboard, you are able to assign permissions and roles to users.

### Assign a role

You can assign a role to a user by clicking on it in the list. It details will open on the right. Click on the **Roles** tab to see the roles they already have. From here, you can look for roles in the select menu. Click on **Add role** to assign it to the user.

![Add role to user from admin dashboard](/assets/images/admin-users-add-role.png)

!!! tip "Asssociated permissions are automatically granted"
    Of course, when you assign a role to a user, the permissions associated to this role are automatically granted to the user. Nothing more to do!

### Revoke a role

You can revoke a role from a user by clicking on the trash button in front of the role you want to remove.

![Revoke role from user from admin dashboard](/assets/images/admin-users-delete-role.png)

!!! tip "Asssociated permissions are automatically revoked"
    Of course, when you revoke a role from a user, the permissions associated to this role are automatically revoked from this user. Nothing more to do!

### Assign a permission

You can assign a single permission to a user by clicking on it in the list. It details will open on the right. Click on the **Permissions** tab to see the permissions they already have. Notice that **permissions granted through roles are also displayed**, in italic.

From here, you can look for permissions in the select menu. Click on **Add permission** to assign it to the user.

![Add permission to user from admin dashboard](/assets/images/admin-users-add-permission.png)

!!! warning "In general, you should prefer roles"
    Assigning a single permission can be convenient from time-to-time but we generally recommend to assign proper roles, even if they contain only one permission. This way, you can be more future-proof if you find that you actually need to add a new permission: rather than editing every users one by one, you'll only have to update the role once.

### Revoke a permission

You can revoke a permission from a user by clicking on the trash button in front of the permission you want to remove.

![Revoke permission from user from admin dashboard](/assets/images/admin-users-delete-permission.png)

## Displaying user fields

By default, every [user fields](./user-fields.md) are displayed in the list. You can customize the view by clicking on the button at the left of the **Create User** button. A menu will show up where you'll be able to **show or hide a field** by clicking on the eye icon and **reorder them** by drag-and-drop.

![Customize users fields view from admin dashboard](/assets/images/admin-users-customize-view.png)

## Create an access token

In some circumstances, like debugging, you might need to impersonate one of your users to better understand what is going on. To help you with this, you can generate an [access token](../getting-started/oauth2.md#access-token-and-id-token) directly from the admin dashboard.

To do this, click on one of the user in the list. You'll see its details on the right. Then, you can click on **Create an access token**. A modal will appear asking you on which [Client](./clients.md) the access token will be tied and what are its allowed scopes. You'll at least need the `openid` scope, which is filled by default.

![Create user access token from admin dashboard](/assets/images/admin-users-create-access-token.png)

Finally, click on **Create** to generate the access token. It'll be valid for **1 hour**.

![User access token created from admin dashboard](/assets/images/admin-users-access-token-created.png)

!!! warning "Treat this access token with extreme care"
    This access token gives access to a user account. Don't save it in a file and don't share it online.
