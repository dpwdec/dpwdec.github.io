---
title: Project
layout: page
exclude: true
---

You can **create a new console application** by using `dotnet new` command with the `console` type argument. This command creates a new console output project in the folder where the command in called.
```bash
dotnet new console
```

You can **name a new application** using the `n` flag followed by the desired name of the application.
```bash
dotnet new console -n MyProject
```

You can **update an existing .NET CLI tool** using the `tool update` command.
```bash
dotnet tool update --global <tool name>
```

You can **build your project** (without running it), using the `build` command.
```bash
dotnet build
```