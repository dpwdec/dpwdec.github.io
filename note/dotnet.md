---
title: .NET
layout: page
exclude: true
---

You can **create a new console application** by using `dotnet new` command with the `console` type argument. This command creates a new console output project in the folder where the command in called.
```bash
$ dotnet new console
```

## Classes

You can **define a class** by using the `class` keyword followed by the name of the class written in `PascalCase`.
```csharp
class MyClass
{
  // class stuff
}
```

You can **define a class constructor** by defining a method inside the class that matches the name of the class definition. The `this` keyword is used to define instance variable assignment.
```csharp
public MyClass(string name, int age)
{
  this.name = name;
  this.age = age;
}
```

### Instances

You can **create a new instance of a class** by using the `new` keyword with the class name and valid constructor.
```csharp
var myClass = new MyClass("Lonathan", 100);
```

### Permissions

**Public variables are accessible and mutable by external code by default.** If you define a public variable on a class then it *can* be modified by external code.
```csharp
public MyClass
{
  public string name;
}

var myClass = new MyClass();
myClass.name = "Lomothy"; // completely accessible
```

You can **control permissions on public variables** using `get` and `set` syntax after the variable definition. In the example below external code can still `get` and `set` name, however, if external code tries to change the value of `id` it will trigger a `readonly` error.
```csharp
public MyClass
{
  public string name { get; set; }
  public int id { get; }
}
```

**Private variables are only accessible from within the class they are defined in**.
```csharp
public MyClass
{
  public string name { get; set; }
  public int id { get; }
}
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkwODI0MzA0Miw4MjEyNzg2NDUsLTE4NT
UyOTMzOTIsNDM2NDQwNjYyXX0=
-->