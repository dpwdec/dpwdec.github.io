---
title: Types
layout: page
exclude: true
---

You can **set the type of a constructor IN LINE when creating a new instance of some structures** by including the type in `<>` angle brackets between an extra pair of `::` double semicolons before creating the instance. This creation method is an alternative to typing the assignment variable at declaration. This method of typing new objects is useful when creating instances for functions like `fold` which need an `acc` to add to.
```rust
let set = HashSet::<i32>::new();
let map = HashMap::<i32, str>::new();
// old alternative
let set: HashSet<i32> = HashSet::new();
```

## Collect

You can **type annotate an iterator's collect method** by following the call to `collect` with `::` double colons followed by the type in angled brackets and then invoking the function.
```rust
let result = (0..10).collect::<Vec<u32>>();
```

## Floating point bit representation

You can **convert a floating point number to and from its bit representation** by using the `to_bits` and `from_bits` functions on floating point types.
```rust
fn  main() {
  let x: f64 = 5.2;
  let y: u64 = x.to_bits();
  let z: f64 = f64::from_bits(y.clone()); // => 5.2
}
```

You can **make conversion from a bit repesentation of a floating point number less verbose by using a trait implementation *on* the bit type**.
```rust
trait BitConversion {
    fn to_f64(&self) -> f64;
}

impl BitConversion for u64 {
    fn to_f64(&self) -> f64 {
        f64::from_bits(self.clone())
    }
}

fn main() {
  let x: f64 = 5.2;
  let y: u64 = x.to_bits();
  let z: f64 = y.to_f64() // => 5.2
}
```