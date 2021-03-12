---
title: Child Process
layout: page
exclude: true
---

## Spawn

You can **execute a sub process on the command line** by using the `spawn` function from the `child_process` library. The `spawn` function takes a command to execute as an argument.
```js
const { spawn } = require('child_process')
spawn('ls') // command executes here
```

You can **use a command with arguments** by appending them as an argument to the `spawn` command as an array of strings.
```js
spawn('curl', ['-v', '-O', 'http://my_binary.org'])
```

The `spawn` function returns a `ChildProcess` instance object that supports a set of event listeners that occur when a `child_process` command runs. You can **access these event listeners** by assigning the output of the `spawn` command and using the `on` function of the `ChildProcess` object.

You can **access the output of a command** using the `stdout` property and the `on` function with `data`.
```js
const ls = spawn('ls')
ls.stdout.on('data', data => { console.log(data) })
```

You can **access command errors** using the `stderr` property and the `on` function with `data`.
```js
const ls = spawn('ls')
ls.stderr.on('data', data => { console.error(data) })
```

You can **trigger an event when the child process finishes** using the `close` event directly on the `ChildProcess` object.
```js
const ls = spawn('ls')
ls.on('close', code => { console.log(`Return code was ${code}`) })
```

### Async Child Processes

You can **execute child processes asynchronously** by wrapping the child process call in a `Promise` that `resolve`s once an event (usually the `close` event) has completed. The example below could then be called inside an `async`hronous function and `await`ed.
```js
const  asyncChildProcess  = () => {
  return  new  Promise(resolve => {
    const bin = spawn('curl', ['-v', '-O', 'http://my_binary.org'])
    bin.on('close', code => {
      console.log(`Curl exited with ${code}`)
      resolve()
    })
  })
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzI1OTc3NzI1LDc3Njc0Mjg4NCwtMTkxND
QzOTQzMSwtMTE4MzkxNzI4Nl19
-->