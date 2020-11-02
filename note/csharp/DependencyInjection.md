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

## IServiceCollection

The `IServiceCollection` is essentially the core of the `IoC` which defines a scoped, key-value relationship between a class or interface and the concrete instance of that class. This is one component that makes up the whole application building framework.

You can **use Microsoft's own version of `IServiceCollection`**, simply called `ServiceCollection` by `using` the `Microsoft.Extensions.DependencyInjection` library. 

You can **configure a set of services for injection** by creating a `new` instance of `ServicesCollection` and then using the scoping methods (`AddTransient`, `AddSingleton` etc.) to define instance-class relationships.
```csharp
var services = new ServicesCollection();
services.AddTransient<IMyInterface, MyClass>();
```

You can **get a new instance of a dependency** from the `ServicesCollection` by *building a provider o* the collection with the
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNjUwNzc5N119
-->