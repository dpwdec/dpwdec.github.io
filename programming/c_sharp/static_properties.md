---
title: Static Properties
layout: page
exclude: true
---

You can **return static values from a class that requires construction** i.e. *not primitive types* by opening a block with `{}` curly brackets and then defining a `get` block which returns the value.
```csharp
public class ValueHolder
{
    public static List<int>() SomeNumbers
    {
        get
        {
            return new List<int>() { 1, 2, 3, 4, 5 };
        }
    }
}
```