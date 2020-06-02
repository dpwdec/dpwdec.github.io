---
title: MongoDB
layout: page
exclude: true
---

**MongoDB** is a **noSQL** (not only sql) database system. Instead of using lots of tables to model relationships between data types Mongo instead encodes data more like a traditional object (or JSON) file as key-value pairs in records called **documents**.

## Mongoose

Mongoose is an javascript ORM used with MongoDB to define database schema and access data. You can start using Mongoose by installing using `npm` and then `require` it in the files where you are going to use the Mongoose library. 
```js
let mongoose = require('mongoose')
```

You can **define a database schema** by creating a new `mongoose.schema` and adding the possible fields a document in this table could take.
```js
let userSchema = new mongoose.schema({
  name: String
})
```

To **turn the mongoose schema into a class model** so that it can have methods and other static data etc. added to it use the `mongoose.model` method with parse the schema.
```js
let User = mongoose.model('User', userSchema);
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk4OTA5MTE2NywyMDI3MDMzMTI4XX0=
-->