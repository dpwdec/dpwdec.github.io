---
title: Itertools
layout: page
exclude: true
---

You can **zip together an arbitrary number of arrays** using the `!izip` macro.
```rust
// code provided by Bluss
use itertools::izip;

fn main() {
  let a = [1, 2, 3];
  let b = [4, 5, 6];
  let c = [7, 8, 9];

  for (x, y, z) in izip!(&a, &b, &c) {
  }
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTkwMTEzMjZdfQ==
-->