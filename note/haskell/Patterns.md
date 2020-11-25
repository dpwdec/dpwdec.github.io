

## Functions

You can **define multiple versions of the same function** that produce different results depending on their input. These function definitions will pattern match whatever argument is passed **in order of definition** and produce an output based on a matching input. The example below shows that if a `7` is passed into the `lucky` function then it will return `"LUCKY NUMBER SEVEN!"` otherwise, if any other `x` is passed in it will return `"Sorry, you're out of luck, pal!"` If the `x` case had been *defined first* then `lucky` would only ever return the second case.
```haskell
lucky :: (Integral a) => a -> String
lucky 7 = "LUCKY NUMBER SEVEN!"
lucky x = "Sorry, you're out of luck, pal!"
```

This sort of pattern matching allows you **elegantly define recursive functions** as the final state at the end of the recursion (in this case `0`) which would usually be defined by an `if` in the body of the function in other languages is instead just pattern matched when the function is called, thus retaining the clarity of the original function.
```haskell
factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

## Tuples

If you **define a pattern matched function that doesn't cover all input possibilities** and you call it with a value outside of its defined patterns you will get an `Non-exhaustive patterns` error.

You can **pattern match** and **destructure tuple arguments to functions** directly in a function definition rather than referring to a tuple argument as a single variable like `x`. Instead you can express it as `(x, y)` to put the values within the tuple into the scope of your function directly.
```haskell
addTuple (Num a) => (a, a) -> a
addTuple (x, y) = x + y
```

The **less elegant solution** would be to destructure the tuple inside the body of the function.
```haskell
badTuple (Num a) => (a, a) ->
badTuple x = fst x + snd x
```

## Lists

You can **pattern match lists** by using defining the name for the lists element you want to destructure to, followed by the `:` operator and then the list in the form `x:myList`
```haskell
head' :: [a] -> a
head' (x:_) = x
head' [1, 2, 3]
-- 1
```

This can be **extended to an arbitrary number of destructured variables**.
```haskell
combineHead :: [a] -> (a, a)
combineHead (x:y:_) = (x, y)
combineHead [1, 2, 3]
-- (1, 2)
```

You can also **destructure. and pattern match lists directly** if you know they are of a static length that is known beforehand. If this destructuring pattern is passed a list of the wrong length it will error with a `non-exhaustive patterns` error.
```haskell
toTuple [x, y] = (x, y)
toTuple [3, 4] = (3, 4)
toTuple [3, 4, 5]
-- ERROR
```

You can also **destructure lists in reverse**, removing the first elements with an `_` and pattern matching the rest of the list.
```haskell
tail' :: [a] -> [a]
tail' (_:x) = x
```

## As Patterns

**As patterns** allow you to **pattern match structures while ALSO retaining the original structure**. You can do this by putting a variable name that will contain the entire structure followed by a `@` at the beginning of the pattern matching.
```haskell
start word@(x:_) = "The first element of " ++ word ++ " is " ++ [x]
start "Hello"
-- The first element of Hello is H
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM2NzQ4MjQ5OV19
-->