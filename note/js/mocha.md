---
title: Mocha
layout: page
exclude: true
---

You can **run mocha** by setting the `test` script in `npm` to `mocha`. Calling `npm test` will then run the mocha test suite.
```json
"scripts": {
  "test": "mocha"
},
```

You can **do assertions in mocha** by using the default `assert`ion library in node.
```js
const  assert  =  require('assert')

describe('Some test', () => {
  it('Equals something', () => {
    assert.strictEqual(10, 10)
  })
})
```

## Code Runner

You can **run mocha from a javascript file** to control how it runs and manage its configuration as code by using the `Mocha` object. This requires creating a `new` object with `mocha` and then adding the tests you want to `run`.
```js
const Mocha = require('mocha')
// instantiate mocha object
let mocha = new Mocha()
// add tests to be run
mocha.addFile('myTest.js')
// run test suite
mocha.run()
```

### Grep

You can **only run a specific tests in mocha** by using the `grep` command *on the `mocha` object* with a regex that matches those tests. The `grep` only applies to `it` blocks and does *not* filter by `describe`.
```js
mocha.grep('/foo/')
```

For the following set of tests **only the `foo` test would be run**.
```js
const  assert  =  require('assert')

describe('tests', () => {
  it('foo', () => {
    assert.strictEqual(10, 10)
  })
  
  it('bar', () => {
    assert.strictEqual(true, true)
  })
})
```

You can **invert mocha test selection** by appending the `invert` function to the `grep`. Given the example test cases above only `bar` would be run.
```js
mocha.grep('/foo/').invert()
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbNTAyMDMxMTMxLDc5ODcyODQ2OSwtMjEwNz
U1MjQ5Nl19
-->