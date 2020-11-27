---
layout: page
exclude: true
title: Lists
---

Lists in Haskell are **homogenous**. They can only contain one type of data.

You can **concatenate one list to the end of another list** using the `++` double plus operator.
```haskell
[1, 2, 3] ++ [4, 5, 6] 
-- [1, 2, 3, 4, 5, 6]
```

The `++` operator **can be slow** because it runs through the entirety of the list before appending to the end.

You can **concatenate a value to the front of a list** using the `:` colon operator. This value must **match the types** held in the list and can **only be applied in front of the list**.
```haskell
5:[1, 2, 3, 4] 
-- [5, 1, 2, 3, 4]
```

You can **rewrite list creation using the colon operator** and indeed, list literals in haskell are syntactic sugar for this sort of operation.
```haskell
[1, 2, 3] -- Same as...
1:2:3:[]
```

You can **retrieve an element from an list** by using the `!!` double exclamation (index) operator.
```haskell
[1, 2, 3, 4] !! 2 
-- 3
"Lewis Carroll" !! 6 
-- C
```

## Comparison

You can **compare lists** by using the standard comparison operators `<`, `<=`. `>`, `>=` and `==`. This works if the elements being compared *can* be compared. Lists are **compared in lexicographical order** with the first elements being compared and then the next and so on **until a definitive comparison can be made**. 

For example if we were comparing `[1, 2, 3]` with `[1, 4, 0]` using the `>` operator, the comparison will stop as soon as something is found that proves or disproves this. So, first `1` and `1` are compared and found to be equal so a call cannot be made, then `2` and `4` are compared and the function returns with `False`.
```haskell
[1, 2, 3] > [1, 4, 0] 
-- False
[1, 2, 3] > [1, 2, 0] 
-- True
[1, 2, 3] > [0, 2, 100] 
-- True
```

The **exception** to this is **lists of different lengths** where if a definitive call cannot be made the list with the shorter length is "less than".
```haskell
[1, 2, 3] > [1, 2] 
-- True
[1, 2, 3] > [1, 5]
-- False
```

If you **compare lists for equality** using the `==` operator, it will only return `True` if all elements are the same.
```haskell
[1, 2, 3] == [1, 2, 3] 
-- True
[1, 2, 3] == [1, 2] 
-- False
```

## Functions

You can **get the front of a list except its last element** by using the `init` function.
```haskell
init [1, 2, 3, 4, 5] 
-- 5
```

## Ranges

You can **create a range** that automatically generates a list by using `..` double periods between the start and end of the ranges. This only works for things that can actually be operated on sequentially.
```haskell
[1..10]
-- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

You can **define a step for a range** by demonstrating a comma separated step *before* use the range operator. In the example below, we start with `2,4` to describe a step range of two and then use the `..` operator to fill in the rest of the sequence.
```haskell
[2,4..20]
-- [2, 4, 8, 10, 12, 14, 16, 18, 20]
[2,5..35]
-- [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
```

You can **create a descending list** by demonstrating a *negative* comma separated step before using the range operator. `10..0` on its own would **not work**.
```haskell
[10,9..0]
-- [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### Unbounded / Infinite ranges

You can **work with unbounded ranges** by taking advantage of haskell's lazy evaluation. For example, if you wanted the first 10 multiples of 2 you could leave the end of the range unbounded and then use the `take` function to get a specific number of elements from that range. The unbounded range would then **only be evaluated once it is called on** and condensed to a specific bounded list.
```haskell
take 10 [2,4..] --unbounded range
-- [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

There are also functions like `cycle` and `repeat` that will **produce infinite lists of elements** that need to be sliced to get a bounded version of them.

You can produce a **bounded list of repeated elements** by using the `replicate` function.
```haskell
replicate 3 10
-- [10, 10, 10]
```

## List comprehension

Ranges are useful but limited in that they can only produce very limited sequences. You can **create more complex lists** using **list comprehensions**.

You can **create a list comprehension** by using the form `[function arg | arg <- range, optional predicate]`.
```haskell
[x * 2 | x <- [1..10]]
-- [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[x * 2 | x <- [1..10], x * 2 >= 12]
-- [12, 14, 16, 18, 20]
```

You can **add multiple comma separated predicates** to your list comprehension expressions.
```haskell
[x | x <- [10..20], x /= 13, x /= 15, x /= 19]
-- [10, 11, 12, 14, 16, 17, 18, 20]
```

You can **combine multiple lists** by comma separating the ranges that the lists are drawing from. This works like a 2D iterator, traversing the elements of the first list once and the elements of the second list as many times as there are elements in the first.
```haskell
[(x, y) | x <- [0..5], y <- [0..5]]
-- [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
```

You can **use strings in list comprehension** just as you would any list of data.
```haskell
[c | c <- "gOtorETail", c `elem` ['A'..'Z']]
-- "OET"
```

You can **nest list comprehensions**.

You can **think of list comprehensions** as **just another version of the map filter** pattern. They allow you to take a range of values, apply a mapping to them and filter the results.
```haskell
double3' range = filter predicate (map double range)
    where predicate x = x `mod`  3  ==  0
          double x    = x *  2
```



```haskell
double3 range = [ dx | x <- [0..range], let dx = x *  2, dx `mod`  3  ==  0]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTgyODU0NzQ5LC0xMTA4Nzc4OTIsMTk0Nj
k4MzYzMiwtMTc2NDg1MTY1NiwtMjA0NjYzMTc4MF19
-->