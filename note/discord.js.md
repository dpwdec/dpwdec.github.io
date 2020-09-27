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

### Events

The client object **comes with many event triggers** that allow it to react to different actions. Events to react to are indicated by an argument to an event handling method on `client` followed by a lambda describing the action to be taken.

You can **react to an event ONCE** by using the `once` method. The `ready` event is **emitted when the client successfully logs in**.
```js
client.once('event', () => {
  // action
});
```

You can **do something when the client successfully logs in** by using the `ready`

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA4NTE1NTcwOCwtMTM2MDcxMTIxOF19
-->