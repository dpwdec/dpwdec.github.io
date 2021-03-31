---
title: Iterators
layout: page
exclude: true
---

## Zip

If you want to **combine the values of two iterators into a set of tuple pairs** you can use the `zip` function.
```rust
first_iterator.zip(second_iterator).collect::<Vec<(usize, usize)>>()
// [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
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

## Mutable Iterators

You can **mutate the objects in a mutable structure with an iterator** by using the `iter_mut()` function. It seems logical that if you mark a structure as `mut` and then use `iter` or `into_iter` the values returned by the iterator should mutate the structure, but this is *not* the case and causes a world of pain, even if you mark the `x` inside the closure with `mut`  it will still result in errors because the values from `iter` *cannot* be written to.
```rust
// wrong :(
let mut x = vec![1, 2, 3, 4];  
x.iter().for_each(|x| *x += 1); // ERROR
// right :)
let mut x = vec![1, 2, 3, 4]; 
x.iter_mut().for_each(|x| *x += 1); // => [2, 3, 4, 5]
```

When **iterating mutably over nested structures** all outer and inner structures *must* use `iter_mut` regardless of how nested the structure is that is actually changing. Using an `iter` method on one of the iterations below while changing the inner structure would cause the same mutabili
```rust
let mut x = vec![vec![1, 2, 3], vec![4, 5, 6]];   
x
  .iter_mut()
  .for_each(|y| {  
    y
    .iter_mut()
    .for_each(|z| *z += 1)  
}); // => [[2, 3, 4], [5, 6, 7]]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzI3NzM1NDEsODU1OTg5MTc5LDgzNTk4Mj
I4LDIxMTA1MjkyOTIsLTExMzc0NDg3MzEsLTc2ODc4OTY4MSwt
NzE2MDU1MDYyXX0=
-->