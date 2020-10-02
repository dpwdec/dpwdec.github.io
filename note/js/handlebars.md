---
title: Handlebars
layout: page
exclude: true
---

You can **create a handlebars helper that resolves a template to a value** by using the `registerHelper` function with the first argument describing the template value to match to the second argument the value to be resolved to. When handlebars processes `{{myValue}}` in a file it will output `0`.
```js
registerHelper('myValue', 0)
```

You can **ensure that a string is safe** by using the `SafeString` function.
```js
new Handlebars.SafeString("<div>HTML content!</div>");
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NTkzNjY4ODZdfQ==
-->