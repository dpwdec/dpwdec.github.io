---
title: JSON
layout: page
exclude: true
---

## Newtonsoft

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzMwMzE1MjczXX0=
-->