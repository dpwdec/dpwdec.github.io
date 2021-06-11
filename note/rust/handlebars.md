---
title: Handlebars
layout: page
exclude: true
---

## Helpers

Rust's `Handlebars` library has a range of built in helpers.

You can **create an IF statement for multiple OR conditions** using the `or` and `eq` helpers.
```handlebars
{{ #if or( eq(1 1) eq(2 1)) }}
true + false = true
{{ /if }}

{{ #if or( eq(1 1) eq(1 1)) }}
true + true = true
{{ /if }}

{{ #if or( eq(2 1) eq(2 1)) }}
false + false = true
{{ /if }}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNzA0MzYyOTRdfQ==
-->