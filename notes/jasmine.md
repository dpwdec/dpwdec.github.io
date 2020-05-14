---
title: Jasmine
layout: page
exclude: true
---

## Spies

The Jasmine equivalent of a doubles and mocks are spies. These have the same functionality of stubbing methods, receiving calls and having pre-defined returns.

You can **create a spy object** using the `creatSpyObject` method and then submitting the name of the object that spy describes and an array of strings which represent the methods that the spy object can receive. In the example below the `mySpy` object that is passed to any other code will respond to the greet method.
```js
mySpy = jasmine.createSpyObject('spy', ['greet'])
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMTMyNTE0NzMsMTE5MjgyNjUzNCwtNT
g5OTI1OTMwXX0=
-->