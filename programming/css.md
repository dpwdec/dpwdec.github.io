---
title: CSS
layout: page
exclude: true
---

## Alignment

You can **put two `div`s on the same line** using the `float` css indicator. In the example below, `div`s with the `id="same-line"` will float next to each other rather than being separated by a line break.
```css
#same-line {
  float: left;
}
```

You can **form a `div` onto a new line** using the `clear` indicator. `Div`s with the `id="new-line"` from the example below will be pushed down onto a new line away from any `float`ing counterparts.
```css
#new-line {
  clear: left
}
```

You can **horizontally centre a div** by setting `margin` to `auto`.
```css
div {
  margin: auto
}
```

You can **space HTML elements using white space** by adding the `pre` tag to the `white-space` property. By default **white space is collapsed by HTML displays** so you cannot easily space elements using a white space.
```css
p {
  white-space: pre;
}
```

## before / after

You can **add text content to a `before` / `after` relative tags** by enclosing the `content` inside `""` quote marks. If you don't include the content inside quote marks it will not be parsed as valid css.
```css
p::before {
  content: "some text"
}
```

## Subsequent Sibling Selector, or the ~ Tilde

The **subsequent sibling selector** allows you to **select subsequent elements** on a page **relative to another element** *IF* they **share the same parent element**. In the example below, the `p` element text before the `x` class line is not styled but the two elements after it *are* styled. Furthermore, the last element inside a `div` - which gives it a different parent from the `x` class element - is ignored.

<p class="codepen" data-height="265" data-theme-id="light" data-default-tab="css,result" data-user="dkowski" data-slug-hash="abJxZMx" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Tilde CSS selector example">
  <span>See the Pen <a href="https://codepen.io/dkowski/pen/abJxZMx">
  Tilde CSS selector example</a> by Dkowski (<a href="https://codepen.io/dkowski">@dkowski</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

## Checkbox

You can **alter the styling of an elements based on the state of a checkbox that is associated with it** by using the `:checked` (and unchecked or default) property of the `input[type="checkbox"]`. An easy way to do this is to use the subsequent sibling selector `~` tilde character to target specific elements around an input that share the same parent thus linking them.
```css
input[type="checkbox"]:checked ~ p {
  color: blue
}
```

In the example below the default version of the `input` element is used to style the `p` element when it is unchecked and the `:checked` element is used to style it when toggled on.

<p class="codepen" data-height="265" data-theme-id="light" data-default-tab="css,result" data-user="dkowski" data-slug-hash="LYWvYMP" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Checkbox association">
  <span>See the Pen <a href="https://codepen.io/dkowski/pen/LYWvYMP">
  Checkbox association</a> by Dkowski (<a href="https://codepen.io/dkowski">@dkowski</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNTc3MTEyMTUsMTcyMTI2NDA4NCw3MT
AwNDM0NjksMjAyMDgxNzc4OCwtMTg1MTEwMzc3MCwtNDcwMjc1
NTk4XX0=
-->