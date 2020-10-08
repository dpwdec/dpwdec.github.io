---
title: Handlebars
layout: page
exclude: true
---

## Values

You **cannot put too templated values next to each other within the same template block**.
```js
let template = '{{key value}}' // => NOT VALID
let template = '{{key}}{{value}}' // => VALID
```

## Helpers

You can **create a handlebars helper that resolves a template to a value** by using the `registerHelper` function with the first argument describing the template value to match to the second argument the value to be resolved to. When handlebars processes `{{myValue}}` in a file it will output `0`. Using a helper that **returns a value directly** without calling a function **cannot be nested** with other helpers.
```js
registerHelper('myValue', 0)
```

You can also **create a helper that resolves to a single value without arguments** by using function syntax.
```js
regu
```

You can **pass the result of a templated value into a helper** by space separating the arguments to the helper.
```js
Handlebars.registerHelper('foo', x => x.toUpperCase())
let source = '{{foo name}}'
let data = {"name": "Tempestua"}
let template = Handlebars.compile(source)
template(data) // => 'TEMPESTUA'
```

Extra helpers added into the template block that do not explicitly cause arguments will be ignored.

It seems like you can nest handlebars commands.

## Utilities

You can **ensure that a string is safe** by using the `SafeString` function.
```js
new Handlebars.SafeString("<div>HTML content!</div>");
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMTU1NDc1MywxODk4Mzg2NjAsMTE0OT
I4OTM4LC0zOTI0MzkyMjUsNjAwMzQ4NjkwLC0xODU5MzY2ODg2
XX0=
-->