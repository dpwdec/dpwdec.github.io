---
title: Rust
layout: page
exclude: true
---

## Cargo
You can **add a new code library** (also known as a "crate") to rust by adding to the `[dependencies]` section of the `cargo.toml` file. To add a new a crate simply input the crate's name and the version that you want to use. The actual installed version may differ from the version specified as this number only ensures that a version compatible with the specified version number will be installed.
```toml
[dependencies]
crate_name = "0.5.5"
```
Use `cargo build` to update and download any dependencies to your project. You can use `cargo update` to update your installed dependencies, this will also ignore your `cargo.lock` file.


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE1NjM5OTI2MywtODU4MDg4MjQzLC0xNj
A4ODI1MjYzXX0=
-->