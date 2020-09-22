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

A context class is a project wide file/class that describes the tables in the database.

You can **define a database table** using a `DbSet` object from `Microsoft.EntityFrameworkCore` as a property within your project's context file, with the type of argument the `DbSet` as the database model.
```

## Design

What is `dotnet add package Microsoft.EntityFrameworkCore.Design`?
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NDcxNjU0MCwtNDkxNDk5Mzc2LDE2MT
A1ODAxODJdfQ==
-->