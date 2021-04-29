---
title: Indexable Types
layout: page
exclude: true
---

**Indexable Types** allow you to add arbitrary indexable properties to typescript objects which are still constrained by types.

To **declare an indexable type** put the keyword `index` in `[]` square brackets with either a `number` or `string` type followed by the type that the index will hold. *Typescript objects can only be indexed by `number` of `string`*. In the example below we add an indexable `string` property - so that this object can indexed by arbitrary `string`s similar to a dictionary. We constrain this to only accept `number` types.
```ts
interface IMyObject {
  [index: string]: number
}

let MyObject = {}

MyObject["id"] = 20
```

You can **nest interfaces inside indexable properties**. If you try to add a value to an indexable field that does not match the declared type than typescript will not compile.
```ts
interface IMyObject {
  [index: string]: number
}

interface IPerson {
  name: string
}

let MyObject = {}

MyObject["person"] = {
  name: "Jamal"
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUyNjgwNDc3Nl19
-->