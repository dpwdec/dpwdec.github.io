---
title: Handlebars
layout: page
exclude: true
---

You can **achieve basic templating with a dictionary of values in handlebars** by running a `compile` on a handlebars template and then passing a dictionary of values to fill in to the `template`.
```js
const  template  = Handlebars.compile("My name is {{ name }} and my age is {{ age }}.")
const  result  =  template({ name:  "Roberto", age: 3 })
// => My name is Roberto and my age is 3.
```

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
registerHelper('myValue', () => 0)
```

You can **pass a value directly into a helper that takes an argument** by surrounding the argument within the handlebars template with `""` quotes.
```js
Handlebars.registerHelper('foo', x => x.toUpperCase())
let source = '{{foo "Belinda"}}'
let template = Handlebars.compile(source)
template({}) // => BELINDA
```

You can **pass the result of a templated value into a helper** by space separating the arguments to the helper.
```js
Handlebars.registerHelper('foo', x => x.toUpperCase())
let source = '{{foo name}}'
let data = {"name": "Tempestua"}
let template = Handlebars.compile(source)
template(data) // => 'TEMPESTUA'
```

You can **nest helpers** by enclosing the helper return types that are arguments for other helpers in `()` brackets. The brackets will not be rendered.
```js
Handlebars.registerHelper('foo', x => x.toUpperCase())
Handlebars.registerHelper('bar', () => 'hello')
let source = '{{foo (bar)}}'
let data = {}
let template = Handlebars.compile(source)
template(data); // => HELLO
```

Extra helpers added into the template block that do not explicitly cause arguments will be ignored.

## Utilities

You can **ensure that a string is safe** by using the `SafeString` function.
```js
new Handlebars.SafeString("<div>HTML content!</div>");
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgzODI5MTEyMSwtMjAyOTg4NDE5MSwzOT
Q0MTQ1ODUsLTY5OTgxNTQ0LC02ODE4NjMyODIsMjAwOTExMDIw
MywxODk4Mzg2NjAsMTE0OTI4OTM4LC0zOTI0MzkyMjUsNjAwMz
Q4NjkwLC0xODU5MzY2ODg2XX0=
-->