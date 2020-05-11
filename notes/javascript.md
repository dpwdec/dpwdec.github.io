
#### Constants
Constants are Javascripts **immutable** variables. They are defined using the keyword `const`.  
```javascript
const N = 204
N = 300 //ERROR
```
Javascript are **actually just constant references to variables**. This means that you **cannot change a primitive constant**, but you **can change the properties of an object constant**. This changing principle goes for all types of objects including arrays, hashes etc.
```javascript
const profile = { name:"Tatsuki", age:"59" }
// change the age property of the profile object
profile.age = "60"
// CANNOT change profile to point to a new object
profile = { name:"Ogawa", age:"18" } //ERROR
```

## Dictionaries

A dictionary is **javascript's equivalent of a hash**. It stores information in key value pairs. Dictionaries are defined using `{ }` curly brackets and `:` to indicate assignment from key to value. 
```js
cat = { legs: 4, sound: 'meow' };
```

You can **ret**


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIzMDQ4OTAxNywtMTE1OTI1NzQyNV19
-->