---
title: Using
layout: page
exclude: true
---

You can **ensure an object is limited to a particular scope** by declaring it with the `using` keyword before the block in which it is used.
```csharp
using (MyResource myRes = new MyResource())
{
  myRes.MyMethod(
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbODQyNzY1ODEyXX0=
-->