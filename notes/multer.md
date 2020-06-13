---
title: Multer
layout: page
exclude: true
---

Multer is an express middleware for handling `multipart/form-data` from website forms, usually for file uploads. To use `multer`, simply `require` it and use the function returned by the `require` with a javascript object representing the options for the data handling and then insert the result of this function into your express routes.
```js
var multer = require('multer');
var upload = multer({options});

app.post('/', upload.single('file'), (req, res) => {})
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MjA2MTE2OSwtMjA2MzU0MTM3XX0=
-->