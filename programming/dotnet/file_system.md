---
title: File System
layout: page
exclude: true
---

You can **read the entirety of a file** using the `ReadAllText` function on the `File` object. It is only faster to use a `StreamReader` object over just the `ReadAllText` function when file lengths grow to the tens of thousands of lines size and the difference is still only tens of milliseconds at that.
```csharp
using System.IO;

var text = File.ReadAllText("/path/to/file");
```

You can **get the base directory from which your project is being run** by using the `System.AppContext.BaseDirectory` property in your code.

You can **get paths to all files in a directory** by using the `EnumerateFiles` function on the `Directory` object. This also allows to submit a second argument that matches a particular file pattern. The directory path is relative to where the project is run from.
```csharp
foreach (string file in Directory.EnumerateFiles("/path/to/directory"), "*.json")
{
    // do something with each file
}
```