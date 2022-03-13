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