---
title: Automapper
layout: page
exclude: true
---

Automapper is a system for creation of **Domain Transfer Objects** as part of your system. It's recommended to use the `Extensions` version of this library which has `Automapper` base as one of its dependencies.
```bash
$ dotnet add package AutoMapper.Extensions.Microsoft.DependencyInjection
```

You can **set up automapper with you project** using the `services` object in the `StartUp` class's `ConfigureServices` method and passing in the `AppDomain.CurrentDomain.GetAssemblies()

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg4MjcwMjcyMCwtMTgzODU0OTk2MV19
-->