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
let color = primary_color::blue
```

You can **place values INSIDE an enum**. This requires you to change the enum definition to specify that value that each variant can hold. The example below shows an updated `primary_color` enum that allows each variant to *hold* a `u8` value.
```rust
enum primary_color {
  red(u8),
  yellow(u8),
  blue(u8)
}
```

You can **use differing types for the value contained in an enum**.
```rust
enum protocol {
  numeric(u8),
  functional(String),
  iterative(vec<u32>)
}
```

You can **assign contained values to an enum** by providing a value when assigning the enum to a variable.
```rust
let color = primary_color::blue(122)
```

One of the **advantages of using enums** is that you can **define functions that take an enum** as a way to define an input for **lots of diffe**


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MDQ0NzU5NDNdfQ==
-->