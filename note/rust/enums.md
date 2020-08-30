---
title: Rust: Enums
layout: page
exclude: true
---

Enums can be used to **pre-define a set of possible variants for a type**. You can **define the possible variants of an enum** using the `enum` keyword. The example below defines an `enum` called `primary_color` that can be `red`, `yellow` or `blue`.
```rust
enum primary_color {
  red,
  yellow,
  blue
}
```

You can **assign a concrete value of an enum to a variable** by referencing the contained type of the enum with a `::` double colon.
```rust
let color = primary_color::red
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbODgwODg3OTc4XX0=
-->