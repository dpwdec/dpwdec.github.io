---
title: p5.js
layout: page
exclude: true
---
p5.js is a javascript implementation of the processing graphics library optimised to run in the browser. The p5.js implementation also contains support for creating a manipulating DOM elements.

## Embedding

The simplest way to **embed a p5 sketch file in another web page** is it simply list it in a `<script>` tag inside the your main `HTML` file. However, doing this **does not allow you to control where the sketch appears on your page**.
```html

```

You can also embed some html page with a sketch in via iFrame

## Dom Elements

P5 supports a range of DOM elements that can be generated on and inserted into the same page as your sketch and then used by your sketch for creating interactive interface elements. By **default, new DOM elements are created *below* your sketch**. Creating elements using the P5 framework inside the sketch code gives you easy access to the dom elements allowing you retrieve data from and interact with them easily.

You can **create a slider element** using the `createSlider()` function. 
```js
mySlider = createSlider();
```

You can **get the value inside a slider** using the `value()` function which show the current value of the slider as it appears on the page. The slider runs at a range of `0` to `100` and starts at `50`.
```js
mySlider.value(); // => 50
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjAzMDM1NzgwLC0xNjk2OTk3MzkyLDE1Mj
QxOTczOTEsLTYwMDA3MTE1Nl19
-->