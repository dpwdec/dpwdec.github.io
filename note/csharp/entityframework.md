---
title: Entity Framework
layout: page
exclude: true
---

Entity Framework is an **orm for .NET objects**.

You can **add a tool for Entity Framework to .NET CLI** by installing `dotnet-ef` using `dotnet tool`. This tool allows you to do things like generate code and run migrations on your entity framework databases. You may also need to have `Microsoft.EntityFrameworkCore.Design` installed as well.
```bash
$ dotnet tool install --global dotnet-ef
```

## Connection

You can **define the connection string for your database** by adding it to your project's `appsettings.json` file. Using the key `"ConnectionStrings"` to encompass all the key-value pairs for your database connections is not absolutely required, *however* Entity Framework comes with default configuration for this key so its convention to use it. The **database string keys within this do not have a specific naming convention**, in this example the name is `"DatabaseConnection"` but it could be any descriptive name.
```json
{
  "ConnectionStrings": {
    "DatabaseConnection": "<database specific connection string here>"
  }
}
```

## Context

A context class is a project wide file/class that describes the tables in the database.

You can **define a database table** using a `DbSet` object from `Microsoft.EntityFrameworkCore` as a property within your project's context file, with the type of argument the `DbSet` as the database model. The **name of this property should be pluralised** as the name of the model type it represents. The example below defines a `DbSet` object called `Users` for the `User` class.
```csharp
public DbSet<User> Users { get; set; }
```

## Design

What is `dotnet add package Microsoft.EntityFrameworkCore.Design`?
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTczNDIwMzk2MywtOTc3Mzk4NDIzLC01Nj
IyNzE1NjUsLTY3MDY3ODUwNSwtNDkxNDk5Mzc2LDE2MTA1ODAx
ODJdfQ==
-->