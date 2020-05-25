---
title: Jasmine
layout: page
exclude: true
---

## Testing Modules
You can test node modules and classes in Jasmine by using the `module.exports` syntax combined with `require` inside of your jasmine tests.  In the `myClass` file below, a class called `MyClass` is defined using ES6 syntax. Then at the bottom of the class it is added to the `module.exports` path.
```js
// src/myClass.js
class MyClass {
  constructor(name) {
    this.name = name
  }
  
  sayName() {
    return 'hello my name is ' + this.name
  }
}

module.exports = MyClass
```
With `MyClass` added to `module.exports` it can now be loaded inside a Jasmine test using `require` and the relative file path from the test to the source file that is `require`d.
```js
// spec/myClassSpec.js
describe('My Class', function() {
  var MyClass = require('../src/myClass') // load MyClass from the myClass.js file
  var myClassInstance

  beforeEach(function() {
    myClassInstance = new MyClass('Dec')
  })

  describe('sayName', function() {
    it('says the hello' function() {
      expect(myClassInstance.sayName()).toEqual(
    })
  })
})
```

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

You can **stub a method and make it return its real return value** using the `.and.callThrough` method. If you *just* `spyOn` on an object's function it will not return anything.
```js
it('stubs the function while maintaining the return value', function() {
  obj = { myFunction: function() { return 10 } }
  spyOn(obj, 'myFunction').and.callThrough()
  expect(obj.myFunction()).toEqual(10)
});
```

You can **stub and `spyOn` the class `prototype` methods** in the same manner as above. This allows you to pass in constructor (class) functions to an object. By then stubbing the function property in the `prototype` of a function all instances of that class will have a stubbed instance method.
```js
it('stubs a prototype function', function() {
  aClass = function() {}
  aClass.prototype.instanceFunction = function() {}
  aClassInstance = new aClass();
  spyOn(aClass.prototype, 'instanceFunction').and.returnValue(10);
  expect(aClassInstance.instanceFunct()).toEqual(10);
});
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzU1MTU5MzYwLDg5ODA3MDYyNiwxMDc3MD
M1NzM5LC0yMDAxNDQxNzgxLC0yMTAxNDgwMjU4LC0yMTQzODk2
ODY3LC0xODA0NTYyNzU1LC0xNDk3OTEzNjgyLDE0OTYyMDc2ND
YsLTEyMTMyNTE0NzMsMTE5MjgyNjUzNCwtNTg5OTI1OTMwXX0=

-->