---
title: Dynamic
layout: page
exclude: true
---

The `dynamic` type is used for **bypassing static type checking**.

You can **convert between dynamic and a concrete types** using a explicit type declaration. If the type cannot be converted, a run time exception will be triggered.
```csharp
dynamic d = 7;
int i = d; // => convert d to int
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNjk3ODgzMjUsLTExODE2MTEzMDZdfQ
==
-->