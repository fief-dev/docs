# Themes

Fief comes with its own authentication pages for login, registration and reset password. You can customize them so they match the brand of your application. This is done through a system of **themes**. They can either be set globally, which is the most common case, or you can assign them to a specific [tenant](../tenants.md) if you need to customize the look-and-feel per tenant.

When your instance is created, Fief will always create a **Default** theme.

![Themes from admin dashboard](/assets/images/admin-themes.png)

## Create a new theme

You can create a new theme by clicking the **Create Theme** button. A modal will open where you'll be able to input its name. You'll then be taken to the [theme edition page](#edit-an-existing-theme).

![Create theme from admin dashboard](/assets/images/admin-themes-create.png)

## Set as default

Unless specified otherwise, [tenants](../tenants.md) will use the theme specified as default. To change the default theme, click on the **Set as default** button in front of the theme you want to make default.

![Create theme from admin dashboard](/assets/images/admin-themes-set-default.png)

## Edit an existing theme

You can edit an existing theme by clicking on the **Update** button in its row. An editor will open, with the customization parameters on the left and a preview on the right.

![Edit theme from admin dashboard](/assets/images/admin-themes-edit.png)

You can switch the page to preview using the select menu above the preview.

![Switch theme preview from admin dashboard](/assets/images/admin-themes-switch-preview.png)

## Customization parameters

You'll find below a description of the customizable parameters and what is their effect.

### Themes's name

This is the name of the theme. It won't be shown to the end-user, it's just a way for you to easily identify them.

### Primary colors

Primary colors correspond to the colors of the buttons, links and form focus borders. This is usually your "brand color".

<figure markdown>
  ![Theme primary color](/assets/images/admin-themes-primary.png)
  <figcaption>Primary color</figcaption>
</figure>

<figure markdown>
  ![Theme primary hover color](/assets/images/admin-themes-primary-hover.png)
  <figcaption>Hover primary color</figcaption>
</figure>

<figure markdown>
  ![Theme primary light color](/assets/images/admin-themes-primary-light.png)
  <figcaption>Light primary color</figcaption>
</figure>

### Form input colors

Form input colors respectively control the color of the text and the background of the form inputs.

<figure markdown>
  ![Form input colors](/assets/images/admin-themes-form-inputs.png)
  <figcaption>Form inputs colors</figcaption>
</figure>

### Light colors

Light colors control the color of the borders, in particular the ones on form inputs.

<figure markdown>
  ![Theme light color](/assets/images/admin-themes-light.png)
  <figcaption>Light color</figcaption>
</figure>

<figure markdown>
  ![Theme light hover color](/assets/images/admin-themes-light-hover.png)
  <figcaption>Hover light color</figcaption>
</figure>

### Text colors

Text colors control the color of the content and headings.

<figure markdown>
  ![Text color](/assets/images/admin-themes-text.png)
  <figcaption>Text color</figcaption>
</figure>

<figure markdown>
  ![Accent text color](/assets/images/admin-themes-text-accent.png)
  <figcaption>Accent text color</figcaption>
</figure>

### Background color

Background color control the color of the whole background.

<figure markdown>
  ![Backgroud color](/assets/images/admin-themes-background.png)
  <figcaption>Background color</figcaption>
</figure>

### Fonts

There are three parameters to control the fonts:

* Base font size: base size of the text, in `px`. Other font sizes (like headings) are proportional to this size.
* Font family: the font to use. It should be a valid [CSS `font-family` property](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family).
* CSS font URL: allows you to import custom fonts, like the ones from [Google Fonts](https://fonts.google.com/). The URL should point to a valid CSS file with `@font-face` instructions.

The example below shows you the result with `14`, `'Merriweather', serif`, `https://fonts.googleapis.com/css2?family=Merriweather&display=swap`:

![Fonts](/assets/images/admin-themes-fonts.png)
