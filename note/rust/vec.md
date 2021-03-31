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
let mut y = [1, 2, 2, 3];
y,d
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQ4NTQ0NTA0LC0xMDU4Mjk2NjRdfQ==
-->