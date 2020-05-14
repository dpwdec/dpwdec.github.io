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

## 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc1ODI1MzY5MSwtMTA2MDY0MzUsMTk4MD
c2NzUzNywxMTU3NzQzNDM0XX0=
-->