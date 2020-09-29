---
title: Using
layout: page
exclude: true
---

You can **ensure an object is limited to a particular scope** by declaring it with the `using` keyword before the block in which it is used. 
```csharp
using (MyObject myObject = new MyObject())
{
  myObject.MyMethod();
}
// myObject is disposed
```

You can also **limit object scope within a block** by placing the `using` statement within an already existing scope. The object will then be disposed of when the program exits that scope.
```csharp
if(true)
{
  using var myObject = new MyObject();
}
// myObject is disposed
```

*Can I use using with a*
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjk4NDU5ODg4XX0=
-->