---
title: Rust: Iterators
layout: page
exclude: true
---

## Functions that Return Iterators

You can **return an iterator from a function** by directly returning the structure the structure that an iterators yields.
```rust
fn return_split(word: &str) -> Split<'_, char> {
  word.split(' ')
}
```

You can **return an iterator from a function in a more readable way** by using the `impl Iterator` syntax. This essentially just dynamically replaces itself with the actually return type above but allows you to specify the iterator return as a generalised iterator with an `Item` type, this means we can specify in the code below that we expect to receieve back an `Iterator` that contains a list of `&str` rather than the more obfuscated `Split` object containing `char`s.
```rust
fn return_split(word: &str) -> impl Iterator<Item = &str> {
  word.split(' ')
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc2ODc4OTY4MSwtNzE2MDU1MDYyXX0=
-->