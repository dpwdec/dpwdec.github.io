---
title: Array
layout: page
exclude: true
---

You can **create an empty array in javascript without using an array literal** by using then `Array` method with an argument of `0`.
```js
Array(0) // => []
new Array(0) // => []
```

You can **create an empty array with a length** by using a larger length argument to the Array function.
```js
let x = Array(5)
x.length // => 5
```

## Methods

You can **check if even one element in an array meets a condition** using the `some` method.
```js
let x = [2, 4, 6, 7, 10]
x.some(e => e % 2 === 1) // => true
let x = [2, 4, 6, 8, 10]
x.some(e => e % 2 === 1) // => false
```

## Synchronous vs Async Iteration

You **cannot use `await` and with the `forEach` method** on an array. Each branch of the `forEach` method will trigger asynchronously and simultaneously, so the loop will not work if it needs to execute synchronously . 

You can **run a synchronous loop through an array** by using the `for...of` syntax.
```js
let x [1, 2, 3, 4, 5]
for (const n of x) {
  synchronousFunction(n)
}
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgwMDkzNjk0NF19
-->