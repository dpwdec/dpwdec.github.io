---
title: Javascript DOM
layout: page
exclude: true
---

## Targeting

You can **select an element on a page by its `id`** using the `document` method `getElementById` which takes an argument that corresponds to that element's `id` HTML property and returns it as an object.
```js
var someDOMElement = document.getElementByID('some-id')
```

You can **get the text value normal page text elements**, such as <p>, <h1>, <h2> etc. by using the `innerHTML` property.
```js
var elementText = document.getElementById('text-id').innerHTML
```

You can **get the value from an <input> element in a <form>** use the `value` property after targeting the element. This method is also used for **getting the text**
```js
var inputElementText = document.getElementById('some-id').value
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUwNzA2NjM3MSwzNDYyMTQzOTZdfQ==
-->