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

## Test Categories

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

You can **create a test with multiple test contexts** by marking the test with the `[Theory]` attribute. Data is then passed in using the `[InlineData]` attribute which takes parameters to the test method as arguments. In the example below the test will pass during its first run and then fail during its second run because the value of `input` will first be set to `0` from the first `InlineData` and then to `1` from the second `InlineData`.
```csharp
[Theory]
[InlineData(0)]
[InlineData(1)]
public void MyTheory(int input)
{
  Assert.Equal(0, input);
}
```

You can **test data sets with multiple pieces of data** by comma separating arguments to `InlineData` and defining arguments to the test method in the same order.
```csharp
[Theory]
[InlineData(0, true, "hello")]
public void MyTheory(int n, bool b, string s)
{
  // use n, b and s in your test
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

You can **assert against an object's type** by using the `BeOfType` method in combination with the `typeof` keyword.
```csharp
var myString = "Watermelon";
myString.Should().BeOfType(typeof(string));
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUzNjUzMzY5OCwtODc5MTczOTM3LC0xOT
E2NTAwMDM4LC02MTI2OTIxOSwxMTIxMzk0NzAsNTY1NzgwNjIy
LC0xNTk3MzIxODczLDIxMTg5NDg1MTEsLTIwNjE3MTY0ODldfQ
==
-->