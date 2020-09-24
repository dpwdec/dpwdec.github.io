---
title: Collections
layout: page
exclude: true
---

## Arrays

You can **initialize and create a new array in a single line** by defining the array type followed by `{}` curly brackets containing the contents of the new array.
```csharp
int[] arr = {1, 2, 3, 4, 5};
```

You can **initialize a new array after creation** using the `new` keyword combined with the type followed by the standard array creation shorthand syntax.
```csharp
int[] arr; // define a variable to hold an array
arr = new int[] {1, 2, 3, 4, 5}; // fill the int array
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

## Linq

You can **return the first matching element from a collection** using the `FirstOrDefault` method. In the example below, only the first `2` is returned. **If no matching elements is found** the method returns `null`, this behaviour cannot be modified.
```csharp
int[] arr = {1, 2, 3, 2, 5};
arr.FirstOrDefault(x => x == 2);
```

You can **match a collection for a specific element OR return a predefined default value** by using the `DefaultIfEmpty` method with the default return value as its argument concatenated with the `First` method.
```csharp

```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQzOTYyNDM0NSwxNjgwMjQ0MzgxLC00OT
gzOTI1OTRdfQ==
-->