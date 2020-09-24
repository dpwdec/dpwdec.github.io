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

You can **define a connection string for your database** by adding it to your project's `appsettings.json` file. Using the key `"ConnectionStrings"` to encompass all the key-value pairs. This name is a convention (not absolutely required) but using it allows you to use the `IConfiguration` utility `GetConnectionString` which looks at the `"ConnectionStrings"` entry. The **database string keys themselves do not have a specific naming convention**, in this example the name is `"DatabaseConnection"` but it could be any descriptive name. *Note*: the database name in the connection string is *case sensitive*.
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

## Queries

You can **query data in a table** by accessing the associated `DbSet` on the database context object. This object essentially works like a collection which can use lambdas to process data. You will need to add the `System.Linq` library to access higher order functions that can process the data from the table collections.

You can **return all data in a table** by using the `ToList` method.
```csharp
DbContext.MyTable.ToList();
```

You can **return a single specific entry in a table** by using the `FirstOrDefault` method with a lambda that matches some condition about the data.
```csharp
// return MyTable entry with Id of 1
DbContext.MyTable.FirstOrDefault(x => x.Id == 1);
```

## Design

What is `dotnet add package Microsoft.EntityFrameworkCore.Design`?

## Repo Pattern

By **wrapping the `DbContext` in an interface** that defines semantic methods like `GetAllResource` or `GetResourceById` it separates the implementation of this database access the application's other modules, allowing them to call these methods declaratively. This allows for the system to swap out the database type and access methods without changing the business logic classes. This is an example of **persistence ignorance**, however, it does seem like its not required for smaller projects.

**Persistence ignorance** separates business logic from infrastructure concerns, this is stated as:
> "...ordinary classes where you focus on the business problem at hand without adding stuff for infrastructure-related reasons..."

## Data Annotations

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

## Migrations

You can **create a new database migration** using the `migrations add` with the `dotnet ef` too. This will add the migration to the `Migrations` folder in your project.
```bash
$ dotnet ef migrations add <MIGRATION_NAME>
```

You can **remove the last migration you created**, *before actually migrating data*, by using the `migrations remove` command.
```bash
$ dotnet ef migrations remove
```

Migrations are **time stamped to allow for effective rolling back**.

You can **run a migration**, *pushing the schema changes to the actual database*, by using the `database update` command. This will also create or add to a `__EFMigrationHistory` table that keeps a log of the migrations on the database for version controlling database changes.
```bash
$ dotnet ef database update
```

### Migration Files

Although the section below details what migrations files mean and how to configure them, its **not recommended to configure migrations directly** to get the database structure you want. Instead you should **use `DataAnnotations` to decorate your model class definitions**. It is useful to understand what migration files specify (which is the primary intention of this documentation), so that you can make changes to your database models and check the structure of the database before changing the real database.

Individual migrations files contain a class named after the migration name which inherits from the `Migration` class in `EntityFrameworkCore.Migrations`. This class implements two methods, either `Up` or `Down`, which add and delete schema from the database respectively.

A **new table migration is created** with the `MigrationBuilder` class's `CreateTable` method. The `name` for this table is automatically generated based on the `DbSet`s defined in the `DbContext` class.
```csharp
public partial class MyMigration : Migration
{
  protected override void Up(MigrationBuilder migrationBuilder)
  {
    migrationBuilder.CreateTable(
      name: "MyTable", // name taken from DbSet
      columns: table => new
      {
        Id = table.Column<int>(nullable: false)
      }
    );
  }
}
```

You can **specify the type of a database column within a migration** by using the `Column` method typed with the property type it holds.
```csharp
table.Column<int>();
```

You can **specify whether a database column within a migration is nullable** by using the `Column` method with the `nullable`argument.
```csharp
table.Column<int>(nullable: false);
```

The `Annotations` method can be used to **specify how a primary key increments**.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ5ODE1OTcwMywtODk5NzIwODU5LC0xMz
QxNzkzNzEsNzA1NzM2MjQyLDE2Nzg4MTQzMDcsLTIyMDE1NDY1
OSwxNTcwNzc0OTIsLTEyNDc2MzEwNjgsMTkwMjIzNTIwNCwtNz
M0MjAzOTYzLC05NzczOTg0MjMsLTU2MjI3MTU2NSwtNjcwNjc4
NTA1LC00OTE0OTkzNzYsMTYxMDU4MDE4Ml19
-->