---
title: Handlebars
layout: page
exclude: true
---

You can **create a custom string quality helper for handlebars in dotnet** using the following code.
```csharp
public static void Eq(EncodedTextWriter output, BlockHelperOptions options, Context context, Arguments arguments)
{
    var cmp = arguments[0] as string;
    if (arguments.Skip(1).Any(arg => (arg as string) == cmp)
    {
        options.Template(output, context);
    }
}
```

This helper can then be used in an `.hbs` document with a single or *set* of strings to match against as shown.
```hbs
{{ #eq MyVar "some string" }}
Template this if it was a match for the string.
{{ /eq }}

{{ #eq MyVar "some string" "another string" }}
Template this if it matched either of the strings.
{{ /eq }}
```