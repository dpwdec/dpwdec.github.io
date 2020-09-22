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

agile manifesto
SDET

consider encapsulating objects in module pattern to propogate and persist data about tests.

# Get the Middle Letter(s)

Requirements

-   The program runs in a REPL like  `irb`  or in a browser console.
    
-   It's fine to use Ruby or JavaScript.
    
-   Your job is to return the middle letter of a word. If the word's length is odd, return the middle letter. If the word's length is even, return the middle 2 letters.
    

#### [](https://github.com/makersacademy/skills-workshops/tree/master/process_review/exercises/middle_letter#acceptance-criteria)Acceptance Criteria

get_middle("test") # => "es"
get_middle("testing") # => "t"
get_middle("middle") # => "dd"
get_middle("A") # => "A"
get_middle("of") # => "of"

[https://gist.github.com/dpwdec/5a35cd93f160dcd072ce771d2c7720d1](https://gist.github.com/dpwdec/5a35cd93f160dcd072ce771d2c7720d1)

use JSON lint to validate JSON and see it in a nice format.

fetch
XMLHttpRequest
$.ajax()

endpoint refers to the route on the server that the external API call url refers to.

## method for quickly getting data out of an endpoint API call and experiment with it in the js console.
window.data = data // => allows you to get API call data into the browser console as an object and use it

would a production website actually make ajax calls for each headline?

```js
class Article {
  toHTML() {
  }
}
```
instead of returning data from a fetch promise based, pass in a callback to give your interface options for working with the data.

```js
function fetchSummary(callback) {
  fetch('some url').then(callback)
}

fetchSummary(function(data) {
  console.log(data)
})
```


Look up React components.
Use exhaustive feature tests.
JSX react addon --> needs to be compiled on the server and sent to the client --> JSX installed on the server side to convert jsx files
Stateless and stateful componenets
The stateless components are purely this is howto style this type of data
Stateful components also have logic 
COMPONENTS! <-- Think in terms of This







macros expanded into code

AGILE:

Always working end to end test

As a user,
So I can see my friends' responses to my posts
I would like to be able to see comments on posts.



engage with write ups
expand to use sub topics and maybe linking to repos maybe
SMART goals --> links
One long list


make ids non unique.


christopher Ly -cv
markdown drop downs
peppered with links
nice image inlining
video yourself coding

convert cv down into one page CV --> get things simple

story driven CVs
give yourself a personality
be weird
online conferencing


these are some gneeral notes, that I write and stuff, but thsi keyboard feels ok, but not amazing

`and doing backticks is far from ideal` especi `if` i need to type several things `with` backticks in it and keep things moving
```
x = 5
function(x) {
  5 * x / 2
}
```

oh no I've lost the ability to type / unfortunately `x` is all i am going to `be`.1\


`pi` and `poc`

what is `
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjM2OTQwNDIwLDE1NTQ0OTU3MDgsMjEwMj
E4NTExOCwtMTExNjU5NDUwMiwtMzMyMjY2OCwtMTI2MDA4NDYw
LDE4NTQ2ODU3MTgsMTg3NjUxNTk0OCwtNzc1ODA0NTk0LDg1Nj
U1MjIzMSw0NzM5NDE1NzgsMTI3Mjg4MjE2NywtMTM2MzczOTE4
OSw4NDE4MTUwNjYsMjIzNTQ1NDI4LC0xNjIyMzE3Mzk4LDU5OT
U5NTYzMSwtMjIxMjQ4NzYyLDE2MTQzNTUyNzQsLTI1MzIwNjQw
Ml19
-->