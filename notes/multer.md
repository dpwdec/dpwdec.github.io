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
To **upload a single file to your server** use the `.single` method and set a `dest`ination where the file will be uploaded in the `options` object. This is probably the simplest upload pattern you can use. In the example below we use the `multer` method with an options object t
```js
var multer = require('multer');
// set server destination folder for uploaded files
var upload = multer({dest: './uploads'});
app.post('/', upload.single('file'), (req, res) => {
});
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzAyNjg0OSwtMjA2MzU0MTM3XX0=
-->