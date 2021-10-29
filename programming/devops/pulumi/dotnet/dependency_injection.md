---
title: Running
layout: page
exclude: true
---

You can **inject dependencies into a Pulumi stack** using a `ServiceProvider`. [The Pulumi API offers an overloaded version of the `Deployment.RunAsync` method](https://www.pulumi.com/docs/reference/pkg/dotnet/Pulumi/Pulumi.Deployment.html#Pulumi_Deployment_RunAsync__1_System_IServiceProvider_) that allows you submit a `ServiceProvider` to the stack and then get dependent from it within the stack as an argument in the stack constructor. *It's important to configure a singleton instance of your stack class for your service provider directly, an interface is **not** required.*
```csharp
namespace PulumiDependencyInjection
{
  class Program
  {
    static Task Main(string[] args)
    {
      var serviceCollection = new ServiceCollection();
      var serviceProvider = serviceCollection
      .AddSingleton<ISomeDependecy, SomeDependencyImplementation>()
      .AddSingleton<MyStack>() // add an instance of your stack
      .BuildServiceProdiver();

      return Deployment.RunAsync<MyStack>(serviceProvider);
    }
  }

  class MyStack : Stack
  {
    public MyStack(IServiceProvider provider)
    {
        // use provider here to get dependencies

        // do the rest of your Pulumi stack set up using the dependencies
    }
  }
}
```