---
title: Hash Map
layout: page
exclude: true
---

You can **mutate the values in a hashmap** by using the `get_mut` method.
```rust
let mut map: HashMap<char, Vec<u32>> = HashMap::new();
map.insert('a', vec![0]);
match map.get_mut('a') {
  Some(v) => v.push(1),
  None => println!("None!")
}
// {'a': [0, 1]}
```

## Floating points and Hashable Values

You **cannot *directly* use floating point numbers or even structures *CONTAINING* floating point numbers as keys in a hashable structure**. For example, the following structures would *not* be valid because `f64` cannot implement the `Eq`, `PartialEq` or `Hashable` traits. Even a struct that uses an `f64` cannot implement this trait because all its fields must ALSO implement these traits.
```rust
fn main() {
  let invalid_float_map: HashMap<f64, &str> = HashMap::new();
  let invalid_struct_map: HashMap<MyStruct, &str> = HashMap::new();
}

struct MyStruct {
    x: f64
}
```

You **can use floating point numbers and floating point containing structs as keys in hashable structures** by storing floating point numbers as a **bit representation**. This can be done using the standard library `to_bits` and `from_bits` functions.
```rust
fn Main() {
  let x: f64 = 5.2;
  let y: u64 = x.to_bits();
  let valid_float_map: HashMap<u64, &str> = HashMap::new();
  valid_float_map.insert(x, "fake float");

  let x: MyStruct = MyStruct { x: (5.2_f64).to_bits() };
  let valid_struct_map: HashMap<MyStruct, &str> = HashMap::new();
  valid_struct_map.insert(x, "fake struct");
}

struct MyStruct {
    x: u64
}
```