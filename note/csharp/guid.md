---
title: Guid
layout: page
exclude: true
---

A `Guid` is a **globally unique identifier**. A `Guid` is a `128` bit integer with `5,316,911,983,139,663,491,615,228,241,121,400,000` possible unique combinations. A `Guid` **can be used to uniquely identify something in your system**, it has a very low probability of being replicated.

You can **create a new `Guid`** by using the `static` method on the `Guid` class, `NewGuid()`. This will generate an entirely new random `Guid`. You **should not use the `new` keyword** to generate a `Guid`, doing so will result in an empty `Guid` w
```csharp
var MyGuid = Guid.NewGuid();
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbNTgzODI0NjE5LDE5ODIyNjIyMjNdfQ==
-->