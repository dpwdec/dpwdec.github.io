---
title: Handlebars
layout: page
exclude: true
---

You can **create a handlebars helper that resolves a template to a value** by using the `registerHelper` function with the first argument describing the template value to match to the second argument the value to be resolved to.
```js
registerHelper('myValue', '0'
```

You can **ensure that a string is safe** by using the `SafeString` function.
```js
new Handlebars.SafeString("<div>HTML content!</div>");
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzM0MTk4MTEzXX0=
-->