---
title: Extension Methods
layout: page
exclude: true
---

Extension methods are **methods added to an existing type WITHOUT extending, recompiling or modifying the existing type**. Extension methods are `static`, however, they can be **used as if they were instance methods**. A frequently used example of extension methods is the `Linq` library which adds a range of methods to collection objects using extensions.

You can **define a new extension method for a particular type** by defining a `static` method the first parameter of which specifies the type which the extension method extends preceded by the `this` keyword.
```csharp
public static void PrintMe(this String str)
{
  Console.WriteLine(
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc1MTExODcxMSw4NDU4MDkwNl19
-->