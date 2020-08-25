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

Jest automocks allow you to generate a mock object automatically from a module. This feature will analyse the module that needs to be mocked and automatically return a mock object which contains mock methods that match the names of the original object. To **automock a dependency** use the `jest.mock` function and then import the dependency.
```js
// dependency.js
const Dependency = {
  greet: () => { return "Hello" }
}
module.exports = Dependency;

// dependency.spec.js
jest.mock("./dependency.js");
const Dependency = require("./dependency.js");

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
eyJoaXN0b3J5IjpbLTE2NTA4Mzc3NjMsMTc0MzU0MzExNCwtMT
gwODI3MzgzMiw0NDg3ODkzMjcsLTE1MDE4NTg3NDYsLTE1MDA5
NTQ2NzAsNzQ4NjM5MTE1XX0=
-->