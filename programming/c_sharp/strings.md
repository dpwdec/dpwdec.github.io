---
title: Strings
layout: page
exclude: true
---

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
// => "My name is Berrylin and I am 51 years old."
```

You can **trim a match characters from the end of a string** using the `TrimEnd` method which takes an array or splat list of `chars` and matches any possible combination of those characters to the end of the string until it reaches a character not included. If **nothing matches** it will **return the original string unchanged**.
```csharp
"XgbXg".TrimEnd('g'); // => "XgbX"
"XgbXgggg".TrimEnd('g'); // => "XgbX"
"XgbXgb".TrimEnd('b', 'g'); // => "XgbX"
"XgbXgbgbbggbgbgg".TrimEnd('b', 'g'); // => "XgbX"
"XgbXg".TrimEnd('b'); // => "XgbXg" (Unchanged)
```

You can **match a pattern to the end of a string** using the `EndsWith` method.
```csharp
"some/path/about/".EndsWith("about/"); // => true
"some/path/about/".EndsWith("wabout/"); // => false
```

## Multiline string literals

You can **create a multiline string** by using a `@` symbol before a string literal. This allows you to create multiline strings that mirror text files.
```csharp
var x = @"
This is a lovely
Multiline string literal
And a string haiku
";
```

You can add `"` double quote characters in a multi-line by using a `""` *double* double quote.
```csharp
var x = @"
{
    ""data"": ""test""
}
";
```