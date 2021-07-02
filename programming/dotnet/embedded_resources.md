---
title: Embedded Resources
layout: page
exclude: true
---

You can **compile a resource into a dotnet program binary or set of DLLs** by using the `EmbeddedResource` tag with the `Include` property pointing to that path of your resource in your project's `.csproj` file and then using the `Assembly` library to access it. When the project is built it dotnet will embed the file into the binary.
```xml
<Project sdk="Microsoft.NET.Sdk">

  ... 

  <ItemGroup>
    <EmbeddedResource Include="path/to/resource.txt"></EmbeddedResource>
  </ItemGroup>
</Project>
````

The above path would work for a file structure in the following format.
```
MyProject
├── path
|   └── to
|       └── resource.txt
└── MyProject.csproj
```

To **access the embedded resource in code** using the `Assembly` object which is part of the `System.Reflection` namespace to get a resource stream to the file and then use a `StreamReader` to parse the resource. When **specifying the path to the embedded resource** all `/` forward slashes are replaced with `.` periods and the file must be namespaced from the top level name of the project.
```csharp
using System.IO;
using System.Reflection;

static void Main(string[] args)
{
    // get reference to the assembly
    var assembly = Assembly.GetEntryAssembly();
   
    // get resource stream to a specific embedded resource
    // note the path has to start with the name of the project
    var resourceStream = assembly.GetManifestResourceStream(".MyProject.path.to.resource.txt");

    // initialise a stream reader to read the resource stream
    using (var reader = new StreamReader(resourceStream))
    {
        // parse the entire resource
        var resourceContent = reader.ReadToEnd();
    }
}
```

You can **get the name of the project** from the `GetEntryAssembly` method with some string manipulation.
```csharp
using System.Reflection;
using System.Linq;

public string GetProjectName()
{
    return Assembly.GetEntryAssembly().ToString().Split(',').First();
}
```