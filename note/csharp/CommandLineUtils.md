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

     public Task<int> OnExecute(CommandLineApplication app)
     {
       // do CLI execution here
       return Task.FromResult(0);
     }
   }
 }
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM0NzA4Njc2MywtMTA5MzM3NzkyOSwxMz
Q3MDg2NzYzLC0xNTEyMTg3NDkwXX0=
-->