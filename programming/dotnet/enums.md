---
title: Enums
layout: page
exclude: true
---

You can **get an array of the all the possible values that enumerable can take** by using the `GetValues` method on the `Enum` namepsae with the `typeOf` the enum you want the values of as its argument.
```csharp
class Program
{
    enum MyEnum
    {
        Foo,
        Bar,
        Baz
    }

    static void Main(string[] args)
    {
        var allValues = Enum.GetValues(typeOf(MyEnum));
        Console.Writeline(allValues[1]) // => Bar
    }
}
```