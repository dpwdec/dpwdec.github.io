---
title: Service Prodiver
layout: page
exclude: true
---

You can **build a service provider** by creating a `ServiceCollection`, then configuring the collection and finally building the provider.
```csharp
using Microsoft.Extensions.DependencyInjection;

static void Main(string[] args)
{
  var serviceCollection = new ServiceCollection();
  var serviceProvider = serviceCollection
    // add services here
    .AddSingleton<ISomeInterface, SomeInterfaceImplementation>()
    .BuildServiceProdiver();
}
```

You can **get an instance of a configured service from a `ServiceProvider`** by using the `GetService` method with the `typeof` service that you want and a cast to that service type. This should be done using the source interface type.
```csharp
var someInterfaceInstance = (ISomeInterface) serviceProvider.GetDervice(typeof(ISomeInterface));
```