---
title: Vec
layout: page
exclude: true
---

The `vec` method `dedup` *does not* remove all duplicates from an array, it **only removes consecutive duplicate elements**.
```rust
// no change
let mut x = [1, 2, 3, 2];
x.dedup(); // => [1, 2, 3, 2]
// removes consecutives
let mut y = [1, 2, 2, 3];
y,dedup(); // => [1, 2, 3]
```

You can **remove all duplicate elements in an array REGARDLESS of position** by using the `unique()` method on `vec`.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNjA5OTc5MDgsLTEwNTgyOTY2NF19
-->