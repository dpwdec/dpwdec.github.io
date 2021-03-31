---
title: Bool
layout: page
exclude: true
---

You can **return a `Option` from a boolean function** by using the `then` method on the bool that is returned. This return the result of the computation inside the `then` closure as an option *if* the bool was `true` otherwise it will return a `None`.
```rust
let x = vec![1, 2, 3];
let y = vec::new();
x.is_empty.then(|| "Empty)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI5MDUwNTI4LC0xNjg3MDE0NjQxXX0=
-->