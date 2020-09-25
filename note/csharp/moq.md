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

The **`Mock` class wraps an instance of mocked structure and allows for configuration**, it **cannot directly be used AS an instance**, instead, to **access the mock instance and use it as a dependency or to make assertions against** use the `

You can **set a mock return value for a method and particular input** by using the a `Mock` instance's `Setup` method. This takes a lambda with the object under tests followed by the method and 


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzMzA2OTI5OSwtNTI2NjM3MjAsLTIwMj
UyNjc0NjFdfQ==
-->