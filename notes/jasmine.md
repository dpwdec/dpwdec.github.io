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
  expect(mySpy.greet).toHaveBeenCalled()
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
it('makes Math random return 203', function() {
  spyOn(Math, 'random').and.returnValue(203)
  expect(Math.random()).toEqual(203)
});
```

You cannot directly use the `toHaveBeenCalled` function on a real object you must stub it first. To **check that a stubbed method was called** use the `spyOn` syntax in conjunction with the `toHaveBeenCalled` method.
```js
it('call the random method on page', function() {
  spyOn(Math, 'random')
  // code that calls Math.random in some capacity
  expect(Math.random).toHaveBeenCalled()
});
```

You can **stub a method and make it return its real return value** using the `.and.callThrough` method. If yo
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI0Mzk4MzE4NiwtMTgwNDU2Mjc1NSwtMT
Q5NzkxMzY4MiwxNDk2MjA3NjQ2LC0xMjEzMjUxNDczLDExOTI4
MjY1MzQsLTU4OTkyNTkzMF19
-->