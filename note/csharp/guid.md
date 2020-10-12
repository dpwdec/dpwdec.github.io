---
title: Guid
layout: page
exclude: true
---

A `Guid` is a **globally unique identifier**. A `Guid` is a `128` bit integer with `5,316,911,983,139,663,491,615,228,241,121,400,000` possible unique combinations. 

A `Guid` **can be used to uniquely identify something in your system**, it has a very low probability of being replicated. A `Guid` can **only contain alphanumeric characters *and* the `-` hyphen character**.

Because the `Guid` has such a low chance of being replicated it is useful in domains that contain many independent systems or clients that need unique identifiers for their data or objects. It is also useful for systems that use caching (or scavenging) as each object instance can also have a unique identifier.

You can **create a new `Guid`** by using the `static` method on the `Guid` class, `NewGuid()`. This will generate an entirely new random `Guid`. You **should not use the `new` keyword** to generate a `Guid`, doing so will result in an empty `Guid` with all characters set to `0`.
```csharp
var MyGuid = Guid.NewGuid();
```



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgzMDU2MjEzMiwxODE4NjcwNzUxLDE5OD
IyNjIyMjNdfQ==
-->