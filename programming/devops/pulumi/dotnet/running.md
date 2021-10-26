---
title: Running
layout: page
exclude: true
---

You can **inject dependencies into Pulumi and complete pre stack creation initialisation** by passing a closure to to the `RunAsync` function on the Pulumi `Deployment` class which then completes set up and finally calls the stack creation function as a static method.
```csharp
using Pulumi;

// --snip--

static Task<int> Main(string[] args)
{
    return Deployment.RunAsync(() => {
        // do pre run set up here
        var someDependency = "some dependency";

        // Call stack and pass in dependencies
        MyStack.Run(someDependency);
    })
}
```

The associated stack would simply be a `static` class with the `Run` function.
```csharp
public static class MyStack
{
    public static void Run(string dependency)
    {
        // set up stack and use dependency
    }
}
```