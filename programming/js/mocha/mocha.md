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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMDc1NTI0OTZdfQ==
-->