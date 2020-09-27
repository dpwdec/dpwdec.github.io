---
title: Discord.js
layout: page
exclude: true
---

`Discord.js` is a feature rich library for interacting with the discord API. It's generally thought to be less performative than other javascript discord integrations.

You can **install `Discord.js`** with `npm`.
```bash
$ npm install discord.js
```

You can **start using the `Discord.js` library** by `require`ing it.
```js
const Discord = require('discord.js');
```

## Client

The client object **represents your actor on the guild (server)** and is the main way you can control its actions.

You can **create a new client** using the `Discord.Client()` method.
```js
const client = new Discord.Client();
```

You can **connect your client to the server** and bring it online, by using the `client`'s `login` method with your `bot token` as an argument.
```js
client.login('<bot token>');
```

### On

The client 


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY3MDQwOTk5NCwtMTM2MDcxMTIxOF19
-->