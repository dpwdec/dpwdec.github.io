---
title: JavaScript
layout: page
exclude: true
---

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

## `Var` vs `Let`

The `let` and `var` keywords are different ways of defining a variable in Javascript. The primary difference between them is their scoping and definition.

The `var` defined variable are scope

## Conditionals

Javascript **automatically coerces string and integer types when running a comparison**, such that writing out one number an an integer `5` and writing string containing just the character `'5'` will be evaluated as `true` when compared.
```js
if (5 == '5') // => true
```

You can **stop integers and the string forms of integers being compared as true** by using the **strict equality** operator `===`. This operator simply does not perform any type conversion on its arguments.
```js
if (5 === '5') // => false
```

The `!=` **inequality operator follows the same rule as the equality operator for type coercion**. There is also a **strict inequality** that works like the strict equality operator.
```js
if (5 != '5') // => false
if (5 !== '5') // => true
```

You can **return the result of a conditional directly from a function** by placing the conditional statement after a `return`
```js
function isNotEqual(a, b) {
  return a !== b
}
```

## Switch

To **match multiple conditions** use a `switch` statement. This allows to test a variable and match its value using a `case` block to execute a specific piece of code. 
```js
var myVar = 12;

switch (myVar) {
  case 12:
    console.log('it is twelve');
    break;
  case 13:
    console.log('it is thirteen');
    break;
}
// => it is twelve
```

**Statements inside a `switch` block are executed from the first match until a `break` is encountered**. This means, if you forget to add a `break` the code below, even though it does not match your condition will *also* be execute. As you can see from the example below the because the `break` statement is missing from the matched `case` statement of `12` the next block that matches `13` is also executed.
```js
var myVar = 12;

switch (myVar) {
  case 12:
    console.log('it is twelve');
  case 13:
    console.log('it is thirteen');
    break;
}
// => 'it is twelve'
// => 'it is thirteen'
```

You can **add a default return type** to a `switch` block using the `default` keyword.
```js
switch(n) {
  case 1:
    //some code
    break;
  // ...
  default:
    console.log('no value found');
    break;
}
```

You can **describe the same output for multiple inputs** by letting `case` blocks without keywords "cascade down".
```js
switch(n) {
  case 1:
  case 2:
  case 3:
    // do something
    break;
  case 4:
    // something else
    break;
}
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

The **contents of strings are immutable**.  This immutability refers only to the actual string object NOT the reference to the string. In the example below you can see that trying to change a string character by index leaves the value of `text` unchanged because the string is immutable. However the `text` variable that points to the string IS mutable and can be reassigned to a new string object entirely.
```js
var text = 'Bob';
text[0] = 'J'
text // => 'Bob' - string not changed
text = 'Job'
text // => 'Job' - text reassigned to a new immutable string
```

You can **return a specific sub-string character of a string** by appending `[ ]` square brackets to its end as if it were an array and placing the index of the character you want to output.
```js
'Hello'[0]; // => 'H'
```

You can **interpolate variables into a string** by surrounding your string with back-ticks and using a `${ }` symbol inside the string with the variable you want to interpolate placed between the curly brackets.
```js
var name = 'Dec';
console.log(`My name is ${name}.`);
```

## Arrays

You can **access the content of multi dimensional arrays** using two consecutive sets of `[ ]` square brackets.
```js
var array = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

array[1][0] // => 4
```

You can **add an element to the end of an array** using the `push` function. You can **add an element to the start of an array** using the `unshift` function.
```js
var array = [4, 5, 6];
array.push(7); // => [4, 5, 6, 7]
array.unshift(3); // =>[3, 4, 5, 6, 7]
```

You can **remove an element from the end of an array** using the `pop` function. You can **remove an element from the start of an array** using the `shift` function.
```js
var array = [4, 5, 6];
array.pop(); // => [4, 5]
array.shift(); // => [5]
```

## While



## Functions

You can **define a function** using the `function` keyword.
```js
function myFunction(parameter) {
  console.log(parameter);
}
```

Javascript functions are treated just like regular variables. You can **assign an un-named function to a `var`** using `=` to name the function.
```js
var myFunction = function() {
  return 'hello';
};
```

You can **call a function** by appending `()` to the end of the variable name that describes the function.
```js
myFunction(); // => 'hello'
```

If you define a variable in a function without using the `var` keyword. Then **the function variable will be in the global scope**. The global variable is only assigned when the function is called. To **limit variables to the local scope of the function** the `var` keyword inside functions!
```js
function myBadFunction() {
  globalVariable = 5;
}
globalVariable // => 5

function myBetterFunction() {
  var localVariable = 5;
}
localVariable // => undefined
```

**Any variables defined in the main code are available in the `function` scope**. If a **local and global variable conflict** then the **local variable takes precedence**.
```js
var myVar = 5;
function myAdder() {
  return 10 + myVar;
}

myAdder(); // => 15

function conflict() {
  var myVar = 10;
  return 10 + myVar;
}

conflict(); // => 20
```

A **function returns `undefined`** if you do not add a `return` statement to it.
```js
function myUndefined() {
  console.log('Return type is undefined');
}

myUndefined(); // => undefined
// => Return type is undefined.
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
You can **re-assign new key values to an Object key** by using `.` syntax and the name of the key with an assignment with `=`. This is also the same syntax for **defining a new key and value pair** to the dictionary.
```js
// redefine existing properties
cat.legs = 10;
cat.sound = 'Prrrr';
// add a new property
cat.name = 'Muffins';
```

You can **`delete` a property from an object** using the `delete` keyword.
```js
delete cat.legs
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
var cat = {
  speak: function() {
    return 'Meow!';
  },
  legs: 4
};
cat.speak; // => 'Meow!'
```

You can **use the `this` keyword to use variables from inside the object**.
```js
var cat = {
  speak: function() {
    return `I have ${legs} legs!`
  },
  legs: 4
};
cat.speak; // => 'I have 4 legs!'
cat.legs = 5;
cat.speak; // => 'I have 5 legs!'
```

You can **use integers or strings as object keys**. Any non-string objects will be automatically coerced into strings, however when using integers you can still access the keys value using a literal integer. These types of key properties **cannot be accessed with `.` notation**.
```js
var robot = {
  'a string': 10,
  7: 'number'
};
```

You can **access multiple word properties and integer properties** using `[ ]` square bracket notion. This also **allows you to access key names** dynamically using substitution.
```js
robot['a string'] // => 10
robot[7] // => 'number'
robot['7'] // => 7
```

You can **check if an object has a named property** using the `hasOwnProperty()` method.
```js
cat.hasOwnProperty('sound'); // => true
cat.hasOwnProperty('age'); // => false
```

You can **store objects as values of keys *inside* another object**. You can **access these "nested objects"** using double dot notation. You can also **use `.` and `[ ]` notation interchangeably**:
```js
var computer = {
  motherBoard: {
    cpu: 'G-Series',
    cooling: '5xx'
  }
};

computer.motherboard.cooling // => '5xx'
computer['motherBoard'].cpu // => 'G-Series'
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

## Console

You can **print to the `std_out`** using the `log` function on the `console` object.
```js
console.log('message to the std_out');
// => 'message to the std_out'
```

You can **submit multiple arguments to be printed** to the `log` function.
```js
var first = 'hello';
var second = 'there';
console.log(first, second);
// => 'hello there'
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NDcxOTIzNDUsLTU5OTI0MDQyMiwxMT
gxNjIyMTU2LC01MDI0OTg0OTYsLTEyMjM2ODQwMDMsODc0MDk3
MDQxLDc4MDM3NjEyNyw0MzA5Nzg1NTEsNjg2ODk2Mjk1LC0xMD
MwMTg1MzY3LC0xNTQwODYwNDE3LC0xNzI2NzA3MzU5LDEwMDky
MDYyODYsMTUwMDYwODM2LC0yMTM3NDMxNTgwLDY5MzU2Nzk1Mi
wxNjA2MTk1NDEyLC0xNDE5Nzg0NzAsOTMxOTQzNjg2LDExNzI0
MDU0MzRdfQ==
-->