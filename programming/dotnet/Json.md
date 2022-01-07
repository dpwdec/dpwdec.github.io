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

You can **deserialize enum properties from JSON** by adding a `JsonStringEnumConverter` object to the list of `Converters` as part of your `JsonSerializerOptions` object. *It seems that this inherits the case inseitivity of the serializer options*.
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

## Custom Deserialization

You can **write custom deserialization code** by extending the `JsonConverter<T>` class. This class implements a `Read` and `Write` method for deserializing and serializing data. The `T` will be the object to which you deserialize. Custom deserializers **slot directly into the existing serialization framework that dotnet offers**. This means that if you have a set of nested objects that you want to deserialize using the ordinary built in serializers that *contain* an object that requires custom deserialization, your custom deserializer will only run for the specific nested object that needs deserialization.

The example below demonstrates with an `Operator` class that contains a list of `Order` objects that require custom deserialization. When running the custom deserializer will only trigger once it reaches one of the order objects in the `Orders` list.
```csharp
public class Operator
{
  string Name { get; set; }
  int id { get; set; }
  List<Order> Orders { get; set; }
}

public class CustomOrderDeserializer : JsonConverter<Order>
{
  // custom deserialization code
}
```

The associated JSON would be as follows...
```json
{
  "name": "Sonitaf",
  "id": 4321766555,
  "orders": 
  [
    {
      "id": "76$$09_k"
    },
    {
      "id": "6^jJ0-f"
    }
  ]
}
```

You can **use your custom deserializer when deserializing** by adding it to the list of `Converters` on your `JsonSerializerOptions` that are an argument for the actual `Deserialize` function.
```csharp
var serializerOptions = new JsonSerializerOptions();
// Add an instance of your deserializer code here
serializerOptions.Converters.Add(new MyCustomDeserializer());

var jawJson = File.ReadAllText("./data.json");

var result = JsonSerializer.Deserialize<MyClass>(rawJson, serializerOptions);
```

This is important to remember when traversing the JSON reader for your object. Your custom reader will **traverse from the beginning of the object** and **must only return the created object once it has reached its end**. Functionally this means you must reach a `JsonTokenType.EndObject` enum variant when returning. If you do this incorrectly you will get a `read too much or not enough` exception when deserializing. More detail [here](https://stackoverflow.com/questions/62147178/system-text-json-deserialization-fails-with-jsonexception-read-to-much-or-not-e).
```csharp
if (reader.TokenType == JsonTokenType.EndObject)
{
  // return the deserialized object
}
```

You can **read the tokenized JSON of an object** using the `Utf8JsonReader` object that is passed into the `Read` method of the `JsonConverter<T>` class. The signature of this method is shown below where `T` is the object that will be returned from the deserialization.
```csharp
public override T Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options);
```

You can **read through the tokens in the reader** using a `while` loop with the `Read` method on the reader. On each loop iteration the *next* JSON token will be accessible on the reader.
```csharp
public override T Read(
  ref Utf8JsonReader reader, 
  Type typeToConvert, 
  JsonSerializerOptions options)
{
  while(reader.Read())
  {
    // moves to the next token in the reader
  }
}
```

You can **check the type of the current json token** using the `TokenType` property.
```csharp
public override T Read(
  ref Utf8JsonReader reader, 
  Type typeToConvert, 
  JsonSerializerOptions options)
{
  while(reader.Read())
  {
    if (reader.TokenType == JsonTokenType.PropertyName)
    {
      // do something if we reached a property
    }
  }
}
```

You can **get the value of a token** *if* it contains a value using the `GetString` method. For example, if we want to get the value of a property or the name of a field.
```csharp
public override T Read(
  ref Utf8JsonReader reader, 
  Type typeToConvert, 
  JsonSerializerOptions options)
{
  while(reader.Read())
  {
    if (reader.TokenType == JsonTokenType.PropertyName)
    {
      if (reader.GetString() == "id")
      {
        // do something if that property was called id
      }
    }
  }
}
```

You can **manually read to the next token within a `while` loop for reading**. This does not cause any problems and will just cause the next loop to start at the nesting that you reached in your traversal *within* the loop. The example below will read *2* tokens per loop.
```csharp
public override T Read(
  ref Utf8JsonReader reader, 
  Type typeToConvert, 
  JsonSerializerOptions options)
{
  while(reader.Read())
  {
    reader.read()
  }
}
```

A more useful application of this can be seen below where the reader reaches a property called `id` and then reads to the next token to get the *value* of that property. When the `while` loop resumes it will move to the next token after the value that was read.
```csharp
public override T Read(
  ref Utf8JsonReader reader, 
  Type typeToConvert, 
  JsonSerializerOptions options)
{
  while(reader.Read())
  {
    if (reader.TokenType == JsonTokenType.PropertyName)
    {
      if (reader.GetString() == "id")
      {
        reader.Read();
        var val = reader.GetString();

        // do something with the property value
      }
    }
  }
}
```

At first it appears like you can only traverse the `Utf8JsonReader` once through. However, you can **traverse the reader multiple times** and even **duplicate the reader content** by passing the reader into a function *without* the `ref` keyword. Not using the `ref` keyword will not mutate the "base" reader that the `Read` method uses. If you pass the `reader` into a function *with* the `ref` keyword that function will continue to mutate the state of the reader that the deserializer passes out for the next stage of deserialization.
```csharp
public override T Read(
  ref Utf8JsonReader reader, 
  Type typeToConvert, 
  JsonSerializerOptions options)
{
  ReadDataThrough(reader);
  // reader is still positioned at start
  Assert.Equals(reader.TokenType, JsonTokenType.StartObject);

  ReadDataThroughMut(ref reader);

  // reader is now positioned where the mut function finished
  Assert.Equals(reader.TokenType, JsonTokenType.StartArray);

  // ---SNIP--- other deserialization stuff
}

// read through the entirety of the json WITHOUT mutating the base reader
public void ReadDataThrough(Utf8JsonReader reader)
{
  while (reader.Read())
  {
    if (reader.TokenType == JsonTokenType.EndObject) { break; }
  }
}

// read through to a start array property that mutates the base reader
public void ReadDataThroughMut(ref Utf8JsonReader reader)
{
  while (reader.Read())
  {
    if (reader.TokenType == JsonTokenType.StartArray) { break; }
  }
}
```

### Polymorphic Deserialization

There's some general info on polymorphic deserialization in dotnet [here](https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-converters-how-to?pivots=dotnet-6-0#support-polymorphic-deserialization).

The example below shows **how to accomplish polymorphic deserialization in dotnet**. The `Person` class contains a `Job` field of type `Role` that can be a concrete polymoprhic instance of the abstract `Role` class, either `Doctor` or `Dentist`. In this case the custom deserializer needs to traverse the JSON of the object until it finds a *discrimator* - i.e. some clue in the object structure about what type of subclass this object is - in this case we use the name of the property on the object; if its a `Doctor` object it will have the property `HospitalId` otherwise its a dentist. The reader then creates an instance of the correct subclass and returns that instance when it reaches the end of the reader.

The example below also demonstrates that if you have to **process JSON with multiple properties that are unordered and occur *before* your discriminator** you may have to store these values while you traverse the JSON tree until you find your discriminator *then* recreate the *correct* object type and copy accross all the stored values. Here this is encapsulated with the `Salary` property which is stored intermediately on the `role` value until the discriminator is found, *then* if the value is there it is copied accross to the new discriminated object. It needs to be done this way as depending on the ordering of the properties in the JSON file the `Salary` value could be found before *or* after the discriminator.
```csharp
public class Person
{
  string Name { get; set; }
  Role Job { get; set; }
}

public abstract class Role
{
  public int Salary { get; set; }

  public abstract string JobAction();
}

public class Doctor : Role
{
  public int HospitalId { get; set; }

  public override string JobAction()
  {
    return "Fixing this dude's spleen."
  }
}

public class Dentist : Role
{
  public string EnamelSpeciality { get; set; }

  public override string JobAction()
  {
    return "Fixing this lady's molar."
  }
}

public class RoleDeserializer : JsonConverter<Role>
{
  public override Role Read(
    ref Utf8JsonReader reader, 
    Type typeToConvert, 
    JsonSerializerOptions options)
  {
    // default to an empty doctor role to hold intermediate values before discrimination
    Role role = new Doctor();

    while(reader.Read())
    {
      if (reader.TokenType == JsonTokenType.PropertyName)
      {
        if (reader.GetString() == "HospitalId")
        {
          reader.Read();
          var id = Int32.Parse(reader.GetString());
          role = new Doctor()
          {
            HospitalId = id
            Salary = role.Salary != null? role.Salary : null
          }
        }
        else
        {
          reader.Read();
          var speciality = reader.GetString();
          role = new Dentist()
          {
            EnamelSpeciality = speciality
            Salary = role.Salary != null? role.Salary : null
          }
        }

        // update the salary on the object - shared by both role instances
        if (reader.GetString() == "Salary")
        {
          reader.Read();
          role.Salary = Int32.Parse(reader.GetString());
        }
      }

      // return object once end is reached
      if (reader.TokenType = JsonTokenType.EndObject)
      {
        return role;
      }
    }

    // return the empty object if we reach the end with out anything
    // could raise an exception here if required
    return role;
  }

  // there will also be an unimplmeneted version of the Write function below
}
```