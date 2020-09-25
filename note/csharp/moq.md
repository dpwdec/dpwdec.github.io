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




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU3NDYxMTk3MSwtMjAyNTI2NzQ2MV19
-->