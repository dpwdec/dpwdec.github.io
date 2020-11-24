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

**Passing around partially applied functions** is known as **sectioning**.

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

You can **show the type of something** by using the `:type` or `:t` command.
```bash
prelude> :type 'a'
'a' :: char
prelude> :t 1
'a' :: Int
```

You can **get info about a function** by using the `:info` command followed by the function. The second number shows the **precedence of the function** which ranges from `0-9` with `9` being the highest precedence.
```bash
prelude> :info (*)
-- infixl 7 *
```

If functions with the same precedence are applied to each other with out parentheses indicating order Haskell will throw an `Precendence parsing error`.
```haskell
9 + -2 -- ERROR
```

## Standard Lib

You can **convert a number into a string** using the `show` function.

The `div` function can be **used for integral division** and **always rounds down**.

The `quot` function can be **used for integral division** and **always rounds towards zero**, so with negative division it will round up.

### Mod vs Rem

The `mod` and `rem` functions are similar but have some key differences.

The `mod` function wraps values around a range even when those values are negative. For example if use `7` to represent the days of the week (Sunday - Saturday) and wanted to find what day of the week `9` days from the `0`th day of the week was, then we can see that `7`th day is Sunday again, the `8`th is Monday, and the `9`th is Tuesday (or index `2`), this is what `mod` returns. This wrapping can be done negatively as well.
```haskell
mod 9 7 
-- 2 (Tuesday)
mod -1 7 
-- 6 (Saturday)

-- comparison to rem examples
mod 2 7 
-- 2
mod (-13) 7 
-- 1
```

The result of `mod` is **negative if the divisor is negative**.

The `rem` function returns the remainder of dividing one number by another.
```haskell
rem 2 7 
-- 2 (same as mod)
rem (-13) 7 
-- -6 (differfent from mod)
```

The result of `rem` is **negative if the dividend is negative**. The term **dividend** refers to the **thing that is being divided**.

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
div 10 2 
-- 5
10 `div` 2 
-- 5
```

You can **use infix functions like regular functions** by surrounding them with `()` soft braces.
```haskell
(+) 20 30 
-- 50
```

You can **define your own infix functions** by surrounding them with `()` soft braces at definition.
```haskell

```

### The ' apostrophe

The `'` apostrophe character is a **valid character in function names**. The `'` apostrophe can be used to indicate a modified version of an existing function.
```haskell
double x = x * 2
double'x = (*2) x
``` 

### Function Type Definitions

You can **declare your function's type** by using the `::` double colon (type of) operator followed by the type signature of your function.
```haskell
sumThree :: Int -> Int -> Int -> Int
sumThree x y z = x + y + z
```

### Pattern Matching

You can **define multiple versions of the same function**

## Conditionals

## Indenting

## Tuples

You can **combine two lists** using the `zip` function. This pairs up each element at the same index in two lists producing a list of tuples consisting of the paired elements.
```haskell
zip [1, 2, 3, 4] [5, 6, 7, 8]
-- [(1,5), (2,6), (3,7), (4,8)]
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
succ 9 + max 10 20 
-- 30
(succ 9) + (max 10 20) 
-- 30
```

When **chaining functions** order of nested function operations must be specified using `()` parentheses. Trying to pass the a function as an argument *directly* to another function will not automatically compute the result of the inner function and plug that result into the outer function, instead the computation before passing must be indicated using parentheses.
```haskell
succ max 10 20 -- Error
succ (max 10 20) 
-- 21
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAwMzQ0NjYxNSwxNzAwMzE5OCwtMTA3Mj
gwNDYyNiwtODQxMTc3MDk0LC0xODMyMDI3Mjk0LC0xMzUwMjEw
MiwtNTU1MjE5MzEsLTIwOTMzNDE5MSwtOTg5MDg2MjAwLDg4Mj
I5NDgxNiwtMTkwNzE2MjA5LC0xMDIxMzc1NTQwLC0xMzY1MzMx
MjQ3LDEyMDg3MTk0ODksODYwMzE1NjMwLDE2MTkyNzU0MzUsLT
Q3MDE1NDQ3MCwtMjM3NzQzMTQ1LDE0NjA0OTE1ODYsMTc2MTcw
NDY0XX0=
-->