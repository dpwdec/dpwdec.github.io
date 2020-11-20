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

The **minus operator** is also a special case because the parathensised `-` minus `negate` function can also be applied using the `-` minus operator. 

```haskell
(-1) 2 -- ERROR
```

You **can only section the `-` minus operator with the **

### $ operator

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYwODQzMjY1MSwxMjQxMDI1ODI1LDU2Nz
Q2MTgyOV19
-->