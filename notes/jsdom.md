---
title: Javascript DOM
layout: page
exclude: true
---

## Creating

You can **create an HTML element on a page** by using the `document` method `createElement` which creates the HTML element as a javascript object and then appending it to the displayed page `body` after its creation using the `appendChild` method. This **must also be done after the page is loaded** using the `onload` method so that the `body` skeleton has been loaded and created before the Javascript which creates and adds element runs. 
```js
document.body.onload = addElement
function addElement() {
var pElement = document.createElement('p')
document.body.appendChild(pElement)
```

## Targeting

You can **select an element on a page by its `id`** using the `document` method `getElementById` which takes an argument that corresponds to that element's `id` HTML property and returns it as an object.
```js
var someDOMElement = document.getElementByID('some-id')
```

## Retrieving Content

You can **get the text value normal page text elements**, such as <p>, <h1>, <h2> etc. by using the `innerHTML` property.
```js
var elementText = document.getElementById('text-id').innerHTML
```

You can **get the text value from an <input> element in a <form>** use the `value` property after targeting the element. This method is also used for **getting the text value from an <textarea>**.
```js
var inputElementText = document.getElementById('some-id').value
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMxMDQ2NDk0NCwzNDYyMTQzOTZdfQ==
-->