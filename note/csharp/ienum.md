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

You can **define your own iteratble structures** in C# using the `IEnumerable` and `IEnumerator` interfaces. This is useful because it allows you to directly use iteration on an instance of class and define a custom interface for how that interation takes place.
```csharp
// NotEnumerable.cs
public class NotEnumerable
{
  public int[] arr { get; }
  public NotEnumerable()
  {
    arr = int[] {1, 2, 3, 4, 5}
  }
}
```

Otherwise you have to access the enumerable object *within* a class and iterate over that instead.
```csharp
// Program.cs
var ne = new NotEnumerable();
foreach(int i in ne.arr)
{
  // do something with contents of arr
}
```

The `IEnumerable` interface is used to **define a structure that supports enumeration with `IEnumerator`.** The `IEnumerable` interface contains a single method signature `GetEnumerator` that returns an `IEnumerator` which contains the methods that actually support enumeration. This the method that enumeration procedures like `foreach` check for, before iterating through a collection.
```csharp
public interface IEnumerable
{
  IEnumerator GetEnumerator();
}
```

To **implement `IEnumerable` on a class** you can return the enumerable result of `GetEnumerator` on the enumerable structure within the class when implementing the `IEnumerable` interface.
```csharp
public class IsEnumerable : IEnumerable
{
  private int[] arr;
  public IsEnumerable()
  {
    arr = int[] {1, 2, 3, 4, 5}
  }
  public IEnumerator GetEnumerator()
  {
    return arr.GetEnumerator();
  }
}
```

Now, when you **use your class that implements `IEnumerable` with a `foreach` or other iterator procedure** it will return the enumeration for a 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkyMzkwOTc4LDExMzM0MTA5MjIsMTgzMD
Y0MzM1MCwxMjE4MzgwODUwLC02Nzc2MDUxNjFdfQ==
-->