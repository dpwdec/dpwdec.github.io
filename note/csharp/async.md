---
title: Async
layout: page
exclude: true
---

## Task

You can **make a thread wait for a set period of time** using the `Task` object with the `Delay` and `Wait` methods. `Delay` takes the wait time in milliseconds.
```csharp
// make the thread wait for 3 seconds
Task.Delay(3000).Wait();
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2Njg3NjcxM119
-->