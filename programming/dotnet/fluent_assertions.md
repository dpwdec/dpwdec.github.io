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