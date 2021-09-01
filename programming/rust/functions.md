---
title: Functions
layout: page
exclude: true
---

You can **create a collection of functions** by using the `dyn` keyword with a reference specifier `&` and passing references to the function into the collection.
```rust
fn main() {
    let fns: Vec<&dyn Fn(i32) -> i32> = vec![&fn1, &fn2];
}

fn1(x: i32) -> i32 { x }
fn2(x: i32) -> i32 { x * 2 }
```

You can **create a collection of functions as a field in a struct** by appending a lifetime specifier as well to the collection.
```rust
struct FunctionHolder<'a> {
    fns: Vec<&'a dyn Fn(i32) -> i32>
}

fn main() {
    let fh: FunctionHolder { 
        fns: vec![&fn1, &fn2]
    }
}
```