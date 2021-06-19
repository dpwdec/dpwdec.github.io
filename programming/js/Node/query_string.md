---
title: querstring
layout: page
exclude: true
---

**Querystring** is a built in node utility for parsing query strings in client requests into a Javascript object as key-value pairs

You can **start using `querystring`** by requiring it.
```js
const qs = require('querystring')
```

You can **turn a querystring into an object** by using the `parse` method. The `querystring` utility is not intelligent enough to type values correctly and simply parses everything as a string.
```js
const query = 'name=Mephisto&age=908'
const values = qs.parse(query)
// => { name: 'Mephisto', Age: '908' }
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI5OTMwNzMwXX0=
-->