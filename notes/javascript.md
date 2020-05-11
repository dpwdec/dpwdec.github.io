## Variables
You can **define a new variable in Javascript** using the `var` keyword.
```js
var x = 5;
```

## Strings

You can **interpolate variables into a string** by using a `${ }` symbol inside the string with the variable you want to interpolate placed between the curly brackets.
```js
var name = 'Dec';
console.log('My name is ${name}.');
```

#### Constants
Constants are Javascripts **immutable** variables. They are defined using the keyword `const`.  
```javascript
const N = 204;
N = 300; //ERROR
```
Javascript are **actually just constant references to variables**. This means that you **cannot change a primitive constant**, but you **can change the properties of an object constant**. This changing principle goes for all types of objects including arrays, hashes etc.
```javascript
const profile = { name:"Tatsuki", age:"59" };
// change the age property of the profile object
profile.age = "60";
// CANNOT change profile to point to a new object
profile = { name:"Ogawa", age:"18" }; //ERROR
```

## Dictionaries

A dictionary is **javascript's equivalent of a hash**. It stores information in key value pairs. Dictionaries are defined using `{ }` curly brackets and `:` to indicate assignment from key to value. 
```js
var cat = { legs: 4, sound: 'meow' };
```

You can **retrieve values from a dictionary** using `.` syntax and the name of the key.
```js
var cat_sound = cat.sound; // => 'meow'
```
You can **assign key values to a dictionary key** by using `.` syntax and the name of the key with an assignment with `=`.
```js
cat.legs = 10;
```

## Functions

You can ** define functions in Javascript** using the `function` keyword and assigning it to a `var` using `=` to name the function.
```js
var myFunction = function() {
  return 'hello';
};
```

You can **call a function** by appending `()` to the end of the variable name that describes the function.
```js
myFunction(); // => 'hello'
```

You can **submit an argument to a function** by placing it inside the `function` definitions `()` brackets.
```js
var myFunction = function(name) {
  return 'hello ' + name;
};

myFunction('Dec'); // 'hello Dec'
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MjcyNzE5MTIsLTc5Mzc3OTgwMywxMT
I2MDM1Mzc0LDE1MTAyMTUyOTYsLTExNTkyNTc0MjVdfQ==
-->