---
title: Functions
layout: page
exclude: true
---

There are **two ways to define anonymous functions** in `C#`.

## Delegates

You can **define an anonymous function** using the `Func` object. When declaring a `Func` you should follow it by `< >` angle brackets with the input argument type and return type. You can use standard lambda calculus syntax to define anonymous functions.
```csharp
Func<int, int> Double = x => x * 2
```

You can **define a function that takes another function with a return type as an argument** by using the `Func` delegate object. `Func` delegates **define inputs in the `<>` angle brackets at definition** with the **last type definition in the angle brackets being the output type**. In the example below `MyFunc` is a delegate that takes an `int` and returns an `int`.
```csharp
public void RunThis(int[] arr, Func<int, int> MyFunc)
{
  foreach(int i in arr)
  {
    var result = MyFunc(i);
    Console.WriteLine(result);
  }
}

int[] arr = new int[] {1, 2, 3, 4, 5};
RunThis(arr, x => x * 2); // => 2, 4, 6, 8, 10
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MjAzODIzNDgsNTM2NDE4OTk5LC0xNT
c0NDY4OTMzXX0=
-->