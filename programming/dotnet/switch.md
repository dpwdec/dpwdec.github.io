---
title: Switch
layout: page
exclude: true
---

You can **match two cases to the same branch** by placing them directly above one another.
```csharp
switch (x)
{
    case 1:
    case 2:
        // do something
    break;
    case 3:
        // do something else
    break;
}
```