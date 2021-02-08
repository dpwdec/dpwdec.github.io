---
title: Embedding
layout: page
exclude: true
---

## Direct Embedding

The simplest way to **embed a p5 sketch file in another web page** is it simply list it in a `<script>` tag inside the your main `HTML` file along with the P5.js library. However, doing this **does not allow you to control where the sketch appears on your page**.
```html
<script src="p5.js"></script>
<script src="mySketch.js"></script>
```

## Parenting

You can **embed elements created in p5 to HTML elements on the page** using the `parent` function which takes the `id` of a container element on the page as its argument. This solution is ok, but it can get messy with multiple containers and multiple sketches that clash and cause issues.
```js

```

## Embedding with Div

You can **add a sketch to a div on a page** to more easily position it, using the `p5` constructor with the element that the sketch should appear in as an argument. The sketch will also need to be written as an encapsulated function that contains an argument from which the sketch elements are created. In the example below, `mySketch` loads the sketch code and then the call in the `<script>` tag at the bottom of the page initialises the sketch inside the `div` container.
```html
<head>
  <script src="p5.js"></script>
  <script src="mySketch.js"></script>
</head>
<body>
  <div id="container"></div>
  <script>
    new p5(sketch, 'container')
  </script>
</body>
```

The corresponding sketch file would then be in the format as below with the `p` argument to the `sketch` function containing the processing specific functions.
```js
let sketch = function(p) {
 
  p.setup = function(){
    p.createCanvas(100, 100);
    p.background(0);
  }

  p.draw = function() {
    ellipse(mouseX, mouseY, 20, 20);
  }
};
```

This solution is ok, but it can get messy with multiple containers and multiple sketches that clash and cause issues. It also means version controlling sketch code in an awkward and verbose format.

## Embedding with iframe

Another easy way to **embed processing sketches on web pages AND control their positioning** is to use an `<iframe>` element which can just simple page from the first processing embedding example above but *inside* an iframe element, the position of which is controllable. The `height` and `width` of the `<iframe>` should be set to match the sketches dimensions or be slightly bigger so it can be easily displayed.
```html
<body>
  <iframe width="600" height="600" frameBorder="0" srcdoc="
    <head>
      <script src='cdn.p5.js'></script>
      <script src='cdn.sketch.js'></script>
    </head>">
  </iframe>
</body>
```

I also use the `srcdoc` property of the `<iframe>` element for the html page as loading in *extra* HTML from a remote source to an `<iframe>` is sometimes seen as a risk by browsers and blocked so you might run into issues otherwise. You *can* embed the sketch code directly into the `srcdoc` as well, but I prefer to load the sketch code and p5.js library from a CDN, such as jsdelivr. This allows you to source control your sketch code in a separate project and maintain a separation of concerns while easily updating page content.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MTYwNjMyNTZdfQ==
-->