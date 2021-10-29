---
title: Reflection
layout: page
exclude: true
---

You can **get the value of a property on an object by the property's string name** using the `GetProperty` method with your object's type and instance. This is not recommended, but can be useful if you need to interact with a user or input that specifies how it wants to interact with data through strings.
```csharp
var x = typeof(ObjectType).GetProperty("PropertyName").GetValue(objectInstance);
```

You can **set the value of a property on an object by the property's string name** using the `SetValue` method.
```csharp
var x = typeof(ObjectType).GetProperty("PropertyName").SetValue(objectInstance, "value");
```