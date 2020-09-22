---
title: Dependency Injection
layout: page
exclude: true
---

The **general pattern for setting up dependency injection with .NET class** is inject the dependency via the constructor as a normal property and then assign to a `private readonly` field within the class that has the same name but with an `_`.
```csharp
public class User 
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNTAwNDAwNTNdfQ==
-->