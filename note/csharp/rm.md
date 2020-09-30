---
title: Resource Management
layout: page
exclude: true
---

## Using

The `using` keyword can be used as a syntax for **deterministically managing the scope of an object**. The use of `using` with a scoped resource forces the resource to be released at the end of the scope that the resource is valid for. Normally you would have to wait for the garbage collector to decide the resource was not being used and dispose of it, but `using` gives an explicit direction that the resource is no longer needed and any reference to it can be removed from the current run time. 

Resource management with `using` **does not free the memory** but it does help with managing limited pools of resources (for example database connections) by marking unneeded resources allowing for the resource pool to be replenished. An object which falls out of scope and owns resources, which is then garbage collected will never has its resources released because the **garbage collector is not responsible for resource management**. For example, in the database connections example, the database connection pool will never receive a message that a garbage collected connection from its pool is done with the connection if the memory for that resource is disposed of *without* it releasing its resources.

Resource management with `using` only works with **only work with objects that implement the `IDisposable` interface**. This interface contains a single method `Dispose` that is **called automatically when the resource declared with `using` goes out of scope**, disposing of it.

The use of `using` within methods, for resource management, is **completely separate from `using` for imports** at the top of a file.

### Using blocks

`using` blocks are one **syntax for deterministically describing the scope of an object**. You can **ensure an object is limited to a particular scope** by declaring it with the `using` keyword before the block in which it is used. This will cause the object's resources to be released at the end of the block.
```csharp
using(MyObject myObject = new MyObject())
{
  myObject.MyMethod();
}
// myObject is disposed (Dipose() called implicitly)
```

You can **define multiple using scope declarations in a single statement** by separating the declarations. You don't have to use nested `using` statements. 
```csharp
using(System.IO.StreamReader r = new System.IO.StreamReader(""), r2 = new System.IO.StreamReader(""))
{
  // use stream readers
}
```

### Using variables

You can also **limit object scope within a block** by placing the `using` statement within an already existing scope. The object will then be disposed of when the program exits that scope. This is a newer syntax version of the `using` blocks above for greater ease of resource management.
```csharp
if(true)
{
  using var myObject = new MyObject();
}
// myObject is disposed (Dipose() called implicitly)
```

## Try / Finally Equivalents

`using` blocks are similar to a `try { } finally { }` block where something is used in the `try` and then disposed of in the `finally`.  Thus, the following example:
```csharp
var con = new SqlConnection();
try
{
  con.execute();
}
finally
{
  con.Dispose();
}
```

Is roughly equivalent to the example below where the `Dispose` method is called implicitly by `using`. The main difference being that `using` **ensures that `Dispose` is called *even* when an exception occurs**.
```csharp.
using(SqlConnection con = new SqlConnect())
{
  con.execute();
}
```

## Finalizer

A finalizer is an **optional method which executes when an object is garbage collected**. Adding a finalizer to an object is **optional**.

If an object does have a finalizer the **finalizer method is added** to a **finalization queue** during garbage collection. This **adds significant overhead to the GC** which means you should **only use it as a safety net for freeing unmanaged resources**. The finalizer exists **in case the user of an `IDisposable` doesn't correctly release its resources**.

You can **create a finalizer method for a class** with the name of the class preceded by a `~` tilde with no arguments.
```csharp
public class MyClass
{
  ~MyClass()
  {
    // finalization logic
  }
}
```

## IDisposable

The `IDisposable` interface **implements a single method called `Dipose`** which is **called automatically when a resource managed object that implements it goes out of scope**. 

If an object implements `IDisposable` this is an indication that it **holds some valuable resource** and **should be released** when possible. It's up the resource consumer to correctly release the resource with the `Dispose` method.
```csharp
public interface IDisposable
{
  void Dispose();
}
```






<!--stackedit_data:
eyJoaXN0b3J5IjpbNDk3ODYxMjY3XX0=
-->