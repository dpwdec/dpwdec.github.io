---
title: Using
layout: page
exclude: true
---

You can **ensure an object is limited to a particular scope** by declaring it with the `using` keyword before the block in which it is used. 
```csharp
using (MyObject myObject = new MyResource())
{
  myRes.MyMethod();
}
// myRes is disposed
```

You can also **limit resource scope** 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYxODUwNjIzNF19
-->