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

You can **get info about a function** by using the `:info` command followed by the function. The second number shows the **precedence of the function** which ranges from `0-9` with `9` being the highest precedence.
```bash
prelude> :info (*)
-- infixl 7 *
```

## Standard Lib

You can **convert a number into a string** using the `show` function.

The `div` function can be **used for integral division** and **always rounds down**.

The `quot` function can be **used for integral division** and **always rounds towards zero**, so with negative division it will round up.

## Mod vs Rem

The `mod` and `rem` functions are similar but have some key differences.

The `mod` function wraps values around a range even when those values are negative.
```haskell
mod 2 7 -- = 1
mod (-13) 7 -- = 1
```

The `rem` function returns the remainder of dividing one number by another.
```haskell

```

## Functions

When defining a function it **must start with a lowercase letter**.
```haskell
triple x = x * 3 --ok
Triple x = x * 3 --WRONG
```

When defining **variables** they **must also start with a lowercase letter**.

### Infix Functions

Infix functions use the **infixl** type for **left associative functions**. For example, `6 * 2 * 3` will be evaluated as `(6 * 2) * 3` because `*` is a left associative infix function.

Infix functions use the **infixr** type for **right associative functions**. For example `2 ^ 3 ^ 4` will be evaluated as `2 ^ (3 ^ 4)` because `^` is a right associative infix function.

You can **use a function as an infix** by surrounding the function name with backticks ` if the function takes two arguments.
```haskell
div 10 2 -- = 5
10 `div` 2 -- = 5
```

You can **use infix functions like regular functions** by surrounding them with `()` soft braces.
```haskell
(+) 20 30 -- = 50
```

You can **define your own infix functions** by surrounding them with `()` soft braces at definition.
```haskell

```

## Modules

You can **define a module** by using the `module` and `where` keyword. The **module name should be capitalised**.
```haskell
module MyModule where

-- code here
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
eyJoaXN0b3J5IjpbLTIwMTgyNDkxMzgsLTg0NzU2OTU2MywtMT
YyMjUxNDA0NywtMTQ0OTU0NjI1NiwtMTk5MjczNTM2NCwtMTYx
OTA0ODI4NCwxODc1NjA0MjQwLDcwMzcxNzQ1NiwtMTExMjIyOD
EzMCwtNTQ4NDEwNDAyLC03MjU4ODQ1MzQsLTE3NDk4NDEzNTEs
MTIwMTQ4MzMwNCwtMTg5NTI5ODI3LC0xNTU1Mzc0NzMzLDE3ND
Y4NDYwNiwxNjE4MDM1MjY4LC0xMDQwNzA4NTY4LDE1ODcyNzAy
MjcsLTE5NTkwOTQ3NzBdfQ==
-->