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

// mutate outside vec by entirely replacing an entry
x[0] = vec![7, 8, 9]; // => [[7, 8, 9], [4, 5, 6]]

// mutate an inner vec by changing an entry

x[1][2] = 1; // [[7, 8, 9], [4, 5, 1]]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1Mzk4MTcxN119
-->