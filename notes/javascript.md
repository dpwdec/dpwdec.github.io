## Style

You should use **lowerCamelCase** for **variables, properties and function names**.
```js
var myVarName = 'name';
var myFunctionName = function() {
  //some function
};
```

You should use **UpperCamelCase** for **class** names.
```js
class MyClass {
  //class definition
}
```

## Variables
You can **define a new variable in Javascript** using the `var` keyword.
```js
var x = 5;
```

## Strings

You can **interpolate variables into a string** by surrounding your string with back-ticks and using a `${ }` symbol inside the string with the variable you want to interpolate placed between the curly brackets.
```js
var name = 'Dec';
console.log(`My name is ${name}.`);
```

## Constants
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
You can **assign key values to a dictionary key** by using `.` syntax and the name of the key with an assignment with `=`. This is also the same syntax for **defining a new key and value pair** to the dictionary.
```js
cat.legs = 10;
cat.name = 'Muffins';
```

You can **assign functions to dictionary keys**. When that key is called on the dictionary the function will be executed.
```js
var catScratch = function() {
  return 'Cat scratches you!';
};
cat.scratch = catScratch; // => 'Cat scratches you!'
```

You can also **define functions inside the dictionary definition**. Note that the end of the `{ }` definition for the function within the dictionary does not have a `;` semi-colon appended to it.
```js
var cat {
  speak: function() {
    return 'Meow!';
  },
  legs: 4
};
cat.speak; // => 'Meow!'
```

You can **use the `this` keyword to use variables from inside the dictionary**.
```js
var cat {
  speak: function() {
    return `I have ${legs} legs!`
  },
  legs: 4
};
cat.speak; // => 'I have 4 legs!'
cat.legs = 5;
cat.speak; // => 'I have 5 legs!'
```

## Functions

Javascript functions are treated just like regular variables.

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

## Classes

There are **two ways to define classes** in Javascript. There is an **older ES5** standard that **uses the `function` keyword** and the **newer ES6** standard that **uses the new `Class` keyword**. 

### ES5

To **define instance variables** in ES5 use the `this` keyword inside the class definition.
```js
// ES5 class definition
var Antelope = function(name) {
  this.name = name;
};
```

Y

### ES6

To **define instance variables** in ES5 use the `constructor` block with the initialisation arguments and assignments placed inside.
```js
// ES6 class definition
class Antelope {
  constructor(name) {
    this.name = name;
  }
}
```

### Both Standards

You can **create a new instance of a class** using the `new` keyword followed by the object.
```js
// this new definition works for both ES5 and ES6
var antelope = new Antelope('Jonathan');
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbNDE2OTc4MzA0LC0yMTM3NDMxNTgwLDY5Mz
U2Nzk1MiwxNjA2MTk1NDEyLC0xNDE5Nzg0NzAsOTMxOTQzNjg2
LDExNzI0MDU0MzQsMTY2NzY5OTYwNywtNzAzMzA3MTY2LDE4MD
c2NDYzMDYsLTU0MjgxMzgyMSwtMTkyNzI3MTkxMiwtNzkzNzc5
ODAzLDExMjYwMzUzNzQsMTUxMDIxNTI5NiwtMTE1OTI1NzQyNV
19
-->