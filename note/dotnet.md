---
title: .NET
layout: page
exclude: true
---

You can **create a new console application** by using `dotnet new` command with the `console` type argument. This command creates a new console output project in the folder where the command in called.
```bash
$ dotnet new console
```

## Strings

You can **convert a number to a string** using the `ToString` method.
```csharp
int numberInt = 5;
string numberString = numberInt.ToString();
```

## List

The `List` is a data structure that offers a resizable list of elements. To **start using the `List` data structure** you must import `using  System.Collections.Generic`. The `List` object is defined with a generic `T` type as `List<T>` which you must supply when constructing a new list object. To **create a new list** use the `new` keyword as you would with any new object instance with the type of the container in `< >` brackets. You **initialize the contents of a list inline** by containing the content in `{ }` curly brackets after the definition.
```csharp
using  System.Collections.Generic;

var names = new List<string> { "John", "James", "Jacob" };
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

You can **define a static "class" variable** by using the `static` keyword. This is shared amongst ALL instances of the class, when it is mutated on the class it changes for all instances. These can also be assigned *within* the class they are defined in.
```csharp
class MyClass
{
  static string ClassName = "My Class";
}
```

### Instances

You can **create a new instance of a class** by using the `new` keyword with the class name and valid constructor.
```csharp
var myClass = new MyClass("Lonathan", 100);
```

You can **initialise default class member values** from within the body of the class.
```csharp
class MyClass
{
  public int distance = 40;
}

var myClass = new MyClass();
myClass.distance; // => 40
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
  public string Name { get; set; }
  public int Id { get; }
}
```

**Private variables are only accessible from within the class they are defined in**. Some developers like to go further and prefix private variables with an `_` underscore as well.
```csharp
public MyClass
{
  private int SecretNumber; // not accessible outside of the class
}
```

## Functions

You can **define an anonymous function** using the `Func` object. When declaring a `Func` you should follow it by `< >` angle brackets with the input argument type and return type. You can use standard lambda calculus syntax to define anonymous functions.
```csharp
Func<int, int> double = x => x * 2
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM4MzA5MjExNCwtMTQwMTMxMTI5MCwxMD
ExMDE4NjA1LC00NDUzNjk5NzUsMTI4NTc4NDU3Niw4MjEyNzg2
NDUsLTE4NTUyOTMzOTIsNDM2NDQwNjYyXX0=
-->