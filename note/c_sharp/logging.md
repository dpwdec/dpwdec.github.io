---
title: Logging
layout: page
exclude: true
---

Logging for dotnet applications is configured by default in the `CreateDefaultBuilder` method in the `Program.cs` file.

The logging you see when you start a default dotnet application for the first time, something like...
```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on https://localhost:5001
```
is part of logs output by microsoft's default logging behavior and picked up the default configured logging architecture.

You can **customise logging configurations** by appending the `ConfigureLogging` function to the `Host` builder in the `CreateHostBuilder` function. This function takes a `context` and a `logging` object. The `logging` object is **used to configure how logging works**.
```csharp
.ConfigureLogging((context, logging) =>
{
  // logging configuration here.
});
```

You can **clear default logging behavior** by using the `ClearProviders
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcwMzc5MTI2Nyw1NTM0NDQ0OTVdfQ==
-->