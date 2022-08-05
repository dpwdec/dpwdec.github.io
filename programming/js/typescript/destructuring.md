---
title: Destructuring
layout: page
exclude: true
---

You can **destructure an object with optional fields and provided defaults for those destructurings** by using the `=` assignment after the destructing syntax call. This will only assign the field if that property is undefined on the object.
```ts
type Foo = {
    bar?: string
}

const x: Foo = {
    bar: "Blue"
}

const y: Foo = {}

const { bar = "Red" } = x; // => "Blue"

const { bar = "Red" } = y; // => "Red"
```