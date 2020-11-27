---
layout: page
exclude: true
title: Operators
---

Operators **behave just like functions** in Haskell and can be curried, passed around and applied.
```haskell
x = (+10) -- currying the first argument of the + function
x 20 -- = 30
```

The **order in which you parenthesise non-commutative operators matters**.
```haskell
(1/) 2 -- = 0.5
(/1) 2 -- = 2.0
```

The **minus operator** is also a special case because the parenthesised `-` minus operator doubles as the `negate` function and simply returns a number meaning it cannot be sectioned and applied leading to an error.
```haskell
(-1) 2 -- ERROR
```

You **can only section the `-` minus operator with the operand in the right position**.
```haskell
(1-) 2 -- = -1
```

## $ operator

The `$` operator allows you to reduce the amount of brackets used in your code by applying the result of functions to one another as an `infixr` operator with a low priority, thus the right most part of an expression is evaluated and applied and then the next rightmost and so on.

For the example, the following function uses a lot of nested parentheses making it more difficult to read.
```haskell
max 10 (min 20 (max 2 5)) -- = 10
```

This can be rewritten using the `$` operator to express the same application of functions.
```haskell
max 10 $ min 20 $ max 2 5 -- = 10
```

The **definition of the `$` operator** is:
```haskell
f $ a = f a
```

## Conditionals

You can **express NOT EQUAL to** by using the `/=` operator.  Different from the usual `!=` operator in almost all other languages. This is intended to be reminiscent of the `≠` symbol.
```haskell
2 /= 3
-- True
2 /= 2
-- False
```

## Piping

You can **pipe data in a left to right manner** similar to a standard `|` pipe function using the `&` operator from the `Data.Function` library which sequential passes the result of each function into the next.
```haskell
import Data.Function
reverse [1, 2, 3, 4] & head & succ
-- 5
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM5MzcxNTg1OCw5NDYyNDU3ODMsLTM4OT
MyNTAzNSwxMjQxMDI1ODI1LDU2NzQ2MTgyOV19
-->