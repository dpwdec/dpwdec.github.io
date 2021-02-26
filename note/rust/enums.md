---
title: Enums
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

You can **define functions that can be passed an enum** as a way to create a function that can take an input for **lots of different possible input types**. In the example below, the `execute` function takes the `protocol` enum as an argument which code enclose `u8`, `string` or `vec<u32>` types (as defined above), this creates a very flexible function which can take a lot of different types while also maintaining a clear semantic structure within the code.
```rust
fn execute(pr: protocol) {
  // use protocol for different things
}
```

You can **implement methods on enums**.

## Option

You can **map the contents of an option enum WITHOUT having to unwrap it** by using the `map` function. This will `map` the value *inside* the `Option` *if* it contains a value, otherwise it will continue to be none. This allows you to work with the values inside an `Option` in a "lazy" manner and only `unwrap` it when it is needed.
```rust
let x = Some(10)

let x_mapped = x
  .map(|n| n + 10) // => Some(20)
  .map(|n| n - 1) // => Some(19)
```

The `Option` enum supports the equivalent of a `flat_map` function with a function called `and_then`. This is useful to avoid situations in which the `map`ping results in nested `Option` structures, such as `Option<Option<u32>>`.
```rust
let x = Some(10)

let x_mapped = x
  .map(|n| n + 10) // => Some(20)
  .map(|n| n - 2) // => Some(18)
  .and_then(|n| divide(2, n)) // => Some(9)
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA0NTYyMDc4NSwtMTgxNTExNTEsMTU0OT
YyMjc3OV19
-->