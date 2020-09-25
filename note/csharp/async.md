---
title: Async
layout: page
exclude: true
---

You can **define an asynchronous block of code by** using the `async` keyword. Code marked with this keyword will expect to use the `await` keyword and send requests

## Task

`Task` is the .NET **equivalent of a Promise in functional languages**. A `Task` object wraps an asynchronous request that can be `await`ed.

You can **make a thread wait for a set period of time** using the `Task` object with the `Delay` and `Wait` methods. `Delay` takes the wait time in milliseconds.
```csharp
// make the thread wait for 3 seconds
Task.Delay(3000).Wait();
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI2ODIwNDI4OCwtMjczOTU5NTM3LC0xNj
Y4NzY3MTNdfQ==
-->