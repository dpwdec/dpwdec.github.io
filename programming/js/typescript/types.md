---
title: Types
layout: page
exclude: true
---

There is a standard `Date` type built into Typescript. You can **construct a `Date` object** using the `new` keyword.
```ts
let now: Date = new Date();
```

## Aliases

You can **define an object type** using a `type` alias. The **fields can seperated by `,` comma or a `;` semi-colon**.
```ts
type Person = {
  name: string,
  age: number,
}
```

You can **define optional object properties** using a `?` question mark after the property name.
```ts
type Person = {
  name: string,
  age?: number,
}
```

If a value is not provided by a property defined as optional, then that property will be marked as `undefined`. This is useful because it means a runtime error will *not* be triggered if the property is accessed.

You can **alias union types**.
```ts
type Id = number | string;
```

You can **extend an existing type alias** by creating a new type using an *intersection*. This will inherit properties from the existing type and allow you to add new properties.
```ts
type Dog = {
  name: string,
  woofsPerSecond: number,
}

type Robodog = Dog & { // type intersection here
  operatingSystem: string,
}

const buzzo: Robodog = {
  name: "Buzzo",
  woofsPerSecond: 9000,
  operatingSystem: "woofSX",
}
```

## Interfaces

You can **use interfaces to define object types**.
```ts
interface Person {
  name: string,
  age: number
}
```

You can **add properties to an interface** by redefining it. It seems like this might also limit you from *totally* redefining an interface.
```ts
interface Person {
  name: string,
}

interface Person {
  age: numnber,
}

const person: Person = {
  name: "Mike",
  age: 444,
}
```

You can **extend an interface** using the `extend` keyword to create a new interface that inherits the properties of another interface and adds new properties.
```ts
interface Dog {
  name: string,
  woofsPerSecond: number,
}

interface Robodog extends Dog {
  operatingSystem: string,
}

const buzzo: Robodog = {
  name: "Buzzo",
  woofsPerSecond: 9000,
  operatingSystem: "woofSX",
}
```

## Aliases vs Interfaces

Generally aliases and interfaces can be used interchangeably. However there are some key distinctions.

Aliases are **static and cannot be redefined**.
```ts
type Animal = {
  name: string
}

// Error: Duplicate identifier 'Animal'.
type Animal = {
  petName: string
}
```

Interfaces **cannot be used to alias primitives**.

## Type Assertions

If a particular **complex type assertion is too constrained by the compiler but is known to be correct** it can be solved by chaining an assertion an `any` type and then to a target type.
```ts
const x = (result as any) as T;
```

## Literals

Literal values use type hints which constrain the possible values that a type can take. For example you could constrain a variable to a single string.
```ts
let x: "hello" = "hello";
x = "bonjour" // ERROR: "hello" is not assignable to "bonjour"
```

This is also how `const` values work but assinging a static type with a specific value. The above `let` is equivalent to assigning `x` to a `const` of `"hello"`.

You can **constrain values using literal type unions** so that only a specific set of values can be used.
```ts
type direction = "north" | "south" | "east" | "west";
let dir: direction = "north";
dir: direction = "up" // ERROR not assignable to type direction
```

**Literals are not automatically inferred** when defined inside objects. The properties `val` and `name` of the object below are inferred to be simply `string` and `number` and so can be mutated. They are **not literals** despite what defining a `const` object with such "typehint-like" assignments might suggest.
```ts
const x = { val: 0, name: "Quizzle" };
```

There are are **two ways to create object enclosed literals**:

1. Using the type assertions on the property when it is defined. This allows you to selectively choose which properties are literals.
```ts
const x = { val: 0, name: "Quizzle" as "Quizzle" }
```

2. Using `as const` after the object assignment to make *all* properties literals that are immutable.
```ts
const x = { val: 0, name: "Quizzle" } as const;
```

A full example of this behavior would be
```ts
const x = { val: 0, name: "Shima" };
x.val = 1;
x.name = "Buta";

const y = { val: 0, name: "Shima" as "Shima" };
y.val = 1;
y.name = "Buta"; // ERROR

const z = { val: 0, name: "Shima" } as const;
z.val = 1; // ERROR
z.name = "Buta"; // ERROR
```

## Null

### Non-null assertion operator

You can **assert that a value is not null** using the `!` exclamation mark postfix operator. This circumnavigates the typescript compiler requiring `null` checking in your code for values that know will not be `null` and removes the `null` type from the value. *You need to be careful with this as it is just away to get around compiler restrictions rather than actually performing any null checking*.
```ts
const testString = (x?: string | null ) => {
    console.log(x!.toUpperCase());
}

testString("hello"); // => "hello"
testString(null); // ERROR
```

