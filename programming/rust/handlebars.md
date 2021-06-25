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

You can find a **list of other available rust handlebars helpers** [here](https://docs.rs/handlebars/4.0.1/handlebars/#built-in-helpers).