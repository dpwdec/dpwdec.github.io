---
title: Functional Programming
layout: page
exclude: true
---

## Composition

Composition in the essence of functional programming. What exactly does composition mean though? Composition means creating a composite of two or more operations. Passing the output from one operation to the input of another operation.

Composition is:

 - Chaining function calls
 - Passing returns calls from one function into another
 - Calling two (or more) methods in sequence - This final composition is more subtle. In this case the data being acted on is implicitly the data represented by the `this` or `self` object which holds that method.
```
let data = {
  foo: 10
}
```

## Pure functions

If you call a function and don't use its return type you are probably using an impure function.

A function is **pure** if you can replace the entire function with the 

## Imperative vs Functional

Imperative programming works with statements

Functional programming works with expressions

The value that an expression evaluates to can be given a name.

`[1, 2, 3]` is an expression and the "result" of this expression can be assigned to a variable.
```js
const x = [1, 2, 3]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwOTc5ODU0ODIsMjEzODUwNDU1NCw2NT
AzNTI5MDcsMzY4MzkxNjg4LDUwNzA4MzcyOCwxNDk2NjkyMjEs
LTU0MDI3MjE2M119
-->