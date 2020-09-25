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

### When

### Delay

You can **make a thread wait for a set period of time** using the `Task` object with the `Delay` and `Wait` methods. `Delay` takes the wait time in milliseconds.
```csharp
// make the thread wait for 3 seconds
Task.Delay(3000).Wait();
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU1Njg5NTY4OCwxNTE1MjUyMTAyLC0xOT
EzOTIzMTY2LDEzMTU2MjAyMTUsLTEyMTM5NTQ4NzQsNTQxOTk3
NzQzLC0yNzM5NTk1MzcsLTE2Njg3NjcxM119
-->