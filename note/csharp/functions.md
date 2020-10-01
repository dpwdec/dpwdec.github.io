---
title: Functions
layout: page
exclude: true
---

You can **define an anonymous function** using the `Func` object. When declaring a `Func` you should follow it by `< >` angle brackets with the input argument type and return type. You can use standard lambda calculus syntax to define anonymous functions.
```csharp
Func<int, int> double = x => x * 2
```

You can **define a function that takes a function as an argument** by using the `Func` object with its return type elided as an argument for the function.
```csharp
public void RunThis(
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbODQyMzcxOTM1XX0=
-->