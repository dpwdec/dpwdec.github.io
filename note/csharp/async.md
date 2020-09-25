---
title: Async
layout: page
exclude: true
---

You can **define an asynchronous block of code by** using the `async` keyword. Code marked with this keyword will expect to use the `await` keyword in its body.
```csharp
public async MyMethod()
{
  var result = await AsynchronousMethod();
}
```

## Task

`Task` is the .NET **equivalent of a Promise in functional languages**. A `Task` object wraps the result of asynchronous code that can be `await`ed, allowing you to trigger multiple `Task`s running from an `async` code block.

You can **define an asynchronous method** by returning a `Task<TResult>` from the method, with the type set to the thing that the task should resolve to. This resolution takes place when the `await` keyword is applied to the result of the method that returns a `Task`.
```csharp
public Task<string> GetMessageAsync()
{
  
}
```

You can **make a thread wait for a set period of time** using the `Task` object with the `Delay` and `Wait` methods. `Delay` takes the wait time in milliseconds.
```csharp
// make the thread wait for 3 seconds
Task.Delay(3000).Wait();
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxNjI0MjgwMSwtMjczOTU5NTM3LC0xNj
Y4NzY3MTNdfQ==
-->