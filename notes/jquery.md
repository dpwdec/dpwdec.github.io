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
  
);
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NDAzOTA4MTYsMTk4MDc2NzUzNywxMT
U3NzQzNDM0XX0=
-->