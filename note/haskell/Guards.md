---
layout: page
exclude: true
title: Guards
---

Guard conditions allow you to **express function branches using boolean expressions** instead of pattern matching. Guard conditions are expressed with a set of aligned `|` characters followed by the condition and assignment to the function body.

If a **condition evaluates to false** it **falls through to the next expression**. 

To **catch all other cases** it's a convention to use an `otherwise` variable.
```haskell
numberSize :: (Integral a) => a -> String
numberSize x
          | x < 0     = "Negative"
          | x <= 20   = "Twenty or less"
          | otherwise = "Bigger than twenty"
```

You can **combine guard clauses with normal pattern matching**.
```haskell

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjgzNzI5MjgsMTc2MzgwNTMwOSwzMTExMT
M3NjFdfQ==
-->