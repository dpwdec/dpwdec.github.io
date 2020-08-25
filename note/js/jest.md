---
title: Jest
layout: page
exclude: true
---

You can **run a specific test file** by using the `jest` command followed by the name of the test file. This will run all tests in that file.
```bash
$ jest myTestFile.spec.js
```


```js
genMocksFromModule()
```

## Automocks

Jest automocks allow you to generate a mock object automatically from a module. This feature will analyse the module that needs to be mocked and automatically return a mock object which contains mock methods that match the names of the original object. To **automock a dependency** use the `jest.mock` function and then import the dependency. In the example below the `Dependency` object is automocked turning the `greet` method into a `jest.fn` automatically which allows for assertions to made against its state, whether it was called, what arguments it received etc. Automocks are **useful for large objects** as mocking does not need to be done manually and the mock structure will change automatically.
```js
// dependency.js
const Dependency = {
  greet: () => { return "Hello" }
}
module.exports = Dependency;

// dependency.spec.js
jest.mock("./dependency.js");
const Dependency = require("./dependency.js");
it("has mocked the greet method", () => {
	Dependency.greet();
	expect(Dependency.greet).toHaveBeenCalled();
});
```
You can **extend automocks locally to a test suite** as you would with any mock.
```js

```

You can **extend automocks in a persistent manner across multiple test suites** with a **manual mock** by creating a `__mocks__` folder in the same directory as the module that is automocked and then generating an automocked version of the module, extending it, and then exporting it. When you can `jest.mock` on that module from a test file, the extended mock from the `__mocks__` folder will be used. In the example below the `greet` method is extended with a mock return value. This return value will be available in any test suite automocks this module.
```js
// __mocks__/dependency.js
let Dependency = genMockFromModule("../dependency.js");
Dependency.greet.mockReturnValue("Hello");
module.exports = Dependency;
```


### Testing Async Functions

You can **test an `async` function** by prefacing the asynchronous code with the `await` keyword and defining the test function as `async` as well.
```js
it("tests an async function"), async () => {
  let result = await asyncFunctionUnderTest();
  
  expect(result).toBe(true);
});
```

### Mocking Promises

You can **mock the resolve value of a successful promise** by assigning a `Promise.resolve` as the `mockReturnValue` of a mock function containing the value you want promise to resolve to.
```js
const returnValue = { message: "OK" };
let mockFunction = jest.fn();
mockFunction.mockReturnValue(Promise.resolve(returnValue));
```

You can **mock the reject error of a failing promise** by assigning a `Promise.reject` as the `mockReturnValue` of a mock function containing the error that you want the promise to fail to. *IMPORTANT:* If you add a `Promise.reject` to a jest test you must have a `catch` somewhere in the code you are testing otherwise the test will not be run and will yield no error message.
```js
const error = new Error("Promise failed.");
let mockFunction = jest.fn();
mockFunction.mockReturnValue(Promise.reject(error));
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIyMDAzMDAwOSwxNzQzNTQzMTE0LC0xOD
A4MjczODMyLDQ0ODc4OTMyNywtMTUwMTg1ODc0NiwtMTUwMDk1
NDY3MCw3NDg2MzkxMTVdfQ==
-->