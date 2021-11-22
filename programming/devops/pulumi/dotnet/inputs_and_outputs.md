---
title: Inputs and Outputs
layout: page
exclude: true
---

You can **use deferred information** when writing pulumi code using the input and output system. For example, the platform specific ID of one resource may need to be known during running to create another resource that depends on it. The ID isn't resolved or known until later.

You can **get promised values relating to a resource** using the `Output` class with the `Apply` function. When a resource is created with properties that will be resolved in the future these properties are of type `Output<T>` where `T` is the type of contained property once resolved. To access these properties use the `Apply` function on the property which yields a closure where the property is accessible. The closure is then run once the property resolves upon the infrastructure being created.
```csharp
var someResource = new Resource();
someResource.DeferredProperty.Apply(property => {
    // do something with the property here
});
```

You can **often using `Output` types directly with pulumi `Input` types** without having to using the `Apply` functionality to access the property values. For example, a resource that requires input from another with resource in its constructor will automatically resolve the "future" of that output as appropriate. This is a quality of life adjustment that pulumi makes for you.
```csharp
var someResource = new Resource();
var someDependentResource = new DependentResource(
    new DependentResourceArgs
    {
        // here the deferred property can be used directly with no closure
        ResourceId = someResource.DeferredProperty
    }
);
```

You can **join outputs from multiple resources** using the `Output` class's `Tuple` function. This yields an `Apply` function that has a tuple as its input argument with all the resolved properties.
```csharp
var someResource = new Resource();
var someOtherResource = new OtherResource();

var dependentThing = Output
  .Tuple(someResource.DeferredProperty, someOtherResource.DeferredpProperty)
  .Apply(propertyTuple => {
    // properties are acessible inside this tuple
    var someResourceProperty = propertyTuple.Item1;
    var someOtherResourceProperty = propertyTuple.Item2;
    // do something with these properties
  });
```