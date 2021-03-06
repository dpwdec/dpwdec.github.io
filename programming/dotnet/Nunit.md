---
title: NUnit
layout: page
exclude: true
---

To **make NUnit tests runnable in visual studio** you also need to install the `NUnit3TestAdapter`. This allows visual studio's test runner to recognise the NUnit tests.

You can **add a new testing project** by `RMB` clicking on the project file and going to `Add -> New Project` and then selecting the `C# -> Tests` section and choosing a test project. The **accepted naming convention for these projects** is `NameOfProject.UnitTests`, or some other test descriptor separate by a `.` period.

You can **indicate test classes** by using the `[TestFixture]` decorator. The **convention for test class naming** is `NAME_OF_CLASSTests` so if we were testing a class called `User` the associated test class would be `UserTests`. 
```csharp
using NUnit.Framework;

[TestFixture]
public class MyClassTests
{
  // test methods here
}
```

You can **indicate test methods** with the `[Test]` decorator. The **convention for naming test methods** is the form `TestName_Scenario_ExpectedResult`.
```csharp
[Test]
public void MyMethod_IsTrue_ReturnsName
{
  // test method code here
}
```

Test methods should **follow an Arrange, Act, Assert** test pattern. First you arrange any test set up, then you run your code, then you make an assertion against the result.
```csharp
[Test]
public void IsAdult_AgeGreaterThan18_ReturnsTrue
{
  // Arrange
  var user = new User();

  // Act
  result = user.IsRegistered();

  // Assert
  Assert.IsTrue(result);
}
```

## Assertions

You can **make assertions using the `Assert`** object followed by a matcher object. 

You can **add hardcoded passing test skips** by using the `pass` method on the `Assert` object.
```csharp
[Test]
public TestWillAlwaysPass()
{
  Assert.pass();
}
```

You can **assert that something is true** in several ways: 
- Using the `IsTrue` method on `Assert`. 
- Using the `That` method of `Assert` with a boolean evaluating expression. 
- Using the `That` method of `Assert` with a boolean property on the `Is` object as an argument.

All of these essentially evaluate to the same thing but just offer better semantic information on the purpose of the test.
```csharp
Assert.IsTrue(result);
Assert.That(result == true);
Assert.That(result, Is.True);
```

You can **assert that two things are equal** by using the boolean matchers above.
```csharp
int i = 1;
Assert.IsTrue(i == 1);
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMzOTY4NDQyNCwtNTQ1MTk1NjU1LDE0NT
Y5MzA3MzQsLTE0MDUxMDEwNjAsLTE3MzIwNzI1NzQsMTIzNDQ1
ODg0NiwtMjAyMDU1NzQyMywtMTc4OTc1MTk5OV19
-->