

Data Annotations can be used to **decorate your model class definitions** to specify what format the tables and columns for the tables are in. You can use Data Annotations by `using` the `ComponentModel.DataAnnotations` module.
```csharp
using  System.ComponentModel.DataAnnotations;
```

You can **specify a primary key field** for your model, using the `[Key]` attribute. However, it does seem that many frameworks (including EF) will do this automatically for properties named `Id`.
```csharp
[Key]
public int Id { get; set; }
```

You can **specify that a field is NOT nullable**, *i.e. its required to be filled with something when inserting new entries into the database*, by using the `[Required]` attribute.
```csharp
[Required]
public string Address { get; set; }
```

You can **specify the length of a character string field** using the `[MaxLength]` attribute with the maximum number of characters for the string passed in an argument.
```csharp
[MaxLength(250)]
public string Message { get; set; }
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNjQ5MzQxNjhdfQ==
-->