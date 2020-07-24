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

### nameof

You can **convert the type of a variable to a string** using the `nameof` operator.
```csharp
var x = 5;
nameof(x); // => Int
```

## List

The `List` is a data structure that offers a resizable list of elements. To **start using the `List` data structure** you must import `using  System.Collections.Generic`. The `List` object is defined with a generic `T` type as `List<T>` which you must supply when constructing a new list object. To **create a new list** use the `new` keyword as you would with any new object instance with the type of the container in `< >` brackets. You **initialize the contents of a list inline** by containing the content in `{ }` curly brackets after the definition.
```csharp
using  System.Collections.Generic;

var names = new List<string> { "John", "James", "Jacob" };
```

You can **add to a `List`** using the List's `Add` method.
```csharp
names.Add("Jason");
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

You can **initialise default instance class member values** from within the body of the class.
```csharp
class MyClass
{
  public int distance = 40;
}

var myClass = new MyClass();
myClass.distance; // => 40
```

### This

Unlike many other languages **the `this` keyword is optional and contextual**. If you refer to a class field within the body of a class that is non-static it is assumed by the compiler to refer to the instance of the class. The `checkDistance` method below use the instance's `distance` property without prefacing it with `this`, *however*, it would also have been valid to use `this` before it to be specific as to its context.
```csharp
class MyClass
{
  public int distance = 40;

  public bool checkDistance()
  {
    return distance > 40;
  }
}
```

You **must use `this` if the context of variable names is unclear** such as when assigning variables of the same name, for example, a constructor where the input arguments match the name of the class members.

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

You can **define implement code for `get` and `set` procedures directly** by expanding and implementing the methods after member definition. This allows you to write more complex implementations for `get` and `set`, however, if you write an implementation for one you must also have an implementation for the other, you cannot have `get` implemented and `set` still using the `set;` syntax. Below is the most basic default implementation, but you can functionally write any code you like here to get and set a member here. The `value` keyword is a special keyword indicating the value that is being passed into the member when it is assigned. By implementing custom `get` and `set` methods **any code inside or outside your class will use these methods for accessing the data**.
```csharp
public int balance
{
  get
  {
    return balance;
  }

  set
  {
    balance = value;
  }
}
```

## Exceptions

You can **throw a new exception** by using the `throw` keyword and creating a `new` instance of an exception with the exception's message as its argument. The most basic type of exception is `System.Exception`.
```csharp
throw new System.Exception("This triggered some exception stuff for some reasonj");
```

## Try and Catch

Code that might throw an exception **should be placed inside a `try` block** and **followed by a `catch` block** with the exception type to be handle as the argument. You can **assign the exception object as an argument to a value** and use it in your `catch` block. 
```csharp
try
{
  functionThatProducesIOException();
}
catch(IOException e)
{
  // handle exception here
}
```

You can **use the `where` clause with `catch` to catch specific exception types** and filter exceptions.
```csharp
try
{
  functionThatProducesIOException();
}
catch(IOException e) where (e.Data == "Some data"
{
  // handle this exception here
}
catch(IOException e) where (e.Data == "Different data"
{
  // handle the other exception here
}
```

## Functions

You can **define an anonymous function** using the `Func` object. When declaring a `Func` you should follow it by `< >` angle brackets with the input argument type and return type. You can use standard lambda calculus syntax to define anonymous functions.
```csharp
Func<int, int> double = x => x * 2
```

## Date and Time

You can **get the current date and time** using the `DateTime` class with the `Now` method.
```csharp
DateTime.Now;
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ4NDA3NDQ1OCw4ODcxMDA0OTAsODg0OD
Y1NDY5LC04MzQwMzI2MjksMTU0NjMxMTkxNywtMTYwNTYyNjcx
Myw1ODE3MjU0MjksLTM4MzA5MjExNCwtMTQwMTMxMTI5MCwxMD
ExMDE4NjA1LC00NDUzNjk5NzUsMTI4NTc4NDU3Niw4MjEyNzg2
NDUsLTE4NTUyOTMzOTIsNDM2NDQwNjYyXX0=
-->