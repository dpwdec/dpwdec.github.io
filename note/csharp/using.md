---
title: Using
layout: page
exclude: true
---

*When using is used with imports of namespaces at the top of a file. How does that work?*

## Using Blocks

You can **ensure an object is limited to a particular scope** by declaring it with the `using` keyword before the block in which it is used. 
```csharp
using(MyObject myObject = new MyObject())
{
  myObject.MyMethod();
}
// myObject is disposed
```

You can **define multiple using scope declarations in a single statement** by separating the declarations. You don't have to use nested `using` statements. 
```csharp
using(System.IO.StreamReader r = new System.IO.StreamReader(""), r2 = new System.IO.StreamReader(""))
{
  // use stream readers
}
```

You can also **limit object scope within a block** by placing the `using` statement within an already existing scope. The object will then be disposed of when the program exits that scope.
```csharp
if(true)
{
  using var myObject = new MyObject();
}
// myObject is disposed
```

## Try / Finally Equivalents

`using` blocks are actually shorthand for a `try { } finally { }` block where something is used in the `try` and then disposed of in the `finally`.  Thus, the following example:
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

Is equivalent to the example below where the `Dispose` method is called implicitly by `using`
```csharp
using(SqlConnection con = new SqlConnect())
{
  con.execute();
}
```

## IDisposable

For an object to **work with a `using` block** it must **implement the `IDisposable` interface**. This interface contains a single method `Dispose` that is used for getting rid of the object.


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjc5MDQ1OTQ4LDEyMDM4NDY4MDBdfQ==
-->