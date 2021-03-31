---
title: Mutability
layout: page
exclude: true
---

If you mark a variable as `mut` that contains other nested structures, **all of the structures become mutable**. For example, if you mark a `vec` containing some `vec`s as `mut`able, *all* the contained `vec`s as well the containing `vec` become mutable.
```rust
let mut x = vec![
  vec![1, 2, 3],
  vec![4, 5, 6]
]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY5ODM2MjUxOF19
-->