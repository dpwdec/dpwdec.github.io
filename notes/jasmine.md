---
title: Jasmine
layout: page
exclude: true
---

## Spies

The Jasmine equivalent of a doubles and mocks are spies. These have the same functionality of stubbing methods, receiving calls and having pre-defined returns.

### Spy Objects

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

You can **define a return type for spy object methods** using the `.and.returnValue` function.
```js
it('returns an expected value', function() {
  mySpy.greet.and.returnValue(true)
  expect(mySpy.greet()).toBe(true)
});
```

### Stubbing

You can **stub methods on a real object with a pre-defined return type** by using the `spyOn` method combined with the `.and.returnValue` function. In the example below the `random` method of the `Math` object is stubbed to always return `203`.
```js
it('it makes Math random return 203', function() {
  spyOn(Math, 'random').and.returnValue(203)
  expect(Math.random()).toEqual(203)
});
```

You cannot directly use the `toHavebee **check that a su**
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjA2MDY0ODk0LC0xNDk3OTEzNjgyLDE0OT
YyMDc2NDYsLTEyMTMyNTE0NzMsMTE5MjgyNjUzNCwtNTg5OTI1
OTMwXX0=
-->