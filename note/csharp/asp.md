---
title: ASP
layout: page
exclude: true
---

## Project

You can **access your project's configuration file** which is found in the corresponding project's `.csproj` file by going to the project file in the solution browser, then `RMB (on Project) -> Edit Project File`.

If you **add a NuGet package or dependency** this will be reflected in the project's `.csproj` file with an `ItemGroup` with a `PackageReference` specifying the project's dependencies.
```xml
<ItemGroup>  
  <PackageReference  Include="SomeDependency"  Version="x.x.x"  />  
</ItemGroup>
```

You can **configure how your web application runs** such as the *port* it runs on, or its *environment variables* using the `priopreties/launchSettings.json` file in your project.

You can **define different profiles here with which to run your application** which change how the application is built and operated when developing. For example you may want to define a *debug* profile with specific variables to debug an application, or you may want to develop something using a *release-like* profile.

You should **store static files for your website** in the `wwwroot` folder within your project. This contains static dependencies like `JavaScript` and `CSS`.

## Razor Pages

The **primary code** for a razor pages application is contained in the `Pages` directory.

Razor pages contain **both a view and model** for each page. The **view is defined using a `.cshtml`file**, and the **model is defined using a standard `.cs` file**. The **naming convention for the model files** is to use `.cshtml.cs`. The example below shows the view and model files together as they appear in a razor pages file structure.
```
index.cshtml
└── index.cshtml.cs
```

To **createa a new razor page** it **must inherit from the `PageModel` class**. This is **imported** by `using Microsoft.AspNetCore.Mvc.RazorPages`.
```csharp
using Microsoft.AspNetCore.Mvc.RazorPages;

public class MyModel : PageModel
{
  // page model here
}
```

### Shared

You can **create layout and page partials** in the the project's `Pages/Shared` folder. The **naming convention for these files** is to start with an `_` underscore, such as `_Layout.cshtml`. 

You can **define the master layout for your application** by using the `_ViewStart.cshtml` file and setting the `Layout` variable equal to the name of the partial you want to use from your `Shared` folder.
```csharp
@{
  Layout = "_Layout";
}
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbODYyNzEyMzc3LDE5MzUyNTE3NjYsMTM4ND
A4NzIwNiwtNjM4NDM1MDM3XX0=
-->