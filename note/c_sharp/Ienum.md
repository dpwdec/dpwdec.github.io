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

## IEnumerable

You can **define your own iteratble structures** in C# using the `IEnumerable` and `IEnumerator` interfaces. Sometimes you can do this by implementing an enumerator directly on your class with a custom iteration schema, but often you will just want to **use `IEnumerable` as access for a private iterable property of your class**.

This is useful because it allows you to directly use iteration on an instance of class and define a custom interface for how that interation takes place.
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

Now, when you **use your class that implements `IEnumerable` with a `foreach` or other iterator procedure** it will return the enumeration for a structure *within* the class *AND* the internal collection can remain `private`, as in the example above.

For classes that implement `IEnumerator` within a custom enumeration you can **use `IEnumerable` to return itself** cast to `IEnumerator` which will give the iteration procedure calling it access to the custom defined enumeration methods. 
```csharp
// NOT RECOMMENDED
public class MyEnumerator : IEnumerable, IEnumerator
{
  // -- implementation for custom enumerator here --
  public IEnumerator GetEnumerator()
  {
    // cast this to IEnumerator and return it
    return (IEnumerator) this;
  }
}
```

This is, however, **not recommended**, you should [**separate your `IEnumerable` and `IEnumerator` classes**](https://stackoverflow.com/a/3947874) and ideally **createa a new instance of the `IEnumerator` whenever enumeration is required**. The example below shows an `IEnumerable` implementation that just returns a new hardcoded array of data, however, this could be dynamic using custom `IEnumerator`s, the important thing is that it creates a new instance to return to any iterators.
```csharp
public class MyEnumerable : IEnumerable
{
  public IEnumerator GetEnumerator()
  {
    return new int[] {1, 2, 3, 4, 5};
  }
}
```

## IEnumerator

You can **define your own enumerators** using the `IEnumerator` interface. The signature for this interface uses two methods, `MoveNext` and `Reset`, and a property called `Current`.
```csharp
public interface IEnumerator
{
  public bool MoveNext();
  public void Reset();
  public object Current; 
}
```

The `MoveNext` method **changes a variable that keeps track of the index of enumeration** and **indicates when enumeration is finished** by returning `false`. The `MoveNext` method **runs before a value is retrieved during iteration** therefore, whatever values `MoveNext` changes needs to be out of range before starting. In the example below the `position` variable keeps track of where iteration is and is initialized at `-1` so that when `MoveNext` is called the first time before a retrieval it is at `0` ready to retrieve some information from the collection. The `MoveNext` method also `return`s `true` until the `position` is equal to the `Length` of the data `collection` at which point iteration ends.
```csharp
int position = -1;
public bool MoveNext()
{
  position++;
  return (position < collection.Length);
}
```

The `Reset` method can **describe a procedure for reseting the positional index for iteration**, however, its **not recommended to use it** and is essential a holdover from interoperability into other language aspects. Indeed it is [**now required in the language spec for iterator blocks to throw an exception on Reset**](https://stackoverflow.com/a/3948450) making the method essentially redundant. Below is a quick implementation for completeness sake.
```csharp
public void Reset()
{
  position = -1;
}
```

The `Current` property returns an `object`. This is **only ever an `object` type** and is **cast into the used type when the enumerator is consumed**, for example the `int` specify in the `foreach(int i in arr)` makes this cast. The `Current` property then needs a `get` accessor which returns a value contained in the enumerator based on the current position.
```csharp
public object Current
{
  get
  {
    return _values[position]
  }
}
```

You can also **write the `Current` accessor as a lambda** as with any other `get` property.
```csharp
public object Current => _values[position]
```

## IEnumerable\<T\>

A **generic enumerable** is an object that implements that `IEnumerable` and `IEnumerate` interface while also containing a specific type. For example an `IEnumerable<string>` will be an enumerable structure that returns `string`s as each item during iteration.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAwMjA1NjIyMSwxMzU3NjQwNTgyLDk3MT
k1MTcyOSwxMDE3NDYwNTEzLC0yMDQ3MTg2ODU4LC0xMDc2OTcw
NTQsMTEzMzQxMDkyMiwxODMwNjQzMzUwLDEyMTgzODA4NTAsLT
Y3NzYwNTE2MV19
-->