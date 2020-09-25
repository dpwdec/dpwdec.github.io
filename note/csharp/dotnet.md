---
title: .NET
layout: page
exclude: true
---

You can **create a new console application** by using `dotnet new` command with the `console` type argument. This command creates a new console output project in the folder where the command in called.
```bash
$ dotnet new console
```

You can **name a new application** using the `n` flag followed by the desired name of the application.
```bash
$ dotnet new console -n MyProject
```

You can **update an existing .NET CLI tool** using the `tool update` command.
```bash
$ dotnet tool update --global <tool name>
```

You can **build your project** (without running it), using the `build` command.
```bash
$ dotnet build
```

You can **run tests from a test project** by using the `test` command.
```bash
$ dotnet test
```

You can **structure the `namespace`s of your projects** around folder hierarchy, with the project name being the highest level `namespace` followed by subfolder names separated by a `.` period. For example in the following folder structure, the `namespace` for `bar.cs`, lying in the `Project` folder would simply be `Project`.
```
Project
├── Models
|   └── foo.cs
└── bar.cs
```

However the `namespace` at the top of the `foo.cs` file would be `Project.Models` to indicate the project structure.
```csharp
// bar.cs
namespace Project
{
  // bar.cs code
}

// foo.cs
namespace Project.Models
{
  // foo.cs code
}
```

You **cannot name your class the same as a folder namespace** as this will confuse the C# compiler in trying to resolve the difference between a `class` and `namespace` when you try to use them.
```yaml
# WRONG
Project
└── User
    └── User.cs

```

## Var

You can **use the `var` keyword** when the type of a variable is inferred or when you are working with an anonymous type. It's recommended to generally avoid using `var` unless you need to or unless type inference is *very* clear to readers.
```csharp
var age = 5;
```

## Strings

You can **convert a number to a string** using the `ToString` method.
```csharp
int numberInt = 5;
string numberString = numberInt.ToString();
```

You can **interpolate values into strings** by prepending the strings with a `$` dollar sign and including the interpolated values inside `{}` curly brackets.
```csharp
var name = "Berrylin";
var age = 51;
var message = $"My name is {name} and I am {age} years old."
// => "My name is Berrlin and I am 51 years old."
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

You can **create a new instance with class parameters assigned during instance construction** by creating an expression block after the `new Object` definition with `{}` curly brackets and then listing out parameters you want to assign by name and assigning them to a value. If you use this construction method you **do not have to define an explicit constructor on your class** that takes arguments.
```csharp
new User{Id = 0, Age = 22, Name = "Belinda Bigglesworth", Zip = "X3 X9Y13"};
```

You can **combine positional arguments and block assigned parameters** by including the argument parameters inside `()` soft brackets after calling `new Object` followed by assignments that you want to take inside `{}` curly brackets. This type of instance creation **does require a constructor**. In the example below, the `User` `Id` and `Age` are passed in as positional arguments followed by `Name` and `Zip` properties assigned using expression syntax.
```csharp
new User(0, 22){Name = "Belinda Bigglesworth", Zip = "X3 X9Y13"};
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

### Base

You can **use the `base` keyword to access methods of a base class from a derived class even when the derived class has override the method** by accessing properties on `base` as if it were an object. The example below defines a `Derived` class that uses its `Base` classes `GetInt` method in its constructor *and* its own version of `GetInt`. The `base` keyword allows you to discriminate between versions of methods overridden in the base class and implementations from the base class.
```csharp
public class Base
{
  public virtual int GetInt() => 5;
}

public class Derived : Base
{
  public int BaseInt { get; set; }
  public int DerivedInt { get; set; }
  
  public Derived()
  {
    BaseInt = base.GetInt();
    DerivedInt = GetInt();
  }

  public override int GetInt() => 60;
}
```

You can **invoke a base class's constructor on your derived class's constructor** by adding the `base` keyword at the end of the constructor separated by a `:` colon and with any constructor specific arguments passed into it. This also **works for overloaded constructors**, as in the example below where the derived class uses `base` to create a version of *both* the constructor method with an argument *and* without.
```csharp
public class Base
{
  public int Value { get; set; }
  public Base(int Value)
  {
    this.Value = Value;
  }

  public Base()
  {
    Value = 10;
  }
}

public class Derived : Base
{
  public Derived(int Value) : base(Value) // invoke the first base constructor with arguments here
  {
    // custom Derived construction here
  } 

  public Derive() : base() // invoke the second base constructor WITHOUT arguments here
  {
    // custom Derived construction here
  }
}
```

### Virtual

The **`virtual` keyword is used to mark methods in a class that can be `override`n** by classes that inherit from them. You **must provide a default implementation** for a `virtual` method as it is optional whether a base class will `override` the method or not. Regular class methods **cannot be overriden**.
```csharp
class Base
{
  public virtual string SayHello()
  {
    return "Hello";
  }
}

class Inheritor : Base
{
  public override string SayHello()
  {
    return "Greetings!"
  }
}
```

### Value

The **`value` keyword allows you to implicitly reference the argument passed into a property's `set` method**. In the example below, the code defines a `private` member called `_X` which reference via a public `X` interface proprety. The `value` keyword is then use to set `_X` as the implicit argument to the `set` method, this would be similar to writing `set(double value)` as the signature for the set method.
```csharp
private double _X;
public double X
{
  get { return _X; }
  set { _X = value; }
}
```

I'm unsure why this useful, or why the value can't assigned directly without a private class member.

### Abstract

The `abstract` keyword (or modifier) is used to define **incomplete or skeleton implementations** for classes and methods, as such, classes marked with the `abstract` keyword **cannot be instantiated** but are instead used as **base classes** to define the structure of classes that are actually implemented. You can **only create `abstract` methods inside an `abstract class**.

To **define an abstract class** use the `abstract` keyword in the class definition and then add abstract method signatures for the class. The example below defines a `Shape` class with a method signature for a method called `Area` that returns a double.
```csharp
abstract class Shape
{
  public abstract double Area();
}
```

You can **inherit from an abstract class** by using standard inheritance syntax. A class that inherits from an abstract class **must provide an implementation for all the base class's abstract methods**. 

To **provide an implementation for an abstract method** use the `override` keyword.
```csharp
public class Square : Shape
{
  public double X { get; set; }

  // concrete override implementation provided for Square
  public override double Area()
  {
    return X * X;
  }
}
```

You can also **provide concrete implementations in an abstract class** to provide functionality to all inheritors of a base class.
```csharp
public abstract class Component
{
  public abstract double ReportCode();
  public string Version()
  {
    return "1.3.3x";
  }
}
```

## Interfaces

An `interface` defines methods that an object that *implements* that interface must fulfill. Any **methods defined in an interface must be implemented in the class that uses the interface**.

You can **define an interface** by using the `interface` keyword. It is the `C#` interface naming convention to add the capital letter `I` to interface names.
```csharp
interface IScreen { }
```

You can **define parameters within an interface** with the same `get` and `set` pattern that would also be in class structures.
```csharp
interface IScreen
{
  double PointData { get; set; }
}
```

You can **define methods to implemented by users of an interface** by adding the method signatures to the body of the interface. If a class used the interface `IScreen` below, it would have to implement `Display` so that it matched the returned types described in the interface. 
```csharp
interface IScreen
{
  double PointData { get; set; }
  int Display();
}
```

It is also generally the case that **interfaces which only implement one key method are renamed to named after that key method with -able appended to the end**, so in the example below the `IScreen` interface which defines the key method `Display` could be renamed to `IDisplayable`
```csharp
interface IDisplayable
{
  double PointData { get; set; }
  int Display();
}
```

To **use an interface** a class must **inherit from that interface** and then **implement all the methods *and* properties** of that interface. Interface inheritance is done using the **same syntax as class inheritance**.
```csharp
class PixelImage: IDisplayable
{
  public double PointData { get; set; }
  int Display()
  {
    // display code
  }
}
```

**A single class can inherit from *multiple* interfaces**. If a class **inherits from another class and some interfaces** the **base class should be listed first** in the inhteritance list followed by the interfaces.
```csharp
class MyClass: BaseClass, MyInterface, MyOtherInterface { ... }
```

All **properties and methods defined in an interface are public** and **do not support access modifiers** because all classes that inherit from them must use all methods and properties. There are also **no static methods in interfaces**.
```csharp
// NOT VALID
interface MyInterface
{
  private int MyMethod(); // access modifiers not supported
  static double MyStatic(); // static methods not supported
}
```

You **cannot set a default value for an interface property**.
```csharp
// NOT VALID
interface MyInterface
{
  double x = 5; // cannot be initialised
}
```

## References

What does `Add Reference` actually do?

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

You can **use the `where` clause with `catch` to catch specific variants of the same exception types** and filter exceptions intuitively. The order in which you filter exceptions matters, when `catch`ing an exception the code will look for the first handler that matches the exception it has and go with that ignoring all other handlers listed afterwards, therefore you should **write exception handling from most specific to least specific**.
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

## Importing

You can **import a reference to the classes / files into different project** (e.g. a test project) by `RMB` clicking on the project you want to import into and selecting `Add -> Reference`.

## VS Code

You can **get a shortcut code snippet for the creation of a class property** by typing `prop` into your editor within a class and pressing `TAB`.

You can **get a code snippet for class constructors** by typing `ctor` followed by `TAB`.

You can **generate a `private readonly` field** by creating an undefined variable starting with an `_` underscore, for example `_variable`, and then `RMB (on variable) -> Generate Private Readonly Variable`.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQwMzIyOTIzNywtMTY1MDg3NzkwMSwtMT
AzMzE0ODMwOSwxMTgwNTcwNDQ0LDM5MTczMjUyMiwtMTU2ODg4
OTMwMSwtOTA3NjA4Mzc0LDEyOTI4MTU1MDUsNjY4NzkyNDk2LD
M1ODk1NzIzMywxMDkyMjk2ODYzLDM0MTg2MzYzNSwyMDA4NDU3
MzU1LC0xMjM5Njg1MDU0LDE4OTc3Njg0ODEsLTEyNTU2MDA2OT
IsMTI1MzM1MTI0NCwxMzk0Njg2Nzk3LDEyNTUyODcxNTcsLTY3
NjU0MDMzMF19
-->