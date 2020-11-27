---
title: Iterators
layout: page
exclude: true
---

## Zip

If you want to **combine the values of two iterators into a set of tuple pairs** you can use the `zip` function.
```rust
(0..5).zip(0..10).for_each(|x| println("{:?}", x))
// (0, 5)
// (1, 6)
// (2, 7)
// (3, 8)
// (4, 9)
```

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
eyJoaXN0b3J5IjpbMjExMDUyOTI5MiwtMTEzNzQ0ODczMSwtNz
Y4Nzg5NjgxLC03MTYwNTUwNjJdfQ==
-->