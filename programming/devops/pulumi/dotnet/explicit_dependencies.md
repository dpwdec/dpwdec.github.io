---
title: Explicit Dependencies
layout: page
exclude: true
---

Pulumi has its own internal dependency graph for making sure that resources are created in the correct order. However, this is not fool proof. For example, policy configurations in AWS are not registered as dependencies automatically, however if access is required for creating infrastructure without it then the pulumi deployment will break.

You can **explicitly define dependencies for a pulumi resource** using the `DependsOn` field in the `CustomResourceOptions` object for resource creation point at the resource which this resource depends on.
```csharp
// create a resource that won't trigger implicit depdencies
var configResource = new Config("config-resource");

var dependent = new DependentResource(
    "dependent-resource",
    new CustomResourceOptions
    {
        DependsOn = configResource
    }
)
```