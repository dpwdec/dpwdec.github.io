---
title: Extern Crates
layout: page
exclude: true
---

To **use an `extern crate` dependency source with a project that contains a submodule structure** you cannot place the external use statement inside the submodule. Instead, you should place it in the `lib.rs` file before the `mod` definition of your submodules.

```rust
// lib.rs
#[macro_use]
extern crate my_external_src;

// my_external_src is now available to submodules

pub mod my_module;
pub mod my_other_module;
```