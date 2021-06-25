---
title: Handlebars
layout: page
exclude: true
---

You can **access a property that is external to a handlebars for loop** by using `..` syntax. When your code moves into a for loop, properties are implicitly taken from the object that is currently available from iteration, by using `..` syntax you can specify that you want an external property.
```hbs
{{#each students}}
  This student is {{name}} and they are in class {{../class}}
{{/each}}
```

In the example above an object holds a list of `students` and a `class` property with the class they are in. This `class` property needs to accessible for templating within the `students` loop. By using the `..` syntax with specify that we want a property from the object a level "up", that holds the `students` object information.