---
title: Handlebars
layout: page
exclude: true
---

You **cannot put too templated values next to each other within the same template block**.
```js
let template = '{{key value}}' // => NOT VALID
```

You **can

You **can only have one helper per template block**. Any extra helpers added into the template block will just be ignored after that helper has executed.

You can **create a handlebars helper that resolves a template to a value** by using the `registerHelper` function with the first argument describing the template value to match to the second argument the value to be resolved to. When handlebars processes `{{myValue}}` in a file it will output `0`.
```js
registerHelper('myValue', 0)
```

It seems like you can nest handlebars commands.

You can **ensure that a string is safe** by using the `SafeString` function.
```js
new Handlebars.SafeString("<div>HTML content!</div>");
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE0OTI4OTM4LC0zOTI0MzkyMjUsNjAwMz
Q4NjkwLC0xODU5MzY2ODg2XX0=
-->