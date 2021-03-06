---
title: Moq
layout: page
exclude: true
---

Moq is a mocking framework for unit testing. You can **install Moq** by installing the `Moq` Nuget package.

You can **use Moq in a test suite** by using the `Moq` namespace.
```csharp
using Moq;
```

You can **run initialisation behaviour on mock objects AFTER passing them in as dependencies during testing**. In the example below the `MyDependent` has a mock version of `IMyInterface` injected into it, but the set up that needs to be done for that specific mock is not carried out until `SomeTestMethod` is called.
```csharp
var mock = new Mock<IMyInterface>();
var dependent = new MyDependent(mock.Object);

public void SomeTestMethod()
{
  mock.Setup(// .. do set up of mock)
  // make assertions
}
```

## Mock Objects

You can **create a new interface mock** by creating a `Mock` class instance, typed with the interface you want to mock.
```csharp
var mock = new Mock<IMyInterface>();
```

You can **create a new class mock** by creating a `Mock` class instance, typed with the class you want to mock. Unlike interfaces **classes must be `public` and any mocked methods must be marked as `virtual`**.
```csharp
// mockable class
public class MyClass
{
  public virtual int DoSomething()
  {
    return 10;
  }
}

var mock = new Mock<MyClass>();
```

## Mock Methods

The **`Mock` class wraps an instance of mocked structure and allows for configuration**, it **cannot directly be used AS an instance**, instead, to **access the mock instance and use it as a dependency or to make assertions against** use the `Object` property of the `Mock` object.
```csharp
var mock = new Mock<IMyInterface>();
// passing in a mock instance of IMyInterface as a dependency to MyDependent
var dependent = new MyDependent(mock.Object);
// access method on mock instance of IMyInterface
var myInterface = mock.Object.MyMethod();
```

You can **set a mock return value for a method and particular input** by using the a `Mock` instance's `Setup` method. This takes a lambda with the object under tests followed by the method and input parameters, the result of this then calls a `Returns` method where the mock return type is specified. The example below specifies that when `MyMethod` is called with the argument `"input"` it should return `200`.
```csharp
mock.Setup(x => x.MyMethod("input")).Returns(200);
```

You can **define multiple returns for different input values**. If you use an undefined input moq will use the first defined return type.
```csharp
mock.Setup(x => x.MyMethod("input")).Returns(200);
mock.Setup(x => x.MyMethod("output")).Returns(300);

mock.Object.MyMethod("input"); // => 200
mock.Object.MyMethod("output"); // => 300
mock.Object.MyMethod("other"); // => 200
```

# It

You can **use the `It` object to help make mock input and output mappings more semantically clear** when defining mock rules for a test.

You can **make define output for ANY valid input** by using the `IsAny` method with the type that would be passed in. The example below defines behaviour for this mock that *any* `string` passed into the method will return `null`;
```csharp
mock.SetUp(x => x.MyMethod(It.IsAny<string>)).Returns(null);
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk3NTQ5MjI5LC0zMTUzOTU5NDYsMTk2Mz
A1OTIwMCw2NTkyNjU0MzQsLTE1OTgyMzM3NjcsLTUyNjYzNzIw
LC0yMDI1MjY3NDYxXX0=
-->