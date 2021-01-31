---
title: Resource Management
layout: page
exclude: true
---

## Storing Types

You **cannot assign object types directly to variables** in C#, such as for purposes of assertion or checking.
```csharp
public class MyClass { ... }

var myClassType = MyClass; // => Error
```

To **get a reference to a type** use the `typeof` keyword with the type as the argument. You can then use this type for checking, assertions, casting etc.
```csharp
var myClassType = typeof(MyClass);
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcwODk3NDkxMl19
-->