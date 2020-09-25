---
title: Async
layout: page
exclude: true
---

## Task

`Task` is the .NET **equivalent of a Promise in functional languages**. A `Task` object wraps an asynchronous request that can be `await`ed.

You can **make a thread wait for a set period of time** using the `Task` object with the `Delay` and `Wait` methods. `Delay` takes the wait time in milliseconds.
```csharp
// make the thread wait for 3 seconds
Task.Delay(3000).Wait();
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI3Mzk1OTUzNywtMTY2ODc2NzEzXX0=
-->