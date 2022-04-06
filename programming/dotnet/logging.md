---
title: Logging
layout: page
exclude: true
---

## Default Logging

Microsoft provides a built in logging framework for dotnet applications.

### Overview

Logging for dotnet applications is configured by default in the `CreateDefaultBuilder` method in the `Program.cs` file.

The logging you see when you start a default dotnet application for the first time, something like...
```
info: Microsoft.Hosting.Lifetime[0]
      Now listening on https://localhost:5001
```
...is part of logs output by microsoft's default logging behavior and picked up the default configured logging architecture.

By default, the built in dotnet logger will log to:

- Debug
- Console
- EventSource (?)
- EventLog (?)
- TraceSource (Requires a NuGet package)
- AzureAppServicesFile (Requires a NuGet package)
- AzureAppServicesBlob (Requires a NuGet package)
- ApplicationInsights (Azure Specific) (Requires a NuGet package)

For **anything else**, such as text file logging or SQL server logging you will **have to integrate a third party library**.

The dotnet logging library is **designed to run synchronously** as logging calls should never be long running.

### Configuration

You can **customise logging configurations** by appending the `ConfigureLogging` function to the `Host` builder in the `CreateHostBuilder` function. This function takes a `context` and a `logging` object. 

- The `context` object is **loaded from the `appsettings.json`** and allows you to target different sections of the json file using the `Configuration.GetSection` method.
- The `logging` object is **used to configure how logging works**.
```csharp
.ConfigureLogging((context, logging) =>
{
  // logging configuration here.
});
```

You can **clear default logging behavior** by using the `ClearProviders` method on the `logging` object.
```csharp
logging.ClearProviders();
```

You can **add configuration data from the `context` object** using the `AddConfiguration` method in conjunction with the `context` data. In the example below this will load the entire json object that represents the `"Logging"` section from the `appsettings.json` file and use that as input for the `logging` object's configuration.
```csharp
.ConfigureLogging((context, logging) =>
{
  logging.AddConfiguration(
    context.Configuration.GetSection("Logging")
  );
});
```

You can **specify which sources can be logged to** using the `Add*` methods on the `logging` object. The example below adds *both* console and debug logging, however, if you don't include this then the feature will not be able to log to these channels.
```csharp
logging.AddDebug()
logging.AddConsole()
```

You can **add a category to a piece of a log information** by creating a type on the logger that is created. The example shows a dependency injected `ILogger` with the `MyClass` type.
```csharp
public MyClass(ILogger<MyClass> logger) { ... }
```

This will cause logs emitted by this class' logger to have an identifying log line entry.
```
Info: MyLoggingProject.MyClass[0]
      Log message here
```

You can **add a logging id to your log messages** by adding an integer argument to the logging functions. This defaults to `0`.
```csharp
_logger.LogInformation(1001, "Log message here");
```

Would result in the `[]` changing to accommodate the log id.
```
Info: MyLoggingProject.MyClass[10001]
      Log message here
```

### Logger Levels

There are several levels of logging offered by the default logger.
```csharp
_logger.LogTrace("Log trace");
_logger.LogDebug("Log debug");
_logger.LogInformation("Log information");
_logger.LogWarn("Log warning");
_logger.LogError("log error");
_logger.LogCritical("log critical");
```

- Trace Logs: for detailed views of what is going on, may contain application secrets
- Debug logs: standard debugging logs for application functionality
- Information Logs: standard application flow logs
- Warning logs: for when an error is encountered but can be handled, like handling an exception
- Error logs: for exceptions that might actually crash part of the application and stop a piece of functionality from working, for example a database being uncontactable
- Critical logs: for when the application is actually going to crash entirely

### String interpolation

It's better to **not use direct string interpolation** using the `$` dollar sign interpolation. Instead its better to use classic interpolation with the interpolated arguments added *after* the log line. The reason to do this is that the interpolated "args" array after the log message can be stored by some loggers as data fields that allow you to interrogate the data separately, such as searching for log errors by time. This cannot be done if the field is directly interpolated as a string into the log message. This is generally done when using **structured** or **semantic** logging frameworks.
```csharp
_logger.LogError("Server crashes at {time}", DateTime.Now);
```

## Loggers in testing

If you want to **unit test a class that has a logger in its dependency graph** but functionality of that logger is not required. You can inject a `NullLoggerFactory` from the `Microsoft.Extensions.Logging` library to create a logger with the `CreateLogger` method that requires an arbitrary logger name.
```csharp
using Microsoft.Extensions.Logging;

class MyClass
{
  private readonly ILogger _logger;
  MyClass(ILogger logger)
  {
    _logger = logger;
  }
}

// test code

var myClass = new MyClass(
  new NullLoggerFactory().CreateLogger("null");
)
```