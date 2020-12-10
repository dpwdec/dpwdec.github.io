---
layout: page
exclude: true
title: Recursion
---

**Statically defined cases** in a recursive function are known as **edge conditions**. For example, if you have a function that sums a list of numbers recursively up to a limit you can define an *edge condition* that stops the recursively loop and returns a final value. In the example below the edge condition occurs when the summing value passed into `f` reaches `1` at which point the function returns.
```haskell
f :: (Eq a, Num a) => a -> a 
f 1 = 1
f x = x + sumf (x -  1)
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY4MDg0NzYwMSwxMDczNjA4MjYyXX0=
-->