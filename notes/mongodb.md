---
title: MongoDB
layout: page
exclude: true
---

**MongoDB** is a **noSQL** (not only sql) database system. Instead of using lots of tables to model relationships between data types Mongo instead encodes data more like a traditional object (or JSON) file as key-value pairs in records called **documents**.

# Mongoose

Mongoose is an javascript ORM used with MongoDB to define database schema and access data. You can start using Mongoose by installing using `npm` and then `require` it in the files where you are going to use the Mongoose library. 
```js
let mongoose = require('mongoose')
```

## Schemas
You can **define a database schema** by creating a new `mongoose.schema` and adding the possible fields a document in this table could take.
```js
let userSchema = new mongoose.schema({
  name: String
});
```

You **cannot embed object types directly into a mongo schema**

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

You can **export your model to the rest of the application for use** using the `module.exports` property with the model class created from your schema. 
```js
module.exports = User;
// You can also export it directly if you don't want to add custom methods to yout model
module.exports = mongoose.model('User', userSchema);
```

You can **create a new instance of a model** by passing the constructor a javascript object that contains the key value pairs that describe the schema fields to be filled. The model object will then have the corresponding fields filled with the data defined in the constructor.
```js
let User = require('./models/user')

let newUser = new User({
  name: 'dec'
})
```

You can **save a new record to the database** using the `.save` method on the Mongoose model instance. The `save` function takes a callback with a save error as its argument.
```js
newUser.save(function(err) {
  //do something if there is an error or success
})
```

## Sub-documents


## Queries
You can **retrieve a list of objects from the database** using the `find` method. The `find` method takes a call back that executes once the query to the database has returned. It returns either an error to the first `err` argument of the callback or the `result` of the `find` query to the second `result` argument of the query. 

Using the `find` query without any arguments **retrieves ALL records from the database** of that database schema type as an array of objects.

**Objects returned from `mongoose` queries are instances of the model that defines them.** This means that you don't need to coerce any of the data returned from a `mongoose` query (such as `find`) into any instance of the model object before using custom defined model methods. In the example below we can immediately call the custom `someMethodDefinedOnMyObjectModel` on `item` immediately. 
```js
MyObject.find(function(err, result) {
  result.forEach(function(item) {
    console.log(item) // => some model instance of MyObject
    item.someMethodDefinedOnMyObjectModel();
  });
});
```

You can **submit selection parameters to `mongoose` queries** to selection criteria for what is returned from the database. This is similar to using `WHEN` in `SQL`. **Queries are submitted as JSON objects** which are matched to objects.
```js
// find query that returns all users with name = 'dec'
User.find({ name:'dec' }, function(err, result) {
  // do something with the result
});
```

You can **submit a list object fields to return** by submitting the fields you want returned as another query argument in the form of a space separated string. If you try retrieve a field on the object that was not retrieved it will simply be `undefined`. For example, if below the `User` model also had a `shoeSize` field that was not retrieved calling `.shoeSize` on each of the `result` objects would returns undefined even though the field might exist on the object's schema.
```js
// find query that returns an object with name, age and height for all users with name = 'dec'
User.find({name:'dec' }, 'name age height', function(err, result) {
  // do something with the result
});
```

You can **retrieve a single object from the database** using the `findOne` method.
```js
User.findOne({_id: 1}, function(err, result) {
  // do something with the single result
});
```

## Relations

You can **insert the database ID from another **

## Gotchas
You **cannot use the word `type` as a key inside a mongoose model**. This will be interpreted incorrectly by mongoose as a schema type leading to database errors.
```js
// DO NOT DO THIS
var myFailedSchema = new mongoose.Schema({
  type: String // causes errors in the database
});
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc0NDk0NDE1OCwtMTYzNzU4MTI5NywtMj
kyOTc3MjQ2LDY2MDU4NzcwOCw0MjE4MjI3MjMsLTE5OTAwMjQ1
MzQsLTkxODgwMDg0MCwtMTY1MzA4ODE5OSwtMTcyNTM4MTY2NS
w5NjM1Mjk0MTEsNjgwMDU3NzEzLDIwMTAyNTA4NDUsLTIxMzY4
OTE5MDMsMjAyNzAzMzEyOF19
-->