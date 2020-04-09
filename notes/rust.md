---
title: Rust
layout: page
exclude: true
---
## Control Flow
The `match`
## Cargo
You can **add a new code library** (also known as a "crate") to rust by adding to the `[dependencies]` section of the `cargo.toml` file. To add a new a crate simply input the crate's name and the version that you want to use. The actual installed version may differ from the version specified as this number only ensures that a version compatible with the specified version number will be installed.
```toml
[dependencies]
crate_name = "0.5.5"
```
Use `cargo build` to update and download any dependencies to your project. You can use `cargo update` to update your installed dependencies, this will also ignore your `cargo.lock` file.

## Rand
The `rand` crate allows you generate random numbers at run time for your program. The random number generator works by creating a `thread_rng` object that is localised to our execution thread and seeded by the operating system.
```rust
use rand::Rng;
// generate a new random number
let random_number = rand::thread_rng.gen_range(1, 101)
```
The `gen_range()` function is inclusive at its bottom end and exclusive at its top end. In the above example it will produce a number between 1 and 100.
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMTUxNDMwNzcsLTg1ODA4ODI0MywtMT
YwODgyNTI2M119
-->