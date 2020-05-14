---
title: jQuery
layout: page
exclude: true
---
jQuery is a javascript library used for making selecting HTML elements and triggering events easier.

## Selectors

You can select different HTML elements using the `$(select).acton()` syntax, where the `selector` describes some sort of accessor to a page element.
```js
$('p').hide(); // hide all <p> elements
$('.test').hide(); // hide all elements with class of 'test'
$('#test').hide(); // hide all elements with id of 'test'
```

The **`this` selector to whatever element is currently selected**. The example below creates an alert with the text of the element with `id="add"`. The `this` refers to that element because the entire code is inside a `$(#add)` at the top level.
```js
$('#add').on('click', function() {
  alert($(this).text());
});
```

You can **get the text from an <input> element** by using the `val` function with your selector. The example below assumes the page has an <input> element with an `id="my-input-elemt"`. The `val` function will take whatever is currently inside that element when it is executed.
```js
$('#my-input-elemt').val();
```

## Events

### Document Ready

You can **execute jQuery code when your user first loads a page** by placing it in the `ready` block. Technically you can make jQuery execute at any time from when the user loads the page, however, using the `ready` block means that your jQuery code will only run once all elements on the page have successfully loaded meaning that you won't run into so many errors with your code.
```js
$(document).ready(function(){  
  // jQuery code to run on start up here
});
```

There is also a **shorter version of the `ready` function** that you can user to make your code briefer.
```js
$(function() {
  // jQuery code to run on start up here
});
```

### User Events

jQuery comes with a host of built in event functions on its selector function. These can be used to **add single events** to HTML elements that are triggered when the event happens. The argument of these functions is a function that will be executed when the event happens. The code below shows an alert **when the <h1> element is clicked**.
```js
$('h1').click(function() {
  alert('you clicked a heading!');
});
```

There is a **more generalised jQuery event handler** in the form of the `on` method. This allows you to specify the name of the event as the first argument of the method and the function to be executed as the second argument.
```js
$('h1').on('click', function() {
  alert('you clicked a heading!');
});
```

You can use the `on` method to **add multiple events to a single object** by submitting an object to the `on` method with properties named after events that you want to execute bound to the functions you want to execute when those functions are registered. In the code below by naming our object properties `mouseenter`, `mouseleave` and `click` we can bind functions to these events for `h1` elements.
```js
$('h1').on({
  mouseenter: function() {
    $(this).css('background-color', 'blue');
  },
  mouseleave: function() {
    $(this).css('background-color', 'white');
  },
  click: function() {
    alert('you clicked a heading!');
  }
});
```

## Ajax

jQuery has **support for sending dynamic AJAX based server requests** with its `get`, `post` and `load` methods.

### get

The `get` function **sends a `GET` request to a server extension**.  It follows the basic pattern of:
```js
$.get(url, callback);
```
It takes two arguments, a `url` and a `callback`. The `callback` itself takes two arguments, the `data` from the request and a `status` code. The `data` and `status` arguments of the callback can be called whatever you want, such as `response`, or `txt`. The `data` argument is simply filled with whatever the return is from the controller route at the `url` which the `get` request goes to.
```js
$.get('/url', function(data, status) {
  // use the data here in some way
});
```

### post

The `post` function **sends a `POST` request to a server extension**. It follows the basic pattern of:
```js
$.post(url, data, callback);
```

It is essentially the same as the `get` function except it takes an additional, second argument which is a javascript object (dictionary) that contains key value pairs that will populate whatever your server framework's object for returning parameters is.
```js
$.post('/url',
{
  name: 'Jason',
  age: 41
},
function(data, status) {
  // use the response data from the post request in some way
});
```

### ajax

You can **write arbitrary ajax requests** using the `ajax` method. This method can have many different forms, but the simplest takes an object that defines different parameters for the request as key value pairs. In the example below the `success` key points to a function that will be run when the `ajax` server request returns successfully. This also has optional `result` argument that will contain the result from the server.
```js
$.ajax({
  url: '/url',
  method: 'GET',
  success: function(result) {
    // do something with the result
  }
});
```

You can also **send data in a `POST` request** by using the `data property with an object holding the data.
```js
$.ajax({
  url: '/url',
  method: 'POST',
  data: { name: 'Jason', age: 41 },
  success: function(result) {
    // do something with the result
  }
});
```

You can **extract the `success` field into a separate method call** by chaining it with the `done` method.
```js
$.ajax({
  url: '/url',
  method: 'POST',
  data: { name: 'Jason', age: 41 },
}).done(function(result) {
  // do something with the result
});
```

You can **handle fail states for your ajax requests** by appending the `fail` method to the chain of method handlers. There doesn't seem to be support from within the key value pair object syntax shown above that `success` has for failure states.
```js
$.ajax({
  url: '/url',
  method: 'POST',
  data: { name: 'Jason', age: 41 },
}).done(function(result) {
  // do something with the result
}).fail(function() {
  // do something when request fails
});
```

You can **write code that ALWAYS executes after an ajax request** whether it succeeded or failed by appending the `always` method to the chain of method handlers.
```js
$.ajax({
  url: '/url',
  method: 'POST',
  data: { name: 'Jason', age: 41 },
}).done(function(result) {
  // do something with the result
}).fail(function() {
  // do something when request fails
}).always(function() {
  // this code always runs
});
```

Using arbitrary ajax requests allows you to **send RESTful HTTP requests to your server** with methods like `PATCH`, `PUT` and `
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI1NDAxMzk1OCwtMTU0MzQ0Nzk1MSwxNz
Q5NDU3MzUyLDg4OTA3MjQ0OCwxNzU4MjUzNjkxLC0xMDYwNjQz
NSwxOTgwNzY3NTM3LDExNTc3NDM0MzRdfQ==
-->