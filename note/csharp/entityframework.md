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



## Design

What is `dotnet add package Microsoft.EntityFrameworkCore.Design`?
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ1MzQ4MTM1LC00OTE0OTkzNzYsMTYxMD
U4MDE4Ml19
-->