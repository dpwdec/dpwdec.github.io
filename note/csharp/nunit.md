---
title: NUnit
layout: page
exclude: true
---

You can **add a new testing project** by `RMB` clicking on the project file and going to `Add -> New Project` and then selecting the `C# -> Tests` section and choosing a test project. The **accepted naming convention for these projects** is `NameOfProject.UnitTests`, or some other test descriptor separate by a `.` period.

You can **indicate test classes** by using the `[Test Class]` decorator. The **convention for test class naming** is `NAME_OF_CLASSTests` so if we were testing a class called `User` the associated test class would be `UserTests`. 
```csharp
[Test Class]
public class MyClassTests
{
  // test methods here
}
```

You can **indicate test methods** with the `[Test Method]` decorator. The **convention for naming test methods** is the form `TestName_Scenario_ExpectedResult`.
```csharp
[Test Method]
public void MyMethod_IsTrue_ReturnsName
{
  // test method code here
}
```

Test methods should **follow an Arrange, Act, Assert** test pattern. First you arrange any test set up, then you run your code, then you make an assertion against the result.
```csharp
[Test Method]
public void IsAdult_AgeGreaterThan18_ReturnsTrue
{
  // Arrange
  var 
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNTQyNzE5NTAsLTE3MzIwNzI1NzQsMT
IzNDQ1ODg0NiwtMjAyMDU1NzQyMywtMTc4OTc1MTk5OV19
-->