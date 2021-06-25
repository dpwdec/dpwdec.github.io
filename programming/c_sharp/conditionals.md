---
title: Conditionals
layout: page
exclude: true
---

You can **write a single line return clause from an `if` condition WITHOUT an `{}` curly braces** by simply separating an if condition by a space and then writing the return.
```csharp
int returnAnInt(string x) {
    if (x == null) return 0; // single line return
    return 9;
}
```