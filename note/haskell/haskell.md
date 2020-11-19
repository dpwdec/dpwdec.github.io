---
layout: page
exclude: true
title: Haskell
---

Haskell is composed entirely of expressions and declarations.

A Haskell program, no matter how complicated, can be understood as one big expression *composed* from smaller expressions.

**Declarations** are used to **name expressions**.

Expressions are said to be in **normal form** if they cannot be reduced any further or no more evaluation steps can be taken. The normal form of `2 + 2` is `4` because `4` can only stand for itself and cannot be further reduced.

Irreducible terms are also **referred to as values**, such as `4`.

Expressions that are reducible are sometimes called **redexes**.

You can also use the term **normalizing** to refer the evaluation of an expression.

A **parameter** refers to the generalised input argument to a function. For example the first `x` in the function `triple x = x * 3`.

An **argument** is the actual concrete value that is provided to a parameter of a function. For example the `3` when the function `triple 3` is called.

Haskell uses **lazy evaluation** which means that **terms are only evaluated when they are needed**.

**Application is evaluation**: applying a function to an argument means that argument needs to be evaluated.

Haskell **does evaluate everything to normal form by default**, instead it evaluates to **weak head normal form** or **WHNF** which means that *not everything* is reduced to its most irreducible form immediately.

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

### Infix Functions

You can **use a function as an infix** by surrounding the function name with backticks ` if the function takes two arguments.
```haskell
div 10 2 -- = 5
10 `div` 2 -- = 5
```

You can **use infix functions like regular functions** by surrounding them with `()` soft braces.
```haskell
(+) 20 30 -- = 50
```



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
eyJoaXN0b3J5IjpbMjc0MjQxODM2LDcwMzcxNzQ1NiwtMTExMj
IyODEzMCwtNTQ4NDEwNDAyLC03MjU4ODQ1MzQsLTE3NDk4NDEz
NTEsMTIwMTQ4MzMwNCwtMTg5NTI5ODI3LC0xNTU1Mzc0NzMzLD
E3NDY4NDYwNiwxNjE4MDM1MjY4LC0xMDQwNzA4NTY4LDE1ODcy
NzAyMjcsLTE5NTkwOTQ3NzAsLTE3MzE2NTY0NzhdfQ==
-->