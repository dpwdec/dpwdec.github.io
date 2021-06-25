---
title: Files
layout: page
exclude: true
---

You can **read in a file as a string** in a concise (but not necessarily error immune method) using `unwrap` and `to_string` methods along with the `fs` module.
```rust
use std::fs;

fn main() {
    let file_string = fs::read_to_string("./path/to/file.txt").unwrap().to_string();
}
```