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

jQuery comes with a host of built in event functions on its selector function. These can be used to **add single events** to HTML elements that are triggered when the event happens. The second argument of these functions is a function that will be executed when the event happens. The code below 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg1MTU0NjM4MywxOTgwNzY3NTM3LDExNT
c3NDM0MzRdfQ==
-->