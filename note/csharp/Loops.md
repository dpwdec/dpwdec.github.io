---
title: Loops
layout: page
exclude: true
---

## For

You can **define multiple variables of the same type** in a `for` loop signature by `,` comma separating them.
```csharp
for (int x = 0, y = 0; x < 10; x++)
{
  GetCoord(x, y + x/2);
}
```

You can **define compound boolean expressions** in a `for` loop's conditional field. In the example below the loop will exit when either of the conditions are falsified.
```csharp
for (int x = 0, y = 0; (x < 10 && y < 3); x ++)
{
  GetCoord(x, y + x/2);
}
```

```csharp
for (int x = 0, y = 0; (x < 10 || y < 3); x ++)
{
  GetCoord(x, y + x/2);
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMxMTAzNjg2NF19
-->