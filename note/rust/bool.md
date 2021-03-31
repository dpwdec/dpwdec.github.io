---
title: Bool
layout: page
exclude: true
---

The `bool` type supports a range of functions that

You can **return a `Option` from a boolean function** by using the `then` method on the bool that is returned. This return the result of the computation inside the `then` closure as an option *if* the bool was `true` otherwise it will return a `None`.
```rust
let x = true;
let y = false;
let r = x.then(|| "true!"); // => Some("true!")
let s = y.then(|| "false!"); // => None
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTY4MDQzMzU5LC0xNjg3MDE0NjQxXX0=
-->