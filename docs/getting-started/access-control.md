# Access control

This is where you'll see and manage the permissions and roles of your workspace.

--8<-- "reusables/access-control-callout.md"

## Permissions

The first item in the menu is the permissions page, showing you a list of all your permissions.

![Permissions from admin dashboard](/assets/images/admin-permissions.png)

### Create a new permission

To create a new permission, fill the fields above the list: the **name** and the **codename** of your permission. The codename is what will be used to identify your permission in the access tokens. It must be **unique across your workspace**.

![Create permission from admin dashboard](/assets/images/admin-permissions-create.png)

Submit the form by clicking on **Create Permission**. The newly created permission will appear in the list.

!!! tip "Naming your permissions"
    You are completely free to choose the name and codenames you wish for your permissions. However, we suggest you to **establish a convention** so it'll be easy for you and your teams to remember them.

    Typically, you'll have a common set of actions (read, create, update, delete...) for each resources (Post, Product, Meeting...) in your app. A common practice is to prefix the codename with the name of the resource and append the corresponding action: `post:read`, `post:create`, `post:update`...

### Delete a permission

If one of your permission is not useful anymore, you can delete it by clicking on the **Delete** button in the list.

![Delete permission from admin dashboard](/assets/images/admin-permissions-delete.png)

!!! danger "The permission will be removed from all the associated roles and users"
    When you delete a permission, it'll be removed from all the roles associated to this permission and all the users who were granted this permission. Before deleting it, make sure you don't need it anymore in your application.

## Roles

The second item in the menu is the roles page, showing you a list of all your roles.

![Roles from admin dashboard](/assets/images/admin-roles.png)

### Create a new role

You can create a new role by clicking the **Create Role** button. A modal will open where you'll be able to input its name, if it's granted by default and its list of associated permissions.

![Create role from admin dashboard](/assets/images/admin-roles-create.png)

### Edit an existing role

If you click on one of the role in the list, you'll see its details on the right. You'll be able to edit its name, granted by default option and associated permissions.

![Edit role from admin dashboard](/assets/images/admin-roles-edit.png)

!!! tip "Permissions are automatically propagated to users with this role"
    If you add or remove a permission from a role, the permissions of the users having this role will also be updated accordingly.

### Delete a role

If one of your role is not useful anymore, you can delete it by clicking on it on the list and click on the **Delete** button on the right.

![Delete role from admin dashboard](/assets/images/admin-roles-delete.png)

!!! danger "The role will be removed from all the associated users"
    When you delete a role, it'll be removed from all the users who were granted this role. Before deleting it, make sure you don't need it anymore in your application.

### Granted by default

When you mark a role as **Granted by default**, it'll be automatically assigned to new users upon their registration. It's especially useful if you need your users to be able to perform basic actions directly on signup.
