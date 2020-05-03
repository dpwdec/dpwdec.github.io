---
title: HTML
layout: page
exclude: true
---
## Forms
You can **hide a form `input` by setting its `type` to `"hidden"`**. It's data will then still be sent when the form is submitted but the user will not be able to directly interact with it.
``

**Empty form fields will not appear in request data body once `submit`ted**, they will be entirely absent from the `params` or whatever object is used to communicate user data to the server. This means that it is possible when needed to have elements of user submission come through as empty strings or `null` values to be acted upon.
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMwODE3MDg5MF19
-->