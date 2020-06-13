---
title: Multer
layout: page
exclude: true
---

Multer is an express middleware for handling `multipart/form-data` from website forms, usually for file uploads. To use `multer`, simply `require` it and use the function returned by the `require` with a javascript object representing the options for the data handling and then insert the result of this function into your express routes.
```js
// app.js basic multer usage
var multer = require('multer');
// expand options into upload requirement
var upload = multer({options});
// specify form upload stream inside the upload method
app.post('/', upload.single('file'), (req, res) => {
  // req.file will have information about the uploaded file.
});
```

## Uploads
To **upload a single file to your server** use the `.single` method and set a `dest`ination where 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYxMTk1NjQwMywtMjA2MzU0MTM3XX0=
-->