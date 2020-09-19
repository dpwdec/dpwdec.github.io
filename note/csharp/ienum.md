---
title: IEnumerable and IEnumerator
layout: page
exclude: true
---

.NET has a range of keywords that **execute iteration over an `enumerator` of some kind**. These are just structures that like an iterator that support passing out a collection of objects one at a time. For example an `int[]` type is compatible and words as an `enumerator` passing one value at a time time `foreach` procedure to be output. 
```csharp
int[] arr = {1, 1, 2, 3, 5}
foreach(int i in arr)
{
  Console.WriteLine(i); // => 1, 1, 2, 3, 5
}
```

You can **define your own iteratble structures** in C# using the `IEnumerable` and `IEnumerator` interfaces. This is useful because it allows you to directly use iteration on a class and define a custom interface for how that interation takes place as opposed to exposing the iteratable object *within* a class and having to iterate over that.
```csharp
public class NotEnumerable
{
  public int[] arr { get; }
  public NotEnumerable()
  {
    
  }
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY3NzYwNTE2MV19
-->