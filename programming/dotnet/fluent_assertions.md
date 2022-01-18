---
title: Fluent Assertions
layout: page
exclude: true
---

The **Fluent Assertions** library allows you to make unit test assertions more easily.

You can **make assertions on the equivalence of two pieces of data** by using the `BeEquivalentTo` function. This allows you to test lists or more complex data structures where the data should be the same but not necessarily in the same order or same format. The example below shows an assertion on two lists that are *equivalent* but not *equal* because the data is out of order.
```csharp
public void TestEquivalence()
{
    var result = new List<int>() { 3, 1, 2, 3, 4 };
    var expected = new List<int>() { 1, 2, 3, 4, 3 };
    result.Should().BeEquivalentTo(expected);
}
```

You can **test equivalence of sub class objects** by adding `RespectingRuntimeTypes` to the `BeEquivalentTo` options object. By default, if fluent assertions is checking the equivalence of a group of objects that are a subclass of another object it will only check the properties on the parent class not the sub classes, *unless*, this option is specified. In the example below the first assertion *without* the `options` will only check the `Foo` properties for equivalence, the `Name` property. However, the subclass' own properties, `Color` and `Age` are different and therefore not equivalent. The second assertion checks correctly by also asserting against the *actual* subclass type and checking the `Age` and `Color` properties.
```csharp
class Foo
{
    string Name { get; set; }
}

class Bar : Foo
{
    string Color { get; set; }
}

class Baz : Foo
{
    int Age { get; set; }
}

public void TestEquivalence()
{
    var result = new List<Foo>()
    {
        new Bar() { Name = "Miku", Color = "green" },
        new Baz() { Name = "Tetsu", Age = 122 }
    };

    var expected = var result = new List<Foo>()
    {
        new Bar() { Name = "Miku", Color = "red" },
        new Baz() { Name = "Tetsu", Age = 140 }
    };

    // This assertion passes incorrectly
    result.Should().BeEquivalentTo(expected);

    // This assertion fails as it should
    result.Should().BeEquivalentTo(expected, options => options.RespectingRunTimeTypes());
}
```