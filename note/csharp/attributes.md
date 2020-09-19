---
title: Attributes
layout: page
exclude: true
---

Attributes are a meta programming method for adding metadata to methods and classes or even entire program structures like assemblies and modules.

This allows you to interact with the C# compiler in specific ways or add extra structural changes to your program as it runs.

## Applying Attributes

You can **use an attribute on a target structure in your program** by including it directly before the definition of that structure in `[]` square brackets.
```csharp
[MyAttribute]
class MyClass
{
  [MyAttribute]
  string MyProperty { get; set; }
  
  [MyAttribute]
  void MyMethod() { ... }
}
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MDE4MjU2MzgsMTg5MzMyODU1NywxNj
ExNzMxNF19
-->