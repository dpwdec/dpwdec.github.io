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

XUnit **creates a new instance of the test class for each test that is run** therefore, you can **place setup for the tests inside the class body or constructor**.
```csharp

```

You can **create a new synchronous unit test** by creating a new `void` method and decorating it with the `[Fact]` attribute.
```csharp
[Fact]
public void MyTest_TestingFramework_Passes()
{
  Assert.True(true);
}
```

You can **skip a test** by adding `Skip` as an argument to the `[Fact]` attribute and setting it equal to a string detailing why the test is skipped.
```csharp
[Fact(Skip = "Redundant Test")]
public void MyTest_TestingFramework_Passes()
{
  Assert.True(true);
}
```

## Assert

You can **assert that something is true** by using the `True` method.
```csharp
Assert.True(true);
```

You can **assert that two things are equal** with the `Equal` method.
```csharp
Assert.Equal(1, 1);
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQwNTQ0ODA2OCwyMTE4OTQ4NTExLC0yMD
YxNzE2NDg5XX0=
-->