---
layout: page
exclude: true
title: Haskell
---

Haskell is composed entirely of expressions and declarations.

A Haskell program, no matter how complicated, can be understood as one big expression *composed* from smaller expressions.

**Declarations** are used to **name expressions**.

Expressions are said to be in **normal form** if they cannot be reduced any further or no more evaluation steps can be taken. The normal form of `2 + 2` is `4` because `4` can only stand for itself and cannot be further reduced.

Irreducible objects are also **referred to as values**.

Expressions that are reducible are sometimes called **redexes**.

You can also use the term **normalizing** to refer the evaluation of an expression.

A **parameter** refers to the generalised input argument to a function. For example the first `x` in the function `triple x = x * 3`.

An **argument** is the actual concrete value that is provided to a parameter of a function. For example the `3` when the function `triple 3` is called.

Haskell uses **lazy evaluation** which means that **terms are only evaluated when they are needed**.

## Prelude

The `prelude` is Haskell's set of standard library components that are contained in Haskell's `base` package.

It is possible to load alternative `prelude`s or not have one at all.

## Types

You can **assign types** with the `::` double colons.

## GHCi

You can **start using the GHCi repl** by loading it with the `stack` command.
```bash
$ stack ghci
```

You can **load an external haskell file** into the REPL by using the `:load` command. This could contain things like function and type definitions that you want to use interactively.
```bash
prelude> :load myfile.hs
```

You can **unload dependencies from the REPL** by using the `:module` command and return to the `prelude`.
```bash
>*Main :module
```

## Standard Lib

You can **convert a number into a string** using the `show` function.

## Functions

When defining a function it **must start with a lowercase letter**.
```haskell
triple x = x * 3 --ok
Triple x = x * 3 --WRONG
```

When defining **variables** they **must also start with a lowercase letter**.

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
eyJoaXN0b3J5IjpbMTA1NjUwODI5OCwtNzI1ODg0NTM0LC0xNz
Q5ODQxMzUxLDEyMDE0ODMzMDQsLTE4OTUyOTgyNywtMTU1NTM3
NDczMywxNzQ2ODQ2MDYsMTYxODAzNTI2OCwtMTA0MDcwODU2OC
wxNTg3MjcwMjI3LC0xOTU5MDk0NzcwLC0xNzMxNjU2NDc4XX0=

-->