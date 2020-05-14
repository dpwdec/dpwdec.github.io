---
title: Jasmine
layout: page
exclude: true
---

## Spies

The Jasmine equivalent of a doubles and mocks are spies. These have the same functionality of stubbing methods, receiving calls and having pre-defined returns.

You can **create a spy object** using the `creatSpyObject` method and then submitting the name of the object that spy describes and an array of strings which represent the methods that the spy object can receive.
```js
mySpy = jasmine.createSpyObject('spy', ['greet'])
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE5MjgyNjUzNCwtNTg5OTI1OTMwXX0=
-->