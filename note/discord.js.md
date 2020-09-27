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

You can **react to an event ONCE** by using the `once` method.
```js
client.once('event', () => {
  // do something
});
```

You can **react to an event MULTIPLE TIMES** by using the `on` method.
```js
client.on('event', () => {
  // do something
});
```

You can **do something when the client successfully logs in** by using the `ready` event.
```js
client.once('ready', () => {
  // do something
});
```

You can **do something when a message is emitted** using the `'message'` event. This supplies a `message` object as an argument to the event lambda.
```js
client.on('message', message => {
  console.log(message.content);
});
```

## Message

You can **get the channel that a message was sent in** by using the `channel` property of `message`.

## Channel

You can **get a unique string name for your channel** by using the `toString` method on the `channel` object. This isn't particularly useful though as its just a string in the format `<#123456789012345678>`
```js
channel.toString(); // => <#123456789012345678>
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ1MTM2NTU2MiwxNzY5OTQ2MDE1LC0xOT
UwNzMyMzQ2LC0xMzYwNzExMjE4XX0=
-->