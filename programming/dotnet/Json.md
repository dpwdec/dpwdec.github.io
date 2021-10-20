---
title: JSON
layout: page
exclude: true
---

To deserialize from JSON you **must enable get and set** on class properties otherwise deserialization will not be attempted for that class property.

You can **convert a string to an object** by using the `Deserialize` method on `JsonSerializer` typed with the object that you want to convert the JSON into.
```csharp
string objectJson = "{ \"Id\": \"0\", \"Name\": \"Xan\", \"Age\": \"400\" }";
var user = JsonSerializer.Deserialize<User>(objectJson);
/*
User class structure:
{
  public int Id { get; set; }
  public string Name { get; set; }
  public int Age { get; set; }
}
*/
```

You can **set different serialization options** such as remove case sensitivity, by using the `JsonSerializerOptions` object as argument to the `Deserialize` method. *Note the lowercase `name` property in this example.*
```csharp
string objectJson = "{ \"Id\": \"0\", \"name\": \"Xan\", \"Age\": \"400\" }";
var user = JsonSerializer.Deserialize<User>(objectJson, new JsonSerializerOptions
{
  PropertyNameCaseInsensitive = true
});
```

You can **define custom deserializations in JSON** using the `JsonPropertyName` attribute. This is useful if you have one or two attributes in your incoming JSON that do not match the dotnet naming schema allowing you to define a custom source for them. The example below deserializes from a snake case version of `some_property` into the standard dotnet pascal case `SomeProperty`.
```csharp
public class Data
{
  [JsonPropertyName("some_property")]
  public string SomeProperty { get; set; }
}
```

You can **deserialize enum properties from JSON** by using the adding a `JsonStringEnumConverter` object to the list of `Converters` as part of your `JsonSerializerOptions` object. *It seems that this inherits the case inseitivity of the serializer options*.
```csharp
// load raw json above

var serializerOptions = new JsonSerializerOptions();
serializerOptions.PropertyNameCaseInsensitive = true;
serializerOptions.Add(new JsonStringEnumConverter());

var deserializedObject = JsonSerializer<MyClass>(rawJson, serializerOptions);
```

## Newtonsoft

Don't use it.

You can **convert a string to an object** by using the `DeserializeObject` method on `JsonConvert` typed with the object that you want to convert the JSON into.
```csharp
string objectJson = "{ \"Id\": \"0\", \"Name\": \"Xan\", \"Age\": \"400\" }";
var user = JsonConvert.DeserializeObject<User>(objectJson);
/*
User class structure:
{
  public int Id { get; set; }
  public string Name { get; set; }
  public int Age { get; set; }
}
*/
```