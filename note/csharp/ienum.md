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

You can **define your own iteratble structures** in C# using the `IEnumerable` and `IEnumerator` interfaces. This is useful because it allows you to directly use iteration on 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5Njc1ODA1MF19
-->