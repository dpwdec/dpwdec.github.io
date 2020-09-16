---
title: ASP
layout: page
exclude: true
---

## Project

You can **access your project's configuration file** which is found in the corresponding project's `.csproj` file by going to the project file in the solution browser, then `RMB (on Project) -> Edit Project File`.

If you **add a NuGet package or dependency** this will be reflected in the project's `.csproj` file with an `Item

## Razor Pages

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


<!--stackedit_data:
eyJoaXN0b3J5IjpbNTYzMDg5NDUzXX0=
-->