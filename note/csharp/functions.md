---
title: Functions
layout: page
exclude: true
---

There are **two ways to define anonymous functions** in `C#`:

- **Delegates**, which take a list of arguments greater than or equal to 0 *and* have a return type
- **Actions**, which take a list of arguments greater than or equal to 0 *and* have no return type

## Delegate

You can **define an anonymous delegate function with a return type** by using the `Func` object. `Func` takes some number of arguments and returns something. When declaring a `Func` you should follow it by `< >` angle brackets with the input argument type and return type. You can use standard lambda calculus syntax to define anonymous functions.
```csharp
Func<int, int> Double = x => x * 2
Func<int> Three = () => 3 // delegate that takes no arguments
```

You can **use lexical scopes with delegates**.
```csharp
var y = 20;

Func<int, int> Mult = x =>
{
  return x;
};
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

## Action

**Many of the rules that apply to delegates also apply to actions**, so unless functionality is specifically stated assume that they overlap.

You can **define an anonymous function without a return type** by using the `Action`. `Action` takes some number of arguments are returns `void`. You can **define an `Action`** by using the `Action` type followed by `< >` angle brackets with the argument types in them.

```csharp
Action<int> EchoInt = i => Console.WriteLine(i);
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNDQ4MjQ0NCwxNDk4NTgyMjg1LC0xMD
c0NDg4MTk3LDUzNjQxODk5OSwtMTU3NDQ2ODkzM119
-->