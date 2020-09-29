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

XUnit **creates a new instance of the test class for each test that is run** therefore, you can **place set up for the tests inside the class body or constructor**.
```csharp
public class MyTestClass
{
  // class body set up here, such as mocks or other dependencies
  private readonly _myObject = new MyObject();

  public MyTestClass()
  {
    // constructor set up here
  }

  // ... individual tests ...
}
```

## Test Types

There are **two major types of test in XUnit**: `Fact` and `Theory` tests. 

`Fact` tests are **invariant and always true**, they do not support dynamic inputs.

`Theory` tests are **true for a particular set of data** passed into them.

### Fact Tests

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

### Theory Tests

You can **create a test with multiple inputs** by marking the test with the `[Theory]` attribute. Data is then passed in using the `[InlineData]` attribute which takes parameters to the test method as arguments.
```csharp
[Theory]
[InlineData(1)]
[InlineData(0)]
public void MyTheory(int value)
{
  Assert.Equal(1, value);
}
```

## Assert

You can **assert that something is true** by using the `True` method.
```csharp
Assert.True(true);
```

You can **assert that two things are equal** with the `Equal` method, the **arguments are passed in the order of `expected` and then `actual`**. 
```csharp
Assert.Equal(1, 1);
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA0MzE4NjcyMSwtNjEyNjkyMTksMTEyMT
M5NDcwLDU2NTc4MDYyMiwtMTU5NzMyMTg3MywyMTE4OTQ4NTEx
LC0yMDYxNzE2NDg5XX0=
-->