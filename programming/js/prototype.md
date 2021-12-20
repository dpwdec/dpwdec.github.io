---
title: Prototype
layout: page
exclude: true
---

You can **get a list of ALL properties on an object** using the `getOwnPropertyNames` in conjunction with the `getPrototypeOf` function. This combination will return all properties *including* **inherited** properties from other prototypes. If you just use the `getOwnPropertyNames` directly on the object then you will only get the properties available and implemented on that specific object rather than the entire prototype chain.
```js
var properties = Object.getOwnPropertyNames(Object.getPrototypeOf(myObject))
```