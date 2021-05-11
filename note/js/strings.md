---
title: Strings
layout: page
exclude: true
---

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

You can **replace all occurrences of a set of characters** in a string using regular expression paired with the `replace` function with the `g` flag appended to the end of the regex. The `+` regex modifier does not work for this functionality in javascript.
```js
"some* string}[& with^ w#eird stuff$$ in@".replace(/[^a-z\s]/g, '')
// => 'some string with weird stuff in'
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUwNzU4ODk5Ml19
-->