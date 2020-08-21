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
  // test code here
}
```

You can **indicate test methods** with the `[Test Method]` decorator. The **convention for**
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgwMzk5NjM0NiwtMjAyMDU1NzQyMywtMT
c4OTc1MTk5OV19
-->