---
layout: page
exclude: true
title: Haskell
---

## Prelude

The `prelude` is Haskell's set of standard library components that are contained in Haskell's `base` package.

It is possible to load alternative `preluide`s or not have one at all.

## Types

You can **assign types** with the `::` double colons.

## Standard Lib

You can **convert a number into a string** using the `show` function.

## Order

When **applying arithmetic operators to functions** the function outputs will take highest precedence and will output their results to be used by the operators. So a statement like `f 20 + g 30 10` would be equivalent to `(f 20) + (g 30 10)` because the results of the functions `f` and `g` would be output in place between arithmetic is applied.
```haskell
succ 9 + max 10 20 --30
(succ 9) + (max 10 20) --30
```

When **chaining functions** order of nested function operations must be specified using `()` parentheses. Trying to pass the a function as an argument *directly* to another function will not automatically compute the result of the inner function and plug that result into the outer function, instead the computation before passing must be indicated using parentheses.
```haskell
succ max 10 20 --Error
succ (max 10 20) --21
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYxODAzNTI2OCwtMTA0MDcwODU2OCwxNT
g3MjcwMjI3LC0xOTU5MDk0NzcwLC0xNzMxNjU2NDc4XX0=
-->