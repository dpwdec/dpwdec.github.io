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
-- 16
mult2 = (*2)
twice mult2 10
-- 40
```

If you are **not passing in an entire function as a single argument** then you don't need to use parentheses. For example, in the `flip` function, the signature can be written as `(a -> b -> c) -> (b -> a -> c)` to indicate that it is returning a function. However, the second set of parentheses is optional because this `flip` function simply returns a curried function which takes the original arguments flipped. They are equivalent.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTM5MTExMzYwLDE4OTc5ODA5NjYsLTIwND
MzNzc3NTIsMTU1MDg1OTk1OV19
-->