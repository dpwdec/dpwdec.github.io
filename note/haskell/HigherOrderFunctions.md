---
layout: page
exclude: true
title: Higher Order Functions
---

You can **define a higher order function** by bracketing function input in the functions type definition. In the example we define a function called `twice` that takes a function, indicated by the bracket `(a -> a)` which itself takes an `a` and returns an `a`, this then takes a further `a` and outputs `a` by applying the initial function argument twice.
```haskell
twice :: (a -> a) -> a -> a
twice f x = f (f x)
twice (+3) 10
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI3ODA0MzUyMiwtMjA0MzM3Nzc1MiwxNT
UwODU5OTU5XX0=
-->