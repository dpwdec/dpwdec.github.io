---
title: Functions
layout: page
exclude: true
---

The **types in anonymous functions are inferred** by typescript. The example below demonstrates how typescript tracks the internal type passed to the function.
```ts
let x = [1, 2, 3, 4];

x.forEach(n => n.toUpperCase()) // throws an error because number cannot be converted to upper case
```

There are **different type signatures for function definitions and parameterized functions or function types**. For example, for a standard function definition, the return type is indicated by a `:` followed by the type and then the body of the function with the `=>` hash rocket for arrow functions.
```ts
function x(a: string): string {
    return a;
}

const x(a: string): string => {
    return a:
}
```

However, for parameterized functions and function types the `=>` hash rocket makes up the signature of the function.
```ts
// type signature of a higher order function
function x(fn: (a: string) => void) {
    fn("Hello!");
}

// type signature of a function type
type x = (a: string) => void
```

## Function Properties

You can **define function types with additional properties** by adding the callable by component of the function as a property of an object definition. *How you actually define an object that matches this type schema is a mystery to me. It seems like you might be required to use classes and constructors.*
```ts
type descriptorFunction = {
    description: string,
    (a: number): number,
}
```

