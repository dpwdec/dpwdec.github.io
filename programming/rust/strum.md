---
title: Strum
layout: page
exclude: true
---

Strum is a library that offers a range of utilities relating enums.

You can use strum to **deserialize an enum from a string representation** by using the `EnumString` trait with the `std::str::FromStr` method. The `strum(serialize = "<PATTERN>")` attribute is added with the different deserialization pattern that you want to use to match from. The example below matches `r` for the `Red` enum variant, allowing you to define arbitrary string representations to be deserialized from.
```rust
use strum_macros::EnumString;
use std::str::FromStr;

#[derive(EnumString)]
enum Color {
  #[strum(serialize = "red", serialize "r")]
  Red,
  #[strum(serialize = "green", serialize "g")]
  Green,
  #[strum(serialize = "blue", serialize "b")]
  Blue
}

fn main() {
  Color::from_str("r").unwrap() // => Color::Red
}
```

You can **serialize an enum to a string** using the `ToString` trait with the `std::string::ToString` method. It's important to note that **this uses the SAME `serialization` attribute as the deserialization pattern** which can make it awkward if you want to deserialize from lots of different patterns but serialize using only a single pattern. In this case it's better to use the `to_string` attribute. In the example below the string could be deserialized from `"Red"` or `"r"` but only gets serialized to a string as `"red"`. It seems if you don't make this explicit which variant you want as serialization then it will seemingly choose one at random.

It also seems like you don't necessarily need the `std::string::ToString` import and I'm not sure why.

If you provide no serialization attributes then the `to_string` will simply produced a literal representation of the enum name. So in the example below `Red` would just be serialized as `"Red"`.
```rust
use strum_macros::ToString;
use std::string::ToString;

#[derive(ToString)]
enum Color {
  #[strum(to_string = "red", serialize = "Red", serialize "r")]
  Red,
  // other colors
}

fn main() {
  Color::Red.to_string() // => "red"
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