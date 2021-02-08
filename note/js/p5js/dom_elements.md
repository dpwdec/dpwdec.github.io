---
title: DOM Elements
layout: page
exclude: true
---

The p5.js implementation also contains support for creating a manipulating DOM elements and virtually anything you can do to a webpage in vanilla javascript you can also do inside a p5.js sketch.

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
eyJoaXN0b3J5IjpbLTEyNjUzMjQ2NjNdfQ==
-->