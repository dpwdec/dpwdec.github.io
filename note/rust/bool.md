---
title: Bool
layout: page
exclude: true
---

The `bool` type supports a range of functions that can be run in response to a boolean result from another function.

## Then

You can **return a `Option` from a boolean function** by using the `then` method on the bool that is returned. This return the result of the computation inside the `then` closure as an option *if* the bool was `true` otherwise it will return a `None`.
```rust
let x = true;
let y = false;
let r = x.then(|| "true!"); // => Some("true!")
let s = y.then(|| "false!"); // => None
```

## Not

You can **reverse the action done by a boolean** by using the `not` function from the `std::ops::{Not}` library. This is useful if the structure only has a positive predicate method but you want to do something in the negative case only. For example, below we have a case where we want to do something if the `x` is *not* empty, however, the `vec` type only supports the `is_empty()` predicate method, so, with the `not` method we reverse this and can use `then` do return an `Option` structure over the reverse case of the the predicate.
```rust
let x = vec![1, 2, 3]
let y = x.is_empty().not().then(|| "Not empty"); // => Some("Not Empty")
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MjM1ODA3MDQsLTE2ODcwMTQ2NDFdfQ
==
-->