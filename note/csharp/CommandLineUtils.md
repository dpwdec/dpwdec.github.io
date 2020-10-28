---
title: Command Line Utils
layout: page
exclude: true
---

You can **start a command line application with `HostBuilder`** to help facilitate crosscutting concerns, by installing the `CommandLine` extension to go with the `CommandLineUtils` library and using the `RunCommandLineApplicationAsync` function with `HostBuilder`.
```csharp
using System.Threading.Tasks;  
using McMaster.Extensions.CommandLineUtils;  
using Microsoft.Extensions.DependencyInjection;  
using Microsoft.Extensions.Hosting;  
  
namespace CLITest  
{  
  class Program  
  {  
    public static async Task<int> Main(string[] args)  
     {  
       var builder = new HostBuilder()  
         .ConfigureServices((hostcontext, services) =>  
         {  
           // dependency injection configuration here  
         });  
       return await builder.RunCommandLineApplicationAsync<MyCli>(args);  
     } 
   }

   class MyCli
   {
     // command line class configuration

     public Task
   }
 }
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzE3NTA0NzM4LC0xNTEyMTg3NDkwXX0=
-->