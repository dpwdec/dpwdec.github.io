---
title: Testing
layout: page
exclude: true
---

You can **link a test project to the project it is testing** thus allowing it to load in data and classes from that project. By adding a `ProjectReference` field into the `.csproj` file for the test project. Simply add a new `ItemGroup` to the test project's `.csproj` file with a relative path pointing to the project you want to test using the `Include` project `\` back slashes. *You still need to reference the classes and data in the project being tested with a `using` directive in your test file.*
```xml
<ItemGroup>
  <ProjectReference Include="path\to\project\being\tested.csproj" />
</ItemGroup>
```