---
title: Xeger
layout: page
exclude: true
---

You can **generate a string that matches a regex** by using the `Xeger` class in the `Fare` NuGet package.
```csharp
using Fare;

var regex = "[a-z]_[A-Z]";
var generatedString = new Xeger(regex, new Random()).Generate(); // => "b_Q"
```