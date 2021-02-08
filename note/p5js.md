---
title: p5.js
layout: page
exclude: true
---
p5.js is a javascript implementation of the processing graphics library optimised to run in the browser. The p5.js implementation also contains support for creating a manipulating DOM elements.

## Embedding

The simplest way to **embed a p5 sketch file in another web page** is it simply list it in a `<script>` tag inside the your main `HTML` file along with the P5.js library. However, doing this **does not allow you to control where the sketch appears on your page**.
```html
<script src="p5.js"></script>
<script src="mySkethch.js"></script>
```

You can **add a sketch to a div on a page** to more easily position it, using the `p5` constructor with the element that the sketch should appear in as an argument. The sketch will 

You can also embed some html page with a sketch in via iFrame

## Dom Elements

P5 supports a range of DOM elements that can be generated on and inserted into the same page as your sketch and then used by your sketch for creating interactive interface elements. By **default, new DOM elements are created *below* your sketch**. Creating elements using the P5 framework inside the sketch code gives you easy access to the dom elements allowing you retrieve data from and interact with them easily. P5 DOM only works with `>1.0.0` versions of the library.

You can **create a slider element** using the `createSlider()` function. 
```js
mySlider = createSlider();
```

You can **get the value inside a slider** using the `value()` function which show the current value of the slider as it appears on the page. The slider runs at a range of `0` to `100` and starts at `50`.
```js
mySlider.value(); // => 50
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM0NDkxNjYzMSwtMTA1MTY2OTk1MywtMT
Y5Njk5NzM5MiwxNTI0MTk3MzkxLC02MDAwNzExNTZdfQ==
-->