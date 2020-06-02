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
});
```

To **turn the mongoose schema into a class model** so that it can have methods and other static data etc. added to it use the `mongoose.model` method with parse the schema. This takes the `userSchema` created above and defines a `'User'` class like structure defined as the name of the object. Mongoose automatically pluralises the table names for these document types based on the name of the model submitted. In this case when a new `User` is saved for the first time a `Users` table will be created in the associated MongoDB database.
```js
let User = mongoose.model('User', userSchema);
```

You can **add custom methods to your mongoose models** using the `prototype` syntax. These methods can reference attributes defined in the database schema.
```js
User.prototype.introduce = function() {
  // a function using the name schema field on the user model
  return 'Hello, my name is ' + this.name
}
```

You can **export your model to the rest of the application for use** using the `module.exports` property with the mode
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk5NzI2NjI5NiwyMDI3MDMzMTI4XX0=
-->