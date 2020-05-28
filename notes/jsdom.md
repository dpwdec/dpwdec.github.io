---
title: Javascript DOM
layout: page
exclude: true
---

## Creating

You can **create an HTML element on a page** by using the `document` method `createElement` which creates the HTML element as a javascript object and then appending it to the displayed page `body` after its creation using the `appendChild` method. This **must also be done after the <body> of the page is loaded** using the `onload` method so that the `body` skeleton has been loaded and created before the Javascript which creates and adds element runs. 
```js
document.body.onload = addElement // => waits until <body> of HTML has loaded
function addElement() {
	var pElement = document.createElement('p')
	document.body.appendChild(pElement)
}
```

You can **add HTML attributes to Javascript created elements** using the `setAttribute` method. This can essential target an valid HTML attribute that a value could hold.
```js
// setting id and class for a text element
var pElement = document.createElement('p')
pElement.setAttribute('id', 'text-0')
pElement.setAttribute('class', 'para-class')

// setting value and type for a form input element
var inuputElement = document.createElement('input')
inputElement.setAttribute('type', 'text')
inputElement.setAttribute('value', 'hello')

// setting a links value
var linkElement = document.createElement('a')
linkElement.setAttribute('href' 'www.somewebsite.com')
```

You can use the `appendChild` on a range of HTML elements to **create composite HTML elements** before appending them to the top level page. In the example below a <div> is created and a <form> is added to it followed by two input elements added to the form. The <div> is then added to the entire the `document.body` which also adds all the children that were appended to it.
```js
var divElement = document.createElement('div')
var formElement = document.createElement('form')
formElement.setAttribute('method', 'post')
formElement.setAttribute('action', '/user')
divElement.appendChild(formElement)

// create input elements
var textInput = document.createElement('input')
textInput.setAttribute('type', 'text')
textInput.setAttribute('placeholder', 'enter information')
formElement.appendChild(textInput)
var submitInput = document.createElement('input')
submitInput.setAttribute('type', 'submit')
submitInput.setAttribute('submit', 'Save Information')

// append div to the top level document with all the content
document.body.appendChild(divElement)
```

### Loading

There are several different ways you can trigger events once a page has loaded which will depend on your needs. As mentioned above, to trigger an event once the `body` of an HTML document is loaded use the `document.body.onload` method.

To **trigger events once the entirety of page is loaded**, including all images, videos, other content etc. Use the `window.onload` method. This is also the most widely supported load method.

To **trigger events once the DOM has loaded**, i.e. when all the page skeleton has loaded but not necessarily all the content that fills those DOM elements, use the `document.onload` method. However, **this method is not very stable** can often not fire at all due to its lack of support.

## Targeting

You can **select an element on a page by its `id`** using the `document` method `getElementById` which takes an argument that corresponds to that element's `id` HTML property and returns it as an object.
```js
var someDOMElement = document.getElementByID('some-id')
```

You can **return a list of an element's child elements** by using the `children` method on a target HTML element.
```js
var listOfChildElements = document.getElementByID('some-id').children
for(i = 0; i < listOfChildElements.length; i++) {
  var childElement = listOfChildElements[i]
  // do something with the targeted element here
}
```

You can 

## Retrieving / Setting Content

You can **get and set the text value normal page text elements**, such as <p>, <h1>, <h2> etc. by using the `innerHTML` property.
```js
// return element's text
var elementText = document.getElementById('text-id').innerHTML
// set element's text
document.getElementById('text-id').innerHTML = 'hello'
```

You can **get the text value from an <input> element in a <form>** use the `value` property after targeting the element. This method is also used for **getting the text value from an <textarea>**.
```js
// return element's text
var inputElementText = document.getElementById('some-id').value
// set element's text
document.getElementById('some-id').value = 'hello'
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MTkyNTg4ODgsLTE1ODU1MTQ2NDcsMz
Q2MjE0Mzk2XX0=
-->