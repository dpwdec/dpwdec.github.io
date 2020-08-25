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

## Mocks

You can **chain mock return values** by calling a jest mock function and assigning the return property.
```js
outerMock = jest.fn();
outerMock.mockReturnValue({ innerMock: jest.fn() });
outerMock().innerMock.mockReturnValue("OK");
```

You can **mock the way classes and prototypes interact with the `new` keyword** by setting the mock object's `mockImplementation` to be a function that returns the result of the `new`.
```js
mockClass = jest.fn();
mockClass.mockImplementation(() => {
  return { name: "Belinda" }
});

mockInstance = new mockClass();
mockInstace.name // => Belinda
```

You can **mock global objects** (such as the `Date`) module by patching them directly from the global object.
```js
global.Date.now = jest.fn();
global.Date.now.mockReturnValue("01/09/2018");
```


## Automocks

Jest automocks allow you to generate a mock object automatically from a module. This feature will analyse the module that needs to be mocked and automatically return a mock object which contains mock methods that match the names of the original object. To **automock a dependency** use the `jest.mock` function and then import the dependency. It's important to note that **automocks DO NOT define any mock function return types** based on the current implementation. This has to be done manually. 

In the example below the `Dependency` object is automocked turning the `greet` method into a `jest.fn` automatically which allows for assertions to made against its state, whether it was called, what arguments it received etc. Automocks are **useful for large objects** as mocking does not need to be done manually and the mock structure will change automatically.
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
// dependency.spec.js
jest.mock("./dependency.js");
const Dependency = require("./dependency.js");
it("has mocked the greet method", () => {
	Dependency.greet.mockReturnValue("Hello");
	expect(Dependency.greet()).toEqual("Hello");
});
```

You can **extend automocks in a persistent manner across multiple test suites** with a **manual mock** by creating a `__mocks__` folder in the same directory as the module that is automocked and then generating an automocked version of the module, extending it, and then exporting it. When you can `jest.mock` on that module from a test file, the extended mock from the `__mocks__` folder will be used. In the example below the `greet` method is extended with a mock return value. This return value will be available in any test suite automocks this module.
```js
// __mocks__/dependency.js
let Dependency = genMockFromModule("../dependency.js");
Dependency.greet.mockReturnValue("Hello");
module.exports = Dependency;
```

Another potential problem is that  **automocks persist changes to their data between tests** within a single test suite. This means that if you want to temporarily make your mock functions throw an error within a test and then change reset back to their original value as defined in your `__mocks__` file, you can't just import them directly inside your test file. To **scope your automock and manual mock objects** use the `resetModules` and `require` functions *inside* your tests `beforeEach` function. The `resetModules` removes all test specific changes made to the mock and the `require` within test set up reloads the original implementation leading to a cleaner separation of mock functionality. You **should still include your call for jest to mock** at the head of the file.
```js
// dependency.spec.js
jest.mock("./dependency.js");

describe("Dependency Test", () => {
  let Dependency;
  beforeEach(() => {
    jest.resetModules();
    Dependecy = require("./dependency.js");
  });
  
  it("has a return value", () => {
	Dependency.greet.mockReturnValue("Hello");
	expect(Dependency.greet()).toEqual("Hello");
  });

  it("has a reset return value", () => {
	expect(Dependency.greet()).toEqual(undefined);
  });
});
```

You can **make instance of automocks  extensible and modifiable within tests** by creating a "private" mock method on the original mock object, assigning that to a property of the `mockImplementation` return object and then changing the outer method on a per test basis.
```js
// __mocks__/mockClass
let mockClass = genMockFromModule("../mockClass.js");
mockClass = jest.fn();
mockClass._greet = jest.fn();
mockClass.mockImplementation(() => {
  return { greet: mockClass._greet }
});
module.exports = mockClass;

// mockClass.spec.js
jest.mock("./mockClass");
const mockClass = require("./mockClass");

it("sets a greet return value of an instance for this test", () => {
  mockClass._greet.mockReturnValue("Hello");
  mockInstance = new mockClass();
  expect(mockClass.greet()).toEqual("Hello");
});
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
eyJoaXN0b3J5IjpbLTMxODA2Mjg0LDQ5MTAxNzE0NywxMDE2Nz
c5MjY0LDE3NDM1NDMxMTQsLTE4MDgyNzM4MzIsNDQ4Nzg5MzI3
LC0xNTAxODU4NzQ2LC0xNTAwOTU0NjcwLDc0ODYzOTExNV19
-->