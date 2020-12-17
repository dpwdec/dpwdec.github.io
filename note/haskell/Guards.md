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
maximum' :: (Ord a) => [a] -> a
maximum' [] = error "maximum of empty list"
maximum' [x] = x
maximum' (x:xs)
         | x > maxTail = x
         | otherwise = maxTail
         where maxTail = maximum' xs
```

Pattern matching with guards can also **fall through to further patterned matched conditions** if no `otherwise` case is specified. In the code below the first instance of `fall` doesn't contain an `otherwise` clause for matching against values of `x` other than those less than `0` so the value falls through to the next definition of `fall` which is a direct pattern match with `10` and then a final guard clause statement which does have an otherwise.
```haskell
fall  :: (Num  a, Eq  a, Ord  a) =>  a  -> [Char]
fall x
     | x <  0  =  "Less than zero"
fall 10  =  "x is 10"
fall x
     | x <  10  =  "Less than 10"
     | otherwise =  "Greater than 10"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjg2MjM2NDIyLC03Nzk3Mjk4NTMsMTc4MT
g4MjA1LDE3NjM4MDUzMDksMzExMTEzNzYxXX0=
-->