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

You can **create a new interface mock** by creating a `Mock` class instance, typed with the interface you want to mock.
```csharp
var mock = new Mock<IMyInterface>();
```

You can **set a mock return value for a method** by using the a `Mock` instance's `Setup` method. This takes a lambda with the object under tests followed by the method and 


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM4MTE3MTAyNiwtMjAyNTI2NzQ2MV19
-->