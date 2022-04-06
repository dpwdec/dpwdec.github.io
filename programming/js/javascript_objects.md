---
title: JavaScript Objects
layout: page
exclude: true
---

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

When **adding `function`s to objects that use the data on that object you must use the `function` keyword** otherwise the result of `this` will be undefined.
```js
let foo = {
  bar: 5,
  qux: function() {
    return this.bar * 2
  }
}
```

### Assign

You **can re-assign or copy the properties of an object to a different object** by using the `Object.assign` method which provides a powerful interface for *composing* objects. This `assign` will overwrite any already existing properties and add any new ones.
```js
let old = {
  name: 'Foo'
}

let updated = {
  name: 'Bar'
  age: 10
}

Object.assign(old, updated) 

console.log(old) // => { name: 'Bar', age: 10 }
```

You **can use this method with multiple source objects as well**. Here the `name` from `b` overwrite the `name` in `a` and the property `age` of `c` is copied over.
```js
let a = {
  name: 'Foo'
}

let b = {
  name: 'Bar'
}

let c = {
  age: 10
}

Object.assign(a, b, c) 

console.log(a) // => { name: 'Bar', age: 10 }
```

You can **re-assign a field of an object** by submitting a variable with the new value as an argument in `{ }` curly brackets. This will mutate the target object to update only part of it and carry over new information.
```js
let old = {
  name: 'Foo'
  age: 10
}

let age = 20

Object.assign(old, { age }) 

console.log(old) // => { name: 'Foo', age: 20 }
```

You can also **add properties to an existing object** by submitting a variable name to the `{ }` argument of `Object.assign` that isn't already on the object.
```js
let old = {
  name: 'Foo'
  age: 10
}

let height = 1.96

Object.assign(old, { height }) 

console.log(old) // => { name: 'Foo', age: 20, height: 1.96 }
```

### Destructuring

You can **destructure both Objects and Array**. The act of destructuring means breaking down a composite object into its component parts and extracting *copies* of them.

You can **destructure an array** by creating a mirrored array of varaibles and assigning to them.
```js
// in line syntax
const [t, u] = ['a', 'b'];
t; // => a
u; // => b

// after assignment syntax
const arr = ['c', 'd']
const [k, v] = arr;

k; // => c
v; // => d
```

You can **destructure an object** by putting the name of field you want to extract from the object in `{}` curly braces and assigning it from the object. This will take that property and assign it to the variable name.
```js
o = {
  foo: 'bar'
}

const { foo } = o;
foo; // => bar
```

You can **destructure multiple object fields simultaneously**.
```js
o = {
  foo: 'bar'
  baz: 'Qux'
}

const { foo, baz } = o;
foo; // => bar
baz; // => Qux
```

You can **assign a different name to your destructuring** by using `:` colon syntax inside the `{}` curly braces.
```js
o = {
  foo: 'bar'
}

const { FOO: foo } = o;
FOO; // => bar
```

You can **destructure objects in function arguments**.
```js
const copy = ({ name, age }) => {
  // name and age usable inside function here
}
```

You can also **set destructured defaults for function arguments**.
```js
const copy = ({ name = 'Anonymous', age = 0 }) => {
  // name and age usable inside function here
}
```

### Object Spread

There is a **shorter version of `Object.assign`** called the **object spread syntax** which uses `...` three periods before each object to be copied into anther object. All this does it iterate through the properties of the source object and assign or overwrite properties on the target object.
```js
const a = {a: 'a'}
const b = {b: 'b'}
const c = {...a, ...b} // => {a: 'a', b: 'b'}
```

## Value Of

You can **create an interface for javascript objects to work with arithmetic operators** by defining the `valueOf` function inside the object. In the example below the `makeObject` function will return an object with `valueOf` defined to return `value` in its lexical scope. When using operators like `+`, the `valueOf` function on the object will be called allowing for interaction with the value enclosed in the object.
```js
makeObject = value => ({
  valueOf: () => value
})

x = makeObject(20);
y = makeObject(30);
x + y // => 50
```

## Object Iteration

You can **iterate through the values of an object's fields with an index** by using the `Object.values` function to convert the entries and then the `entries` function to create an iterator.
```js
const x = { a: "a", b: "b" };
for (const [index, val] of Object.values(x).entries()) { 
  console.log(index, val) 
}
// => 0 a
// => 1 b
```