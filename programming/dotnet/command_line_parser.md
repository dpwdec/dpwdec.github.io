---
title: Command Line Parser
layout: page
exclude: true
---

You can **extract the result of parsed arguments** into a seperate funtion to improve readability by passing an "operational" function in as an argument to the `WithParsed` function which takes the parsed options.

```csharp
class Program
{
    public class Options
    {
        [Options('x', Required = true, HelpText = "Some arguments", Default = "Hello World!")]
        public string X { get; set; }
    }

    static void Main(string[] args)
    {
        Parser.Default.ParseArguments<Options>(args)
            .WithParsed<Options>(OperationalLogic)
    }

    static void OperationanLogic(Options opts)
    {
        Console.WriteLine(opts.X); // => "Hello World"
    }
}
```