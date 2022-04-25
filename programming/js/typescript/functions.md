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

You can **define function types with additional properties** by adding the callable component of the function as a property of an object definition. *How you actually define an object that matches this type schema is a mystery to me. It seems like you might be required to use classes and constructors.*
```ts
type descriptorFunction = {
    description: string,
    (a: number): number,
}
```

## Generics

You can **define a generic function** using a type parameter is `<>` angle brackets. Typescript does not require the type parameters to be state explicitly if it can infer the types.
```ts
function doSomething<T>(arr: T[]): T;
```

You can **constrain generic types** using the `extends` keyword and the pattern that input type must meet. In the example below the input of type `T` must have a property `length` that is a number.
```ts
type ILengthType = { length: number }

function longest<T extends ILengthType>(a: T, b: T): T {
    return a.length > b.length ? a : b;
}

longest([1, 2, 3], [5, 6]); // => [1, 2, 3]

longest(['a', 'b'], ['c', 'd', 'e']); // => ['c', 'd', 'e']

longest([1, 2], ['a', 'b', 'c']); // => ['a', 'b', 'c'] - This one is slightly weird, it feels like this should error
```

## Overloads

You can **overload a function** so that it takes multiple sets of parameters. This is done by defining 

- a set of *overload signatures* which represent an interface that can be called, and 
- a single *implementation signature* which is an underlying function implementation signature that combines the arguments from the overload signatures

In the example below the two overload signatures of the function use either one or two numbers. However the actual implementation of this is as a single functional with an optional second argument that may be undefined. The overload logic is therefore *implemented* inside the body of the function. *Which doesn't seem that useful really? 🤔*
```ts
// overload signatures
function multiplyOrNothing(x: number)
function multiplyOrNothing(x: number, y: number)
// implementation signature
function multiplyOrNothing(x: number, y?: number) {
    if (y !== undefined) {
        return x * y;
    } else {
        return x * 0;
    }
}
```
