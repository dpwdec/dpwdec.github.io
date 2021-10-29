---
title: Types
layout: page
exclude: true
---

## Storing Types

You **cannot assign object types directly to variables** in C#, such as for purposes of assertion or checking.
```csharp
public class MyClass { ... }

var myClassType = MyClass; // => Error
```

To **get a reference to a type** use the `typeof` keyword with the type as the argument. You can then use this type for checking, assertions, casting etc.
```csharp
var myClassType = typeof(MyClass);
```

## Type Aliases

You can **alias a type** with a `using` statement with the name of the alias followed by the actual type. 
```csharp
using UserName = System.String;

public static void Main(int[] args)
{
  var x = new Dictionary<UserName, User>();
}
```

This also allows you to **alias conflicting types with the same name** to disambiguate them.
```csharp
using RunEnvironment = System.Environment;
using ModelEnvironment = Models.Environment;
using Deployment.Environment; // this version of environment can be used directly
```