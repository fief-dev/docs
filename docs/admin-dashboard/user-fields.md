# User fields

This is where you'll see and manage the custom user fields of your workspace.

--8<-- "reusables/user-field-callout.md"

![User fields from admin dashboard](/assets/images/admin-user-fields.png)

## Create a new user field

You can create a new client by clicking the **Create User field** button. A modal will open where you'll be able to input its different properties.

![Create user field from admin dashboard](/assets/images/admin-user-fields-create.png)

## Edit an existing user field

If you click on one of the user field in the list, you'll see its details on the right and be able to change its properties.

![Edit user field from admin dashboard](/assets/images/admin-user-fields-edit.png)

## Delete an existing user field

If one of your user field is not useful anymore, you can delete it: click on the user field you want to delete in the list and click on the **Delete** button.

![Delete user field from admin dashboard](/assets/images/admin-user-fields-delete.png)

!!! danger "Associated user values will be deleted as well"
    When you delete a user field, the **associated data on the user will also be deleted**. Make sure you don't need this information anymore or that you saved it somewhere else before proceeding.

## User field properties

User fields can be configured through their properties.

### Name

This is the name of your user field. It'll be used as **label in the registration form** and in the **admin dashboard**.

### Slug

This will be the **identifier of the field** in the [ID token](../getting-started/oauth2.md#access-token-and-id-token) and in API responses.

By default, it'll be automatically generated from the [name](#name), but you can customize it at will.

!!! tip "The slug is unique in a workspace"
    Each field should have a unique identifier. If you try to create a new user field with a slug that already exists, an error will be raised.

### Type

This is probably the most important setting for your user field. It'll determine the **type of data you want to store**. We currently support n types:

#### String

Common type for textual values. Examples:

* A first or last name
* A company name
* A tagline

It'll be shown as a simple text input in forms.

#### Integer

Type to store integer values. Examples:

* A reputation score
* An height
* An age

It'll be shown as a numeric input in forms.

#### Boolean

Type to store boolean values. Examples:

* Subscription status to a newsletter
* Terms consent
* A validation status

It'll be shown as a checkbox in forms.

#### Choice

Type accepting a predefined set of values. Examples:

* A gender
* A job sector
* A level of experience

When selecting this type, you'll be able to configure the allowed choices.

![Create choice user field from admin dashboard](/assets/images/admin-user-fields-create-choice.png)

Each choice consists of two things: the **value** (`A`), which is the actual underlying value that will be stored in database and returned in the user data, and the **label** (`Choice A`) which will be used to show a user-friendly label in forms and the admin dashboard.

It'll be shown as a select menu in forms.

#### Phone number

Type that'll validate if the value is a valid phone number. It shall be formatted with the international country code, `+331020405`.

It'll be shown as a text input in forms.

#### Address

Type that'll display several inputs to validate a full postal address.

![Address user field input](/assets/images/user-fields-address-input.png)

#### Timezone

Type that'll display a list of valid timezones.

### Default

For some types, you can define a **default value**.

If the field is shown in a form, the field will automatically be pre-filled with this value.

If the field is not presented in a form, this value will be automatically assigned to new users when they register.

### Ask at registration

If checked, the user field will be presented in the **user registration form**.

### Ask at update

If checked, the user will be able to update its value through the `/profile` API.

!!! tip "Private field"
    In some cases, you need values that can't be set by the user, e.g., an onboarding status or a reputation score.

    To do this, you can simply uncheck both **Ask at registration** and **Ask at update** field.

    You'll always be able to update this value through the admin dashboard or the Admin API.

### Required

If checked, the value will have to be filled when presented in forms.

!!! tip "Required boolean field"
    You can set a user field of type [Boolean](#boolean) as **required**. In this case, the value **must be True**.

    It can be useful for consent checkbox where you need the user to accept the terms before creating its account.
