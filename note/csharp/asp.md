---
title: ASP
layout: page
exclude: true
---

## Razor Pages

Razor pages contain **both a view and model** for each page. The **view is defined using a `.cshtml`file**, and the **model is defined using a standard `.cs` file**. The **naming convention for the model files** is to use `.cshtml.cs`. The example below shows the view and model files together as they appear in a razor pages file structure.
```
index.cshtml
└── index.cshtml.cs
```

To **createa a new razor page** it **must inherit from the `PageModel` class**. This is **imported** using `Microsoft.AspNetCore.Mvc.RazorPages`.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAyOTEwNDE3OF19
-->