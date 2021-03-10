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

Yo

 and returns an object that logs events when that command executes.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ1Nzk3NzAxNF19
-->