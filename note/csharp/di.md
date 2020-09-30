---
title: Dependency Injection
layout: page
exclude: true
---

You **cannot pass run time parameters into a dependency injected via an IoC**. The graph of objects that depend on each other should be static (and preferably stateless)

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
eyJoaXN0b3J5IjpbNzk1OTIzNTg0LC0yNTcyODMzNiwtODYzNT
I5NzZdfQ==
-->