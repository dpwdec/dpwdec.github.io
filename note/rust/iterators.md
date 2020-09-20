---
title: Rust: Iterators
layout: page
exclude: true
---

## Functions that Return Iterators

You can **return an iterator from a function** by directly returning the structure the structure that an iterators yields.
```rust
fn return_split(word: &str) -> 
```

You can **return an iterator from a function in a more readable way** by using the `impl Iterator` syntax. This essentially just dynamically replaces itself with the actually return type above but allows you to specify the iterator return as a generalised 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA4NjcwODMwLC03MTYwNTUwNjJdfQ==
-->