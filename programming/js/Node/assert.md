---
title: Assert
layout: page
exclude: true
---

Node **supports assertions as part of the standard library** using the `assert` library. If an `assert` fails (without a test library) it will raise an `ERR_ASSERTION` exception.

You **start using node assertions** by `require`ing `assert`.
```js
const assert = require('assert')
```

You can **run a strict equality assertion** by using the `strictEqual` on the `assert` object.
```js
assert.strictEqual(10, 9) // => ERR_ASSERTION 10 !== 9
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNDI3NTQ3MjAsLTIxODExOTI5M119
-->