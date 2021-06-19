---
title: Vec
layout: page
exclude: true
---

The `vec` method `dedup` *does not* remove all duplicates from an array, it **only removes consecutive duplicate elements**.
```rust
// no change
let mut x = vec![1, 2, 3, 2];
x.dedup(); // => [1, 2, 3, 2]
// removes consecutives
let mut y = vec![1, 2, 2, 3];
y,dedup(); // => [1, 2, 3]
```

You can **remove all duplicate elements in an array REGARDLESS of position** by using the `unique()` method on `vec`.

You can **destructively remove the nth element from a `vec`** by the converting the `vec` to an `iter` then using the `nth` function and `unwrap`ping the result. This moves and discards all the values from the original `vec` making it unusable.
```rust
let x = vec![1, 2, 3, 4]
x.into_iter().nth(1).unwrap() // => 2
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NzQ1NzU1MTksLTEwNTgyOTY2NF19
-->