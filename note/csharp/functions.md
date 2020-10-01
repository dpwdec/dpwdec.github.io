---
title: Functions
layout: page
exclude: true
---

You can **define an anonymous function** using the `Func` object. When declaring a `Func` you should follow it by `< >` angle brackets with the input argument type and return type. You can use standard lambda calculus syntax to define anonymous functions.
```csharp
Func<int, int> double = x => x * 2
```

You can **define a function that takes a function as an argument** by using the `Func` delegate object.
```csharp
public void RunThis(int[] arr, Func<int> MyFunc)
{
  foreach(int i in arr)
  {
    MyFunc(i);
  }
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEyNDg5NDYzMywtMTU3NDQ2ODkzM119
-->