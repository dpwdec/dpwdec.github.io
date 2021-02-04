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
<textarea rows="3"></textarea>
```

## Internal Links
You can **link to internal elements in an HTML document** by using the `a` tag type in conjunction with an element's `id` and the name of the `id` with a `#` selector. In the example below, the `Link To Hello` link will take the browser window to the HTML element with an `id` equal to `a_heading`. These `id` selectors *are* case sensitive.
```html
<a href="#a_heading">Link to Hello</a>
<h1 id="a_heading">Hello</h1>
```

## IFrame

You can **remove the default drop shadow border around an `<iframe>` element** using the `frameBorder` property set to `0`.
```html
<iframe src="https://somewebsite.com" frameBorder="0"></iframe>
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMDY5ODEzNzIsLTExNjE4MDQzMzgsMT
EwODM5OTMwNywxNjMxOTYxOTY5LDczNDI4MjAyMV19
-->