---
title: Strum
layout: page
exclude: true
---

Strum is a library that offers a range of utilities relating enums.

You can use strum to **deserialize an enum from a string representation** by using the `EnumString` trait with the `std::str::FromStr` method.
```rust
use strum_macros::EnumString;
use std::str::FromStr;

#[derive(EnumString)]
enum Color {
  Red,
  Green,
  Blue
}
```

You can **enumerate all variants of an enum** by using the `EnumIter` strum macro to derive the enumeration function and the `IntoEnumIterator` import to actually use the enumeration functionality. This will require the `strum` and `strum_macros` crates.
```rust
use strum::IntoEnumIterator;
use strum_macros::{EnumIter}

#[derive(EnumIter)]
enum HttpMethod {
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
eyJoaXN0b3J5IjpbMTUzNjY1Njg2OCwxMzk4OTg5NTcyXX0=
-->