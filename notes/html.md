---
title: HTML
layout: page
exclude: true
---
## Forms
You can **hide a form `input` by setting its `type` to `"hidden"`**. It's data will then still be sent when the form is submitted but the user will not be able to directly interact with it.
```html
<input type="hidden"  id="custId"  name="custId"  value="3487">
```

**Empty form fields will not appear in request data body once `submit`ted**, they will be entirely absent from the `params` or whatever object is used to communicate user data to the server. This means that it is possible when needed to have elements of user submission come through as empty strings or `null` values to be acted upon.

To **create a hidden field** for a password that does not display what the user is typing. Use an `input` with `type="password"`.
```html
<input typ="password">
```

To **create a text box that can be resized and typed into** use the `textarea` tags within a form. This also takes an argument `rows` that sets the default height of the text box when first created.
```html

```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzM0MjgyMDIxXX0=
-->