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

## Context

A context class extends the `DbContext` class from `EntityFrameworkCore` and is a project wide file that is used to configure connections to the database and define tables within the database.

You can **define a new database context class** by inheriting from `DbContext` and calling the `base` constructor which takes a single `options` argument of type `DbContextOptions` which is typed with itself.
```csharp
using Microsoft.EntityFrameworkCore;

public class MyDbContext : DbContext
{
  public MyDbContext(DbContextOptions<MyDbContext> options) : base(options) { ... }
}
```

You can **define a database table** using a `DbSet` object from `Microsoft.EntityFrameworkCore` as a property within your project's context file, with the type of argument the `DbSet` as the database model. The **name of this property should be pluralised** as the name of the model type it represents. The example below defines a `DbSet` object called `Users` for the `User` class.
```csharp
public DbSet<User> Users { get; set; }
```

## Connection

You can **define a connection string for your database** by adding it to your project's `appsettings.json` file. Using the key `"ConnectionStrings"` to encompass all the key-value pairs. This name is a convention (not absolutely required) but using it allows you to use the `IConfiguration` utility `GetConnectionString` which looks at the `"ConnectionStrings"` entry. The **database string keys themselves do not have a specific naming convention**, in this example the name is `"DatabaseConnection"` but it could be any descriptive name.
```json
{
  "ConnectionStrings": {
    "DatabaseConnection": "<database specific connection string here>"
  }
}
```

You can **set up a connection to your database for a project** by using the `ConfigureSerivces` method in the `Startup` class. To do this, use the `services` object to `AddDbContext` with a type of your project specific class that extends `DbContext` from Entity Framework. This method then takes a lambda that passes in an `DbContextOptions` as its argument and which database type specific configuration is run on. As detailed above, the `Configuration` object has methods to access the `appsettings.json` file to retrieve the associated database string.
```csharp
services.AddDbContext(options => options.UseSqlServer(Configuration.GetConnectionString("DatabaseName"));
```

You can **connect to a PostgreSQL database** by installing the `Npgsql.EntityFrameworkCore.PostgreSQL` nuget package, and using the `UseNpgsql` method on `options`.
```csharp
services.AddDbContext(options => options.UseNpgsql(Configuration.GetConnectionString("DatabaseName"));
```

## Design

What is `dotnet add package Microsoft.EntityFrameworkCore.Design`?
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNDc2MzEwNjgsMTkwMjIzNTIwNCwtNz
M0MjAzOTYzLC05NzczOTg0MjMsLTU2MjI3MTU2NSwtNjcwNjc4
NTA1LC00OTE0OTkzNzYsMTYxMDU4MDE4Ml19
-->