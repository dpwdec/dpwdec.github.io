---
title: Using
layout: page
exclude: true
---

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



*Can I use using with an actual library or is specifically for objects?*


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2NzY5NjE4MF19
-->