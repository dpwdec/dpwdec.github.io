---
layout: page
exclude: true
title: Types
---

## Type Variables (Generics)

Haskell's version of generics are called Type Variables.
```haskell
head :: [a] -> a
```

Functions that use type variables are called **polymorphic functions**.

Type variables are usually named in the format `a`, `b`, `c`, `d` ... etc.


## Typesclasses

Typeclasses are similar interfaces in object oriented languages or traits in Rust, they are used to describe a behavior that a type implements.

Below is an example of the `==` equality operator's type signature. The `=>` hash rocket is used to show the type classes of different inputs to a function, these are also called **class constraints**. In the case of `==`, this type signature shows that the type `a` must implement the class constraint `Eq` to passed into this function.
```haskell
== :: (Eq a) => a -> a -> Bool
```

The `Ord` typeclass takes types that can be ordered in a hierarchy. Types can only be part of `Ord` if they also implement `Eq`.

The `Show` typeclass describes **types that can be presented as strings**.

The `Read` typeclass describes **types that can coerced from a string form into their actual type**. This can be demonstrated using the `read` function
```haskell
read "8" - 3
-- 5
read "True" || False
-- True
```

In the examples above the **type that `read` outputs is inferred** by how it is used. However, if you use `read` on its own without usage then the type returned is ambiguous and the compiler will complain with `ambiguous type variable`. You can **resolve ambiguous types** by including a type annotation *after* the use of the function.
```haskell
read "5" :: Int
-- 5
read "5" :: Float
-- 5.0
```

The `Enum` typeclass can be sequentially ordered and enumerated. This includes types that can be placed in ranges. Such as `Char` and `Int`.

The `Bounded` has members that have an upper and a lower bound. You can **get these bounds** by using the `minBound` and `maxBound` functions.
```haskell
minBound :: Int
-- -2147483648
maxBound :: Char
-- '\1114111'
```

The `Num` typeclass has members that behave like numbers. Whole numbers **act like polymorphic constants** because they can stand in for many types that are members of the `Num` typeclass.
```haskell
20 :: Int
-- 20
20 :: Float
-- 20.0
20 :: Double
-- 20.0
```

Operators that use `Num` **only work with the same type**, however, often haskell can automatically resolve these types to be the same *however* if you use explicit type annotations you can short circuit this behavior.
```haskell
(5 :: Int) * (6 :: Integer)
-- ERROR
```

You can **convert integral numbers to more general numbers** using the `fromIntegral` function. This takes a number that is a member of the `Integral` typeclass and returns a member of the `Num` typeclass.
```haskell
fromIntegral :: (Num b, Integral a) => a -> b
formInrtegral (length [1, 2, 3, 4]) + 3.2
-- 7.2
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ1ODAzMjI3Nl19
-->