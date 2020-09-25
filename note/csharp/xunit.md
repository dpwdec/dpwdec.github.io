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

You can **create a new synchronous unit test** by creating a new `void` method and decorating it with the `[Fact]` attribute.
```csharp
public void MyTest_TestingFramework_Passes()
{
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbNzYwMTA3MDYsLTIwNjE3MTY0ODldfQ==
-->