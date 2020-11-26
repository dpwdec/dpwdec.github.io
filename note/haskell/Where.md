---
layout: page
exclude: true
title: Where
---

You can **set variables to be used in functions and guard conditionals** by using the `where` operator. This also called **binding**, because you are binding some information to the context of the function. In the example below the use of `where` allows use to only write the `length x` expression *once* and assign it to a variable that can then be used with each guard clause of the function.
```haskell
rename  ::  String  ->  String
rename x
       | y <=  0   =  "Nemo"
       | y <  5    =  "Fiveo"
       | y <  10   =  "Decaron"
       | otherwise =  "Longbono"
       where y = length x
```

You can **define multiple function scoped variables** using `where` by listing other variables below the initial `where` clause, indented at the level of the first variable definition.
```haskell
rename  ::  String  ->  String
rename x
       | y <=  nothing =  "Nemo"
       | y <  small    =  "Fiveo"
       | y <  medium   =  "Decaron"
       | otherwise     =  "Longbono"
       where y = length x
             nothing = 0
             small = 5
             medium = 10
```

You can **use pattern matching inside a `where` block**.
```haskell
where y = length x
      (nothing, small, medium) = (0, 5, 10)
```

You can **define functions inside a `where` block** that can be used in the context of your main function.
```haskell
initials  :: [(String, String)] -> [String]
initials names = [strip f l | (f, l) <- names]
where strip firstname lastname = [head firstname] ++  "."  ++ [head lastname]
```

You can **nest `where` blocks within functions**. The nested `where` block **must be indented past the original `where` block's variable definitions**.

You can **define pattern matched expressions** as part of a `where` block.
```haskell

```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYwNzAzNTYyOV19
-->