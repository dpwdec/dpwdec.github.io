---
title: Handlebars
layout: page
exclude: true
---

You **cannot put too templated values next to each other within the same template block**.
```js
let template = '{{key value}}' // => NOT VALID
let template = '{{key}}{{value}}' // => VALID
```

You **can only have one helper per template block**. Any extra helpers added into the template block will just be ignored after that helper has executed.

You can **create a handlebars helper that resolves a template to a value** by using the `registerHelper` function with the first argument describing the template value to match to the second argument the value to be resolved to. When handlebars processes `{{myValue}}` in a file it will output `0`.
```js
registerHelper('myValue', 0)
```

You can **pass the result of a templated value into a helper** by space separating the arguments to the helper.
```js
Handlebars.registerHelper('foo', x => x.toUpperCase())
let source = '{{foo name}}'
let data = {"name": "
```

It seems like you can nest handlebars commands.

You can **ensure that a string is safe** by using the `SafeString` function.
```js
new Handlebars.SafeString("<div>HTML content!</div>");
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA3MzE3ODI4OCwxMTQ5Mjg5MzgsLTM5Mj
QzOTIyNSw2MDAzNDg2OTAsLTE4NTkzNjY4ODZdfQ==
-->