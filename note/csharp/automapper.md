---
title: Automapper
layout: page
exclude: true
---

Automapper is a system for creation of **Domain Transfer Objects** as part of your system. It's recommended to use the `Extensions` version of this library which has `Automapper` base as one of its dependencies.
```bash
$ dotnet add package AutoMapper.Extensions.Microsoft.DependencyInjection
```

You can **set up automapper with you project** using the `services` object in the `StartUp` class's `ConfigureServices` method and passing in the `AppDomain.CurrentDomain.GetAssemblies()`. *But what is AppDomain?*
```csharp
public void ConfigureServices(IServiceCollection services)  
{  
  // makes automapper available via dependency injection to the rest of our application  
  services.AddAutoMapper(AppDomain.CurrentDomain.GetAssemblies());
}
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgwNDIwMzQ1LC0xODM4NTQ5OTYxXX0=
-->