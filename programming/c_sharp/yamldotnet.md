---
title: YamlDotNet
layout: page
exclude: true
---

You can **deserialize yaml files to dotnet objects** using the `YamlDotNet` NuGet package.

`YamlDotNet` does not easily support unstructured serialisation so if you want to access some arbitrary object inside a global object you will need to create a data model to do this.

```csharp
using YamlDotNet.Serialization;

class Person
{
    public string name { get; set; }
    public int age { get; set; }
}

// in main...

var yaml = @"
name: John
age: 20
";

var deserializer = new DeserializerBuilder().Build();

var person = deserializer.Deserialize<Person>(yaml);

person.name; // => John
person.age; // => 20
```

You can **ignore propreties that are present in the input data but NOT present in the models being deserialized to** by using the `IgnoreUnmatchedProperties` function on the `DeserializerBuilder` object. By default the deserializer will throw an error if it encounters a property it is not expecting.
```csharp
var deserializer = new DeserializerBuilder()
  .IgnoreUnmatchedProperties()
  .Build();
```

You can **deserialize from other naming conventions to dotnet style naming conventions** by using the `WithNamingConvention` method in combination with a `YamlDotNet.Serialization.NamingConventions` objects. Usually dotnet classes have capitalized properties, so, if your input data is formatted with lowercase properties and snake case the data will not be correctly deserialized and the properties not found.
```csharp
using YamlDotNet.Serialization;
using YamlDotNet.Serialization.NamingConventions;

// more closely matches dotnet naming conventions
class Person
{
    public string Name { get; set; }
    public int CurrentAge { get; set; }
}

// in main...

var yaml = @"
name: John
current_age: 20
";

var deserializer = new DeserializerBuilder()
  .WithNamingConvention(new UnderscoredNamingConvention())
  .Build();

var person = deserializer.Deserialize<Person>(yaml);

person.name; // => John
person.age; // => 20
```

