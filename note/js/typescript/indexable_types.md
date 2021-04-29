---
title: Indexable Types
layout: page
exclude: true
---

**Indexable Types** allow you to add arbitrary indexable properties to typescript objects which are still constrained by types.

To **declare an indexable type** put the keyword `index` in `[]` square brackets with either a `number` or `string` type followed by the type that the index will hold. *Typescript objects can only be indexed by `number` of `string`*.
```ts
interface IMyObject {
  [index: string]: number
}

let MyObject = {}

MyObject["
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MDA3MTUxMDNdfQ==
-->