---
layout: page
exclude: true
title: dmd
---

rspec --documentation view

irb scripts.

UML - unified modelling language

wireframe.cc
diagram.codes

Class diagram displays classes and methods on them
A sequence diagram shows how different classes interact

where the arrow points indicates the method being called on that object

object --hello()--> thing
This calls the hello() method on the thing object.

return types are returned with dotted lines back --> this can contain the return type or even the value

There are 13 types of UML diagrams


why was I not able to use a CONSTANT for class methods inside my sinatra object?

the model CAN BE CONSIDERED AS ITS OWN APP

4xx are for user errors

you can have multiple servers running on a single machine
databases are visually referenced by a cylinder


NOT changes OR to AND and logical comparators to their inverse i.e. `>` becomes `<=`

INSERT INTO table_name (column_list)
VALUES
    (value_list_1),
    (value_list_2),
    ...
    (value_list_n);

the resistance

crc --> class responsibilities and collaborators
agile modeling class responsibility collaborator CRC

a responsibility is what a class knows, or what a class does

something is a collaborator of class if that collaborator is required for that class to complete its responsibilities.]

when you have a ONE TO MANY relationship you put the foreign key in the MANY table.

MANY to MANY relationships in a middle man table

es5 was the previous version js
in this syntax classes are define with functions
```js
function Parrot(name) {
  this.name = name;
}

//add a 
Parrot.prototype.speal = function() {
  alert('hello');
};

```

use the `debugger` function to pause execution and in chrome you can use the dev tools to step through your code in the `Sources` tab of the dev tools.

you can define fucntion inside classes without the function keyword

javascript hoistin

you can set a breakpoint inside chrome by clicking on a line number inside the sources tab

document.addEventListener('click' function() { }); --> add event listener to entire document

latentflip.com

javascript always executes everything in the main body outside of the callbacks

on jQuery form submission events
event.preventDefault()

change element

cypress can be used for end to end testing in javascript servers
## process modelling


immediately invoked function expression.
--> if you wrap a function in two sets of brackets it becomes an expression and is executed immediately.
```js
function something() { return 'hello' }
// => function
(function something() { return 'hello' })()
// => hello
```

```js
(function(context) {
  var name = 'Dec'
  
  function sayHello(name) {
    return name
  }
  
  context.sayHello = sayHello
})(this)

sayHello() // => 'dec'
```
You can encapsulate variables inside this outer context using closures.
Once a variable is set in this way, its set. You can't change it using a closure.
commonly `exports` will be the name used instead of `context` as a way to describe these contextual things.

when you define a function in the top level inside the browser, defined functions are stored on the `window` object.

first class functions means being able to pass functions around as arguments.

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUzNTgwMTc4MSwtMTM1Mzg4MjYzNiwtMz
IzODk2ODA2LC0xNzg2NDk1MzEzLDg5MzczMjQ3MCwtMTIxMzU0
MDQ0MiwxMDk0MTM0MTI0LC0xMTAwMjM3NDM3LC0xNzE5MTk1Mj
c0LC0xODUxMjI4ODIsMTM0NDUyMjE3OCwxNjY4Njc2ODQxLC0x
OTI4MDgyOCwxOTQxMjg1ODUzLC02MjY3MzgxNzMsLTE5ODc2Mj
kzNCwtMTY0NDg0NzY5MCwtNjQ5NjIwMDMzLC0yMDg1MDUxOTcx
LC0yMDM1ODc5NDA2XX0=
-->