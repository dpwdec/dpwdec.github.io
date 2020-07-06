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

You can **print out the name of a variable** using the Javascript `Object.keys` and submitting the variable to the `keys` hash.
```js
var myVar = 42
Object.keys({myVar})[0] // => 'myVar'
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

## The Global Object

The **global object is an object on which all global variables for your script are defined**. The global object is **client side javascript specific**, i.e. it is not a feature in `node.js`. In browser based javascript the default global object is `window`. At the top level scope, creating a new `var` will add it to the global object.
```js
var spam = 'spam';
window.spam; // => 'spam'
```

## `Var` vs `Let`

The `let` and `var` keywords are different ways of defining a variable in Javascript. The primary difference between them is their scoping and definition.

### Scoping

The `**var` defined variable are scoped to the function they are declared in** whereas **`let` defined variables are scoped to the block they are defined in and any blocks contained within that block**.

If you try to **use a `let` variable** in a block with a scope outside of the one it was defined in you will get a `ReferenceError`.
```js
{
  let spam = 'spam';
}
console.log(spam); // => ReferenceError
```

However if you **define a `var` variable inside a block** it will still be available outside of that block.
```js
{
  var spam = 'spam';
}
console.log(spam) // => 'spam'
```

You can still **access `let` variables from nested blocks**.
```js
function spamFunction() {
  let spam = 'spam';
  {
	console.log(spam); // => spam
  }
}
```

Furthermore **`var` defined variables are NOT available outside of the function they were defined in**.
```js
function spamFunction() {
  var spam = 'spam';
}
console.log(spam) // => ReferenceError
```

### Hoisting

**Variables define with `var` are hoisted**. This means that even before they are ever defined in the flow of execution of the code they are initialized with an `undefined` type meaning that they won't throw an error if used before their definition.
```js
function hoisting() {
  console.log(spam); // => undefined
  var spam = 'spam';
  console.log(spam); // => 'spam'
}
```

However **calling a `let` variable before definition results in a `ReferenceError**.
```js
function hoisting() {
  console.log(spam); // => ReferenceError
  let spam = 'spam';
  console.log(spam); // => 'spam' (but never gets executed due to error above)
}
```

### Global Object

At the top level scope **`var` defined variables are added as properties of the global object**, whereas **`let` define variables are not**.
```js
var spam = 'spam';
let ham = 'ham';

console.log(window.spam); // => 'spam'
console.log(window.ham); // => undefined
```

### Redeclaration

In `strict mode` you can **redefine `var` variables** however trying **redefining a `let` variable in a single scope will result in a syntax error**.
```js
'use strict';
var spam = 'spam';
var spam = 'yam'; // spam is replaced

let ham = 'ham';
let ham = 'eggs'; // SyntaxError
```

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

You **cannot multiply strings in Javascript**. For example, `'d' * 5` is not valid syntax for outputting `'ddddd'`, instead you should **use the `repeat` method on a string** to duplicate it. This returns the duplicated string.
```js
// with var
var letter = 'd'
letter.repeat(5) // => 'ddddd'
// directly in a string
'd'.repeat(5) // => 'ddddd'
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

You can **remove a specific item from an array** by using the array `filter` function. This works in ES6 only. In the example below any `item` that is not equal to `4` is placed back into the array.
```js
arr = [1, 2, 3, 4, 5];
arr = arr.filter(item => item !== 4); // => [1, 2, 3, 5]
```

## do ... while loops

`do ... while` loops follow the structure of having a piece of code placed in a `do` block followed by a condition for executing that code multiple time in  a `while` statement. Uniquely **`do ... while` loops always execute once before their conditions is evaluated**, because the condition is placed after the execution block. The basic definition syntax is:
```js
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 5);
// => 1 2 3 4 5
```

If you set `i = 5` with the same code `i` will still be printed once because **the `while` condition is not immediately evaluated**.
```js
let i = 5;
do {
  console.log(i);
  i++;
} while (i < 5);
// => 5
```

## Iterables


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

### Lexical Scoping

A **function define within another function has access to the variables of that function**. In the example below the `eggs` function has access to the `ham` variable because it is defined within the function scope. This is called **lexical scoping** and describes how the function `eggs` resolves the variable name `ham` as referring to the context in which it was define. This context is called the **lexical environment** of a function.
```js
function spam() {
  var ham = 'ham';
  function eggs() { // define the eggs function
    console.log(ham);
  }
  eggs(); // call the eggs function
}
spam(); // => 'ham'
```

### Closures

A **closure** refers to a situation in which the **lexical environment** of a function (i.e. the outer it was defined in) comes bundled with a reference to that function. In the example below, instead of all the `eggs` function within the `spam` function it is instead returned and assigned to the `beans` variable and then called. This is an example of a **closure** because even though the local `ham` variable that was defined inside the body of `spam` has been called and passed out of scope, `beans` as a copy of the inner function `eggs` keeps a reference to that variable and its value and can still return it as it were still contained within the **lexical environment** of the `spam` function.
```js
function spam() {
  var ham = 'ham';
  function eggs() { // define the eggs function
    console.log(ham);
  }
  return eggs; // call the eggs function
}
var beans = spam();
beans(); // => 'ham'
```

You can **uses closures to store lexical environments** as a way of configuring functions. In the example below, the `makeBreakfastFunction` returns a function that simple concatenates its initial argument with an argument that is placed into the returned function. By assigning this return to a `var` we created a **closure** that remembers the state of `main` when it was created. Essentially we store the environment at the definition of the returned function without having to reference outside variables. Because **closures allow to associate data with a function** similarly to how you might associate data with functions in a class. They can be useful any time you have a class that would have some data and only a single function.
```js
function makeBreakfastFunction(main) {
  return function(side) {
    return main + ' and ' side;
  };
}
var spamBreakfast = makeBreakfastFunction('spam');
var eggsBreakfast = makeBreakfastFunction('eggs');

console.log(spamBreakfast('beans'); // => 'spam and beans'
console.log(eegsBreakfast('beans'); // => 'eggs and beans'
```

The **data inside a closures lexical environment is persistent across all instances of that closure**. In the example below we create a closure with the `count` variable set to `0` and return a function `add` that adds one to the `count`. When we create a new `incrementer` from the `counter` function the `count` is initialised to `0` and then counts up every time the function object is called. If we create a new `incrementer2` it **resets the lexical environment for BOTH closures**. They both start back at `0` and both closure objects will alter the lexical environment. They are tied to it together.
```js
function  counter() {
  count = 0;
  function  add() {
    count += 1;
    console.log(count);
  }
  return  add;
  }
incrementer = counter();
incrementer(); // => 1
incrementer(); // => 2
incrementer2 = counter();
incrementer2(); // => 1
incrementer2(); // => 2
incrementer(); // => 3
```

When creating **nested functions**. Each function **has access to the closure scope of all enclosing functions**. In the example below each anonymous function has access to all the function scope above it. the function with argument `d` has access to the function of scope of the top level `add` function and every function in between.
```js
function add(a) {
  return function(b) {
    return function(c) {
      // function scope
      return function(d) {
	    // local scope
        return a + b + c + d;
      }
    }
  }
}
add(1)(2)(3)(4); // => 10
```

### Callbacks

A callback is a **function that is called somewhere in another function when passed as an argument** and usually executes once the calling functions body has finished executing.
```js
// caller function that takes a function as an argument and calls it
function caller(callback) {
  callback()
}

caller(function() {
  console.log('hello')
})
// => 'hello'
```

### IIFE

An IIFE or **immediately invoked function expression** involves containing a function inside a set of **grouping operator** parentheses `( )` followed by a further set of execution parentheses `( )`. The function below is immediately returned defined and executed with its return value.
```js
(function() { return 'hello' })() // => 'hello'
```

You can **submit an argument to the enclosing IIFE** by placing in the execution parentheses at the end of the code.
```js
(function(arg) { return arg })('hello') // => 'hello'
```

You can **define IIFEs with function names**, however the name will not be stored.
```js
(function sayHello() { return 'hello' })() // => 'hello'
```

You can use IIFE to **contain variables to avoid the global scope becoming polluted**. In the example below we may want to work with a `var` and have actions using the var execute immediately but keep the `var` names separate from the scope in which the code is executing in.
```js
(function antiPollution() {
  var message = 'hello'
  return message
})() // => 'hello'
// message => undefined
```

You can **add IIFE defined function to a particular scope while maintaining their context** using closures. In the example below, the `context` is some context or object that we want the `sayHello` method to be available in, we then add it as a variable to the context. This `sayHello` method can now retrieve the `message` variable, but the message itself is not in scope. This allows us to mediate what is accessible within particular scopes to particular methods.
```js
(function(context) {
  var message = 'hello'
  function sayHello() {
    return message
  }
  context.sayHello = sayHello
})(this)

message // => undefined
sayHello() // => 'hello'
```

### Arrow Functions

An arrow function allows you **condense the syntax for defining anonymous functions** by omitting the function keyword and using a `=>` hash rocket arrow instead. Arrow functions are anonymous by default, so to use them you need to assign them to a variable. Arrow functions also have the effect of preserving the `this` context that the function was defined in.
```js
let myFunction = () => {
  return 'hello'
}
```

You can **condense arrow functions to one line** and omit curly braces and `return` statements associated with them.
```js
let myFunction = () => 'hello'
```

You can **include argument in your arrow functions** by placing it between the brackets.
```js
let myFunction = (arg) => arg * 2
```

You can also **use arrow functions as callbacks in other functions**.
```js
setTimeout(() => {
  console.log('hello')
}, 500)
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

## JSON

JSON is a format for serializing javascript objects. You can **`parse` a JSON string into a javascript object** using the `JSON.parse` method.
```js
const json_string = '{"result":true, "count":42}';
const json_object = JSON.parse(json_string);
json_object.result // => true
json_object.count // => 42
```

You can **convert a javascript object to JSON** to be sent via an API call or other method by using the `JSON.stringify()` method.
```js
let myObject = {name: 'dec', age: 28}
JSON.stringify(myObject) // => "{"name":"dec", "age":"28"}"
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

You **can define methods outside of the class body** using the `pototype` field to add methods to the class.
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

### Prototype

Functions added to classes using `prototype` are separate from functions added *within* a class. If you define a functional class (ES5 syntax) with methods contained within, these methods will indeed be duplicated on each `new` object that you create from that class, however, they will be separate pieces within memory. However if you create functions on the `prototype` property of a class then that method will **exist in one place**, and class instances that refer to that `prototype` function will simply **reference** it.

In the example below, when creating a `new` instance of `Dog` the `sayName` function will be copied for each instance.
```js
function Dog(name) {
  this.name = name;
  
  this.sayName = function() {
    console.log(this.name);
  }
}
```

However, if the `sayName` function is added to `Dog` using prototype then every instance of `Dog` will share the same function.
```js
function Dog(name) {
  this.name = name;
}

Dog.prototype.sayName = function() {
  console.log(this.name);
}
```

When **overwriting a function** defined in *both* the class definition *and* `prototype`, the **class definition version of the function takes precedence**.
```js
function Dog(name) {
  this.name = name;
  
  this.sayName = function() {
    console.log(this.name);
  }
}

Dog.prototype.sayName = function() {
  console.log('woof');
}

let dog = new Dog('Banjo');
dog.sayName(); // => 'Banjo'
```

Using `prototype` is also useful for testing because it allows you to mock an entire function definition on a class rather than a function definition of a specific instance. For example, if `Dog` had an injected dependency of `Bark` and called `sound` on `Bark` this could be mocked in tests easily by simply creating a `prototype` object for `Bark` in our test suite. The `Dog` class would take in a new instance of `Bark`.
```js
function Dog(name, bark) {
  this.name = name;
  this.bark = bark;
}

Dog.prototype.sound = function() {
  console.log(this.bark.sound());
}
```
Then the associated test could create its own empty mock of `Bark`. So that there are no errors when `bark.sound()` is called during testing and our dependency has been mocked.
```js
fakeBark = function() {}
fakeBark.prototype.sound = function() {}
```

### Class Methods

You can **create the equivalent of a class method** in javascript by adding a method as a parameter directly to the a class object. You have to define the class methods outside of the class body.
```js
class MyClass {
  constructor() {}
}

MyClass.someClassMethod = function() { console.log('hello') }

// call class method
MyClass.someClassMethod() // => 'hello'
```

### Class Type
You can **return the name of the type of an object** (similar to returning the **class type** that an object is) by using the `constructor.name` property of an object.
```js
myString = 'hello';
myString.constructor.name // => name
```

## Scope

### This
Javascript's `this` keyword does not function in the most intuitive way i.e. it doesn't work in a traditionally object oriented way. The `this` keyword tends to refers to how a function was called depending on the enclosing object.
```js
function foo() {
  return this
}

foo() // => 'this' refers to the window (or other top level object) becuase it is called at the top level

obj = { bar: foo } // assign foo to the bar property of this object
obj.bar() // => 'this' refers to obj

new foo() // => 'this' refers to the objec that inherits from the foo prototype
```

As a side note **`this` does not exist for `prototype`** objects. It seems that `this` only comes into being once an object that inherits from the prototype has been instantiated. So **using `this` inside a `prototype` object WILL refer to that object instance**.
```js
function MyClass() { } 

MyClass.prototype.this // undefined

MyClass.prototype.foo = function() {
  this // => refers to an instance of MyClass
}
```

### Bind

One of the more "interesting" things about Javascript is that when you **extract a function from an object that uses the `this` keyword** into a variable. The thing that `this` points to will change to reflect the scope in which it was extracted into.  As a rule a **function's `this` refers to the place in which the function is being called not where it is defined**.

One way to think of this is that when you assign a *method* (i.e. a function that belongs to an object) to a variable outside of that object, it is no longer a method but **becomes a function** and therefore the use of `this` to refer to an internal instance variable no longer makes sense. In the example below when the function associated with `dog.talk` is assigned in the `talkFunction` variable it loses its connection to the dog object.
```js
let dog = {
  sound: 'woof',
  talk: function() {
    return this.sound
  }
}

dog.talk() // => 'woof'
let talkFunction = dog.talk
talkFunction() // => undefined
```

A good way to understand this loss of connection is to think about what the assignment actually does. It just **adds the function definition directly to the variable in question**. Therefore, its clear that a `this` defined outside of an object will be `undefined` as the `talk` variable on `dog` just points to a function definition.
```js
let talkFunction = function() {
  return this.sound
}
```

Variables in the scope into which functions are extracted that have the same namespace as those defined in the context of the extracted function will overwrite those defined within the function's context. In the example below, because `sound` is defined in the scope that `talkFunction` is extracted to, `this.sound` now points to `'meow'` as defined by the scope in which the function is running.
```js
let sound = 'meow'
let talkFunction = dog.talk
talkFunction() // => 'meow'
```

You can **`bind` a function to the specific object context** by using the `bind` keyword and submitting as an argument the object context that you want to bind to.
```js
let talkFunction = dog.talk
talkFunction.bind(dog)
talkFunction() // => 'woof'
```

### This with Callbacks and Objects

The problems with `this` means that `callback` or object functions placed into another function or object that have a reference to `this` will appear as undefined.
```js
function MyClass() {
  this.foo = 'bar'
}

MyClass.prototype.caller = function(callback) {
  console.log(this.foo)
  callback()
}

myClass = new MyClass()
myClass.caller(function() {
  console.log(this.foo)
})
// => 'bar' because first 'this' was called inside the prototype caller object and refers to the object instnace
// => 'undefined' because 'this' in the callback refers to the top level object still because the function is just placed outside
```

This becomes more confusing **when callbacks are placed inside `prototype`s**.
```js
function MyClass() {
  this.foo = 'bar'
}

function outerCaller(callback) {
  callback()
}

MyClass.prototype.caller = function() {
  console.log(this.foo)
  outerCaller(function() {
    console.log(this.foo)
  })
}

myClass = new MyClass()
myClass.caller()
// => 'bar' because first 'this' was called inside the prototype caller object and refers to the object instnace
// => 'undefined' because 'this' in the callback refers to the top level object becuase this function COULD BE defined outside of the prototype object entirely and then passed in
```

You **can use `bind` inside callback arguments** to access the `this` context that the callback is called in or the object that this refers to. This requires appending `bind` to the `{ }` inside the argument. In the example below the callback is bound to the `myClass` instance object so that `this` refers to `MyClass`.
```js
function MyClass() {
  this.foo = 'bar'
}

MyClass.prototype.caller = function(callback) {
  console.log(this.foo)
  callback()
}

myClass = new MyClass()
myClass.caller(function() {
  console.log(this.foo)
}.bind(myClass))
// => Bar
```

You can also **use the enclosing context of a `porotype`** with `this` to refer to a specific variable defined on an object. In the example below `bind(this)` is appended to the call back argument and because it is within a `prototype` definition the `this` will refer whatever `prototype` instance inherits from it.
```js
function MyClass() {
  this.foo = 'bar'
}

function outerCaller(callback) {
  callback()
}

MyClass.prototype.caller = function() {
  console.log(this.foo)
  outerCaller(function() {
    console.log(this.foo)
  }.bind(this))
}

myClass = new MyClass()
myClass.caller()
// => Bar
// => Bar
```

Another way to solve the issue of `this` with callbacks and other scopes, is to **use a `self` variable** that is assigned as the `this` context which you want in your callback or object and then referencing that in the callback. In the example below `self` is defined inside the `MyClass.prototype.caller` function as the `this` context of that `prototype` and then used in the callback function instead of `this`.
```js
function  MyClass() {
  this.foo = 'bar'
}

function  outerCaller(callback) {
  callback()
}

MyClass.prototype.caller = function() {
  console.log(this.foo)
  var  self = this
  outerCaller(function() {
    console.log(self.foo)
  })
}
myClass = new  MyClass()
myClass.caller()
// => Bar
// => Bar
```

Another possibility for solving this type of issue is to use an **arrow function** which means that the functions scope is looked as if were used like a variable, this means the scope that the function is used in inherits from that `this`.
```js
function  MyClass() {
  this.foo = 'bar'
}

function  outerCaller(callback) {
  callback()
}

MyClass.prototype.caller = function() {
  console.log(this.foo)
  outerCaller(() => {
    console.log(this.foo)
  })
}
myClass = new  MyClass()
myClass.caller()
// => Bar
// => Bar
```

## Privacy


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

## Strict Mode

`'strict mode'` allows you to write safer Javascript by removing some of the more idiosyncratic tendencies of the language. You can use `strict mode`:
- globally for an entire script
- in a function specific context

To ** use `strict mode` globally** place it at the beginning of your script at the top level before any other code.
```js
'strict mode';
// other code
```

To **use `strict mode` with a function** place at the start of the function before any other code.
```js
function strict() {
  'use strict';
  // function code
}
```

`strict mode` **stops variables that have not been explicitly defined from being used**. In regular Javascript mistyping a variable name with assignment results in the creation of a new global variable.
```js
'use strict';
x = 3.141 // => ReferenceError
```

You **cannot `delete` a function or variable** in `strict mode`.
```js
let spam = 'spam';

function ham(eggs) {
};

delete spam; // => SyntaxError
delete ham; // => SyntaxError
```

You **cannot duplicate a parameter name** in `strict mode`.
```js
function spam(ham, ham) {
};
// => SyntaxError
```

## Modules
Modules allow you to store interpolated Javascript code into a single file. These files can be named using the `.mjs` file extension, however, this only *HAS* to be the case when you use `node` if you want to use module specific features like the `export` and `import` keyword. When using a module on a webpage you must use `type="module"` inside the `<script>` tags to mark your `.js` files as modules to be loaded, again, if you don't in some way indicate that the file *is* a module then you will not be able to use some of the ES6 module features.
```html
<script type="module" src="./myModule.js"></script>
```

## Asynchronous Javascript

### Promises

The `Promise` class allows you to handle the results of asynchronous functions by wrapping them in a `Promise` object that accepts functions that will run depending on the results of that asynchronous function. In the function below `timeOutPromise` is defined with a single possible branch called `resolve`. The number of arguments passed into the `Promise` constructor is the number of branches that a promise can resolve to. This `resolve` function is called when the `setTimeOut` function completes after `1000`ms. After this definition the promise is called with each `then` clause (in this case only one) matching the different branches defined in the `Promise` constructor. Whatever value is passed into the matching promise resolution branch will be retrievable here.
```js
let timeOutPromise = new Promise(function(resolve) {
  setTimeOut(function() {
    resolve('done')
  }, 1000)
})

timeOutPromise.then(function(done) {
  console.log(done)
}) // => 'done'
```

### Async and Await

The `async` and `await` keywords allow you to define functions that use the resolve values of promise based asynchronous requests. Using the `async` keyword allows you to mark a part of your code as asynchronous and then use the `await` keyword to resolve a promise. In the example below, whatever is returned from the `resolve` of the `timeOutFunction` promise will be returned into the `result` variable. The body of this function will *wait* until this value has been returned before it continue executing. This is the only time you will get a direct value from a promise function, but its worth noting that this value is only available for the duration of the function.
```js
function timeOutFunction() {
  let timeOutPromise = new Promise(function(resolve) {
  setTimeOut(function() {
    resolve('done')
  }, 1000)
  })
  return timeOutPromise
}

async function myFunction() {
  let result = await timeOutFunction()
  console.log(result) // => 'done'
  return result
}
```

It's important to note that even though `myFunction` returns `result`, the `result` will not be available to synchronous code *outside* of `myFunction` that tries to use the result. In the example below calling `console.log` on `myFunction` will return a pending promise (because `async` functions returns promises, see below) that has not yet been resolved when the `log` function is executed thus it simply returns a `pending` promise. After this the `await` resolves `timeOutFunction` and the `log` within `myFunction` executes and prints the value directly. Importantly, to the **outer scope of an `asyn` function the value of `await` is never directly exposed** and is instead passed out as a value wrapped in a promise.
```js
console.log(myFunction())
// => promise { pending }
// => 'done'
```

If you wanted to resolve the result of `myFunction` in the outer scope you would have to use a standard `then` clause.
```js
myFunction().then(function(result) { console.log(result) })
```

Defining a function with the `async` keywords makes it return a promise automatically.
```js
async function myFunction() {
  return 'hello'
}
myFunction() // => Promise
```

You can **resolve this `async` returned promise** by placing a `function` into the `then` of the promise. This executes with whatever the resulting return of the originally defined `async` function was.
```js
async function myFunction() {
  return 'hello'
}

myFunction().then(function(resolve) {
  console.log(resolve)
}) // => 'hello'
```

### Async Loops
At times you made to **loop through a set of data and make an async request for each piece of data** and THEN execute some other code. Much of the information on this is drawn from [this][async] article about looping with async. For example, imagine you have a page that makes a server API request for some corresponding information about a list of users, on the server side you need to loop through the information of each user and fire off an asynchronous database request to gather information on each user and the once ALL those requests are finished finally send data back to the client, or execute some other procedure. In the examples below the server request is mocked by the asynchronous `userInformationServerRequest` function that uses `setTimeout` to return information about the user after `1000` milliseconds.

[async]: (https://zellwk.com/blog/async-await-in-loops/) 

A **forEach based async loop DOES NOT WORK with async**, it can never support `async` behaviour and does not recognise it . Looking at the code below you would expect the output to be `start` then looping with an `await` for each server request mocked by the `setTimeout` function that prints the transformed user information followed by `end`. However, in practice `start` and then `end` are printed followed by the information.
```js
// forEach async example --> DOES NOT WORK
var users = [{name:  'dec'}, {name:  'marc'}, {name:  'phil'}];

var userInfo = {
dec:  10,
marc:  1,
phil:  23
}

async  function  updateUserInformation(usersArray) {
  console.log('Start');
  usersArray.forEach(async  function(user) {
    await  userInformationServerRequest(user);
  });
  console.log('end');
};

function  userInformationServerRequest(user) {
  return  new  Promise(function(resolve) {
    setTimeout(function() {
      user.age  = userInfo[user.name];
      console.log(user);
      resolve(user);
    }, 1000);
  });
}

updateUserInformation(users);
// => Start
// => End
// { name: 'dec', age: 10 }
// { name: 'marc', age: 1 }
// { name: 'phil', age: 23 }
```

You can **use the `.map` method correctly process an array each element of which triggers an asynchronous request** by mapping the array to an array of promises that is then resolved with the `Promise.all` function. In the `updateUserInformation` information below we use `map` to map each `user` in the array to a new `Promise` that makes a mock server request and resolves with the updated user information. Then the asynchronous `Promise.all` function is used with `await` to resolve all the promises we returned from `map` before `log`ging them. Structuring async in this manner produces the behaviour in the correct order.
```js
// async map example
// ... variable declarations removed for brevity
// ... check example above for var declarations

async  function  updateUserInformation(usersArray) {
  console.log('start');
  var userInformationPromises = usersArray.map(function(user) {
    return  userInformationServerRequest(user);
  });
  var updatedUserInformation =  await  Promise.all(userInformationPromises);
  console.log(updatedUserInformation);
  console.log('end');
}

function  userInformationServerRequest(user) {
  return  new  Promise(function(resolve) {
    setTimeout(function() {
      user.age  = userInfo[user.name];
      resolve(user);
    }, 1000);
  });
}

updateUserInformation(users);
// => Start
// { name: 'dec', age: 10 }
// { name: 'marc', age: 1 }
// { name: 'phil', age: 23 }
// => End
```

You can also use **recursive async statements to model a loop WITHOUT relying on a traditional looping method** by passing down information through an `async` that calls itself. In the example below the `userInformationServerRequest` calls itself for each successive request mutating the input array on each execution before returning the mutated array through the `resolve` callback function when it reaches the end of the list.

```js
async  function  updateUserInformation(usersArray) {
  console.log('start');
  var startIndex =  0;
  var outputArray =  await  userInformationServerRequest(usersArray, startIndex);
  console.log(outputArray);
  console.log('end');
}

async  function  userInformationServerRequest(usersArray, index) {
  return  new  Promise(function(resolve) {
    setTimeout(async  function() {
      if(index === usersArray.length) {
        resolve(usersArray);
      } else {
        usersArray[index].age  = userInfo[usersArray[index].name]; //mutate array
        index++;
        var outputArray =  await  userInformationServerRequest(usersArray, index);
        resolve(outputArray);
      }
    }, 1000);
  });
}

updateUserInformation(users);
// => Start
// { name: 'dec', age: 10 }
// { name: 'marc', age: 1 }
// { name: 'phil', age: 23 }
// => End
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NDk5MzczODgsNTg1NjA1OTkzLC0xNT
c5NzgxMTI4LDEwMDA5NTk4NzksMTU2MTQ1MTMxOCwtOTMwODA2
MzM0LC0yMTAxNTYyNzcwLDIwNjQ2MjAxMTksMTM2ODQ0NDYwOS
wtNjA0NzUxNzA2LDE0MjczNjkzNDYsOTQ4MDgyODQ3LC0xMDI0
NDMwNzEsLTE4MDM5ODgwMzcsLTE5MjkyMDg5MTQsLTI5MDg2OD
Q3OSw2NTA2MzY1OTYsLTEwMTUxMTAyMDgsLTE0MTY2NzQxMSwx
MzIxOTE0MTczXX0=
-->