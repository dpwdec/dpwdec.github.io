---
layout: page
exclude: true
title: Haskell
---

## Order

When **applying arithmetic operators to functions** the function outputs will take highest precedence and will output their results to be used by the operators. So a statement like `f 20 + g 30 10` would be equivalent to `(f 20) + (g 30 10)` because the results of the functions `f` and `g` would be output in place between arithmetic is applied.
```haskell
succ 9 + max 
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ5MjQ3Mzc1Nl19
-->