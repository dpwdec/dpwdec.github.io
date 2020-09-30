---
title: Extension Methods
layout: page
exclude: true
---

Extension methods are **methods added to an existing type WITHOUT extending, recompiling or modifying the existing type**. Extension methods are `static`, however, they can be **used as if they were instance methods**. A frequently used example of extension methods is the `Linq` library which adds a range of methods to collection objects using extensions.

You can **define a new extension method for a particular type** by creating a `static` class and defining a `static` method on that class, the first parameter of which specifies the type which the extension method extends preceded by the `this` keyword.
```csharp
namespace ExtensionMethods
{
  public static class MyExtensions
  {
    public static void Print(this String str)
    {
      Console.WriteLine(str);
    }
  }
}
```

You can **call an extension method** by importing the namespace of the extension and then calling it as if it were instance method on the object.
```csharp
using ExtensionMethods;

var str = "Message";
str.Print() // => message
```



<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM4MDIwOTEwNywxNjExODUyMzM0LDg0NT
gwOTA2XX0=
-->