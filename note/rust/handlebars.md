---
title: Handlebars
layout: page
exclude: true
---

## Helpers

Rust's `Handlebars` library has a range of built in helpers.

You can **create an IF statement for multiple OR conditions** using the `or` and `eq` helpers.
```handlebars
{{ #if or( eq(true) eq(false)) }}
true + false = true
{{ /if }}

{{ #if or( eq(true) eq(true)) }}
true + true = true
{{ /if }}

{{ #if or( eq(true) eq(true)) }}
false + false = true
{{ /if }}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjk3NDY2NDEwXX0=
-->