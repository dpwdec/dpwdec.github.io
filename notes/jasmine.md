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

You can **check that method on a spy object has been called** by using the `toHaveBeenCalled` method.
```js
it('calls the greet method', function() {
  // code that calls the greet function from the tested object
  expect(mySpy.greet).toHaveBeenCalled();
});
```

You can **check that a specific argument was passed in with the spy objects method called** by using the `toHaveBeenCalledWith` function and submitting an argument which describes the expected input.
```js
it('calls the greet method', function() {
  // code that calls the greet function and passes in an argument from the tested object
  expect(mySpy.greet).toHaveBeenCalledWith('Dec');
});
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ5NjIwNzY0NiwtMTIxMzI1MTQ3MywxMT
kyODI2NTM0LC01ODk5MjU5MzBdfQ==
-->