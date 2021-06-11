---
title: Strum
layout: page
exclude: true
---

Strum is a library that offers a range of utilities relating enums.

You can 

You can **enumerate all variants of an enum** by using the `EnumIter` strum macro to derive the enumeration function and the `IntoEnumIterator` import to actually use the enumeration functionality. This will require the `strum` and `strum_macros` crates.
```rust
use strum::IntoEnumIterator;
use strum_macros::{EnumIter}

#[derive(EnumIter)]
pub enum HttpMethod {
  Get,
  Put,
  Post,
  // etc.
}

fn main() {
  for method in HttpMethod::iter() {
    // iterate all methods
  }
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM5ODk4OTU3Ml19
-->