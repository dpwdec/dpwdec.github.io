---
title: Dependency Injection
layout: page
exclude: true
---

You **cannot pass run time parameters into a dependency injected via an IoC**. The graph of objects that depend on each other should be static (and preferably stateless) with runtime data being passed through them with method calls after the entire object graph has been constructed. A class like `MyClass` below which takes a dynamic `string` parameter `name` as an input at construction would *not* be appropriate for dependency injection via an IoC.
```csharp
public class MyClass
{
  public MyClass(string name) { ... }
}
```

**Dependency injection for your project's `IConfiguration` object is automatically set up in during configuration**, you can inject it into any class from the start of your project.

The **general pattern for setting up dependency injection with .NET class** is inject the dependency via the constructor as a normal property and then assign to a `private readonly` field within the class that has the same name but with an `_`.
```csharp
public class User
{
  private readonly IDataConnection _connection;

  public User(IDataConnection connection) // concrete dependency injected here
  {
    _connection = connection;
  }
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NjgzNDYxNjQsLTI1NzI4MzM2LC04Nj
M1Mjk3Nl19
-->