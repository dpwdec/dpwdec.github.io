---
title: XUnit
layout: page
exclude: true
---

XUnit is an iteration on NUnit. 

By default XUnit **runs tests in parallel**.

There is a convention to **name the object you are testing** with a `private readonly` property called `_sut` which stands for **system under test**.
```csharp
private readonly MyClass _sut;
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM0OTUxNDQ2NywtMjA2MTcxNjQ4OV19
-->