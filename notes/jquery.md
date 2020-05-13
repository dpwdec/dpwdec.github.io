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

You can **execute jQuery code when your user first loads a page** by placing it in the `ready` block.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU0MDA1NDUyMSwxOTgwNzY3NTM3LDExNT
c3NDM0MzRdfQ==
-->