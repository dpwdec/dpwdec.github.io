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

You should **use `'` single quotes for strings** unless you are writing in `JSON`.
```js
var myString = 'my string';
```

## Variables
You can **define a new variable in Javascript** using the `var` keyword.
```js
var x = 5;
```

### Undefined

An **unassigned variable returns `undefined`**.
```js
var a; // => undefined
```

If you **add a number `undefined` variable** you will get the type `NaN` for "Not a Number".
```js
var a; // => undefined
a + 5; // => NaN
```

If you a **add a string to an `undefined` variable** you will get the word `"undefined"` as a string literal.
```js
var a;
a + ""; // => 'undefined'
```

## Strings

You can **place `"` double quotes directly into `'` single quote strings**.
```js
var sampleText = 'She came in and said "Good Morning." to everyone.';
```

You can **place `"` double quotes inside `"` double quotes by escaping them**.
```js
var sampleText = "She came in and said \"Good Morning.\" to everyone.";
```

You can **use the `+=` operator to concatenate and assign the string result**.
```js
var text = 'Some text.';
text += ' And some more text.'; // => 'Some text. And some more text.'
```

You can ** get the length of a string** using the string `length` function.
```js
'Hello'.length; // => 5
```

The **contents of strings are immutable**.  This immutability refers only to the actual string objec

You can **return a specific sub-string character of a string** by appending `[ ]` square brackets to its end as if it were an array and placing the index of the character you want to output.
```js
'Hello'[0]; // => 'H'
```

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

## Objects

A basic javascript object is **structured like a hash in ruby** or a **struct in Rust**. It stores information in key value pairs. Objects are defined using `{ }` curly brackets and `:` to indicate assignment from key to value. 
```js
var cat = { legs: 4, sound: 'meow' };
```

You can **retrieve values from an Object** using `.` syntax and the name of the key.
```js
var cat_sound = cat.sound; // => 'meow'
```
You can **assign key values to an Object key** by using `.` syntax and the name of the key with an assignment with `=`. This is also the same syntax for **defining a new key and value pair** to the dictionary.
```js
cat.legs = 10;
cat.name = 'Muffins';
```

You can **assign functions to object keys**. When that key is called on the dictionary the function will be executed.
```js
var catScratch = function() {
  return 'Cat scratches you!';
};
cat.scratch = catScratch; // => 'Cat scratches you!'
```

You can also **define functions inside the object definition**. Note that the end of the `{ }` definition for the function within the dictionary does not have a `;` semi-colon appended to it.
```js
var cat {
  speak: function() {
    return 'Meow!';
  },
  legs: 4
};
cat.speak; // => 'Meow!'
```

You can **use the `this` keyword to use variables from inside the object**.
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

You **cannot define class methods inside the class body** when using ES5, instead use the `pototype` field to add methods to the class.
```js
Antelope.prototype.myFunction = function() {
  return 'My name is ' + this.name
};
```

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

You can **define class and instance methods** inside the body of the class using the ES6 standard. You **can also use the prototype syntax** to add methods to ES6 classes.
```js
class Antelope {
  constructor(name) {
    this.name = name;
  }

  myFunction() {
    return 'My name is ' + this.name
  }
}
```

### Both Standards

You can **create a new instance of a class** using the `new` keyword followed by the object.
```js
// this new definition works for both ES5 and ES6
var antelope = new Antelope('Jonathan');
```

**Class and instance variables are public by default**. For example we can directly access and change the `name` parameter of an `Antelope` class instance object.
```js
antelope.name = 'Mark';
antelope.myFunction(); // => 'My name is Mark.'
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbOTczMTM1MTIyLC0xNTQwODYwNDE3LC0xNz
I2NzA3MzU5LDEwMDkyMDYyODYsMTUwMDYwODM2LC0yMTM3NDMx
NTgwLDY5MzU2Nzk1MiwxNjA2MTk1NDEyLC0xNDE5Nzg0NzAsOT
MxOTQzNjg2LDExNzI0MDU0MzQsMTY2NzY5OTYwNywtNzAzMzA3
MTY2LDE4MDc2NDYzMDYsLTU0MjgxMzgyMSwtMTkyNzI3MTkxMi
wtNzkzNzc5ODAzLDExMjYwMzUzNzQsMTUxMDIxNTI5NiwtMTE1
OTI1NzQyNV19
-->