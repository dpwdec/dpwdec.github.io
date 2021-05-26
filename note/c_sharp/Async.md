---
title: Async
layout: page
exclude: true
---

## Async and Await

You can **define an asynchronous block of code by** using the `async` keyword. Code marked with this keyword will expect to use the `await` keyword in its body.
```csharp
public async MyMethod()
{
  var result = await AsynchronousMethod();
}
```

While a particular part of your code is `await`ing the result of some asynchronous method, the **thread is NOT blocked**, this is an import distinction. Even though the execution of the local code that needs the result of the `await`ed asynchronous routing might be paused, the rest of the thread can still be used to run other resources, leading to better efficiency.
```csharp
public async MyMethod()
{
  Console.WriteLine("Start");
  var result = await AsynchronousMethod(); // <= Execution in this method pauses until complete
  Console.WriteLine(result);
  var extension = await AsynchronousAddMethod(result); // <= Execution in this method pauses until complete
  Console.WriteLine(extension);
}
``` 

## Task

`Task` is a structure in .NET that is **similar to a Promise in functional languages**. A `Task` object wraps the result of asynchronous code that can be `await`ed, allowing you to trigger multiple `Task`s running from an `async` code block.

### Asynchronous Tasks

You can **define an asynchronous method** by returning a `Task<TResult>` from the method, with the type set to the thing that the task should resolve to. This resolution takes place when the `await` keyword is applied to the result of the method that returns a `Task`. You only **need to return a result that matches the `TResult` type contained in the `Task`**, the conversion between the two is done automatically, however, the method itself **needs to use the `async` keyword** for this implicit conversion to run.
```csharp
public async Task<string> GetMessageAsync()
{
  Task.Delay(3000).Wait();
  return "Hello" // => implicitly converted into a Task<string>
}
```

`Task`s **begin running once the method that returns them is called**. This means you can trigger an asynchronous task before its result is needed by returning the `Task` type result of the asynchronous method and then calling `await` on it to resolve that task. This can result in faster run times in the local method because the asynchronous requests made for resources at the top of a method can be ready by the time method reaches the `await` clauses for the resource.
```csharp
public async MyMethod()
{
  // start the task running
  Task<string> messageTask = GetMessageAsync();
  // ... do other stuff
  // get the value of the result of the task
  string message = await messageTask;
}
```

You can **create a task that returns something** using the `Factory` property on a typed task with the `StartNew` method. This task can then be resolved as normal.
```csharp

```

### When

You can **`await` the completion of multiple tasks simultaneously** by using the `WhenAll` method. This method accepts an arbitrary number of tasks as its arguments and returns another `Task` that resolves when all the supplied tasks complete.
```csharp
Task<string> task1 = GetMessageAsync();
Task<string> task2 = GetMessageAsync();
Task<string> task3 = GetMessageAsync();

await Task.WhenAll(task1, task2, task3);
```

You can **get the combined results of a `WhenAll` call as a collection** by assigning the result of `await`ing `WhenAll` to a variable. This **only works if the tasks passed in ALL resolve to the same type**.
```csharp
Task<string> task1 = GetMessageAsync();
Task<string> task2 = GetMessageAsync();
Task<string> task3 = GetMessageAsync();

string[] results = await Task.WhenAll(task1, task2, task3);
// can also be written as: var results = await Task.WhenAll(task1, task2, task3);

for(var message in results) {
  // iterate through each message
}
```

You can **pass a collection of `Task`s to the `WhenAll` method** instead of a splat list of `Task`s. This can be a `List` or any array or other collection type.
```csharp
Task<string[] tasks = new Task<string>[] {
  GetMessageAsync(),
  GetMessageAsync(),
  GetMessageAsync()
}

string[] results = await Task.WhenAll(tasks);

for(var message in results) {
  // iterate through each message
}
```

### Delay

You can **make a thread wait for a set period of time** using the `Task` object with the `Delay` and `Wait` methods. `Delay` takes the wait time in milliseconds.
```csharp
// make the thread wait for 3 seconds
Task.Delay(3000).Wait();
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgyNTgwODQ5NywyMDIxODIyNTE2LDEzMD
cwNjMzMzksLTk4NzMyMzcxNCwxNTE1MjUyMTAyLC0xOTEzOTIz
MTY2LDEzMTU2MjAyMTUsLTEyMTM5NTQ4NzQsNTQxOTk3NzQzLC
0yNzM5NTk1MzcsLTE2Njg3NjcxM119
-->