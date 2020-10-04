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

You can **get references to other `Discord.js` modules** by using the `.` dot syntax on the `Discord` object.
```js
Discord.User; // => return the User class
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

## Client Events

The client object **comes with many event triggers** that allow it to react to different actions. Events to react to are indicated by an argument to an event handling method on `client` followed by a lambda describing the action to be taken.

### Event methods

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

### Ready

You can **do something when the client successfully logs in** by using the `ready` event.
```js
client.once('ready', () => {
  // do something
});
```

### Message Events

You can **do something when a message is emitted** using the `'message'` event. This supplies a `message` object as an argument to the event lambda.
```js
client.on('message', message => {
  console.log(message.content);
});
```

You can **trigger an action when a user reacts to an message** by using the `messageReactionAdd` event. The arguments to this event's lambda are a `MessageReact` object and a `User` object of the user that sent the message.
```js
client.on('messageReactionAdd', (reaction, user) => {
  console.log(`${user} reacted with ${reaction}`);
});
```

The `messageReactionAdd` event will **only work on cached messages** - bots will automatically cache messages that come in while they are online - so if someone reacts to a message sent while your bot was offline it will not trigger.

### Gotchas

It's worth noting that **discord bots have no filters about what events they will listen to** and can cause infinite loops, for example, if you listen to messages and also send messages, the messages your bot sends will be listened to by itself thus causing it to spam a channel.
```js
// BAD: INFINITE LOOP
client.on('message', message => {
  message.channel.send('hello');
});
```

## Message

You can **get the channel that a message was sent in** by using the `channel` property of `message`. This returns a `channel` object with information about the channel.



## Reactions

You can **get all the reactions that were sent on a message** using the `reactions` property which returns a `ReactionsManager` and the `cache` property that holds the cache of reactions. The `cache` is map from the reaction object (usually an emoji) *to* a `MessageReaction` object.
```js
message.reactions.cache.forEach(reaction => {
  // do something with reaction data
});
```

You can **get the associated emoji** of a reaction by using the `_emoji.name` property of each `MessageReaction` object. This is not reccommended though as `_emoji` is indicating itself to be a private field.
```js
message.reactions.cache.forEach(reaction => {
  reaction._emoji.name
});
```

You can also  **get a list of associated reactions** by getting the `keys` from the `cache` object (a javascript `Map`) which returns a `MapIterator`, which can be used to construct an `Array` that can be then iterated through.
```js
Array.from(reactions.cache.keys()).forEach(key => {
  console.log(key); // => emoji here
});
```

## Channel

You can **get a unique string name for your channel** by using the `toString` method on the `channel` object. This isn't particularly useful though as its just a string in the format `<#123456789012345678>`
```js
channel.toString(); // => <#123456789012345678>
```

You can **send a message to a text channel** using the `send` method. Text based messages are sent using the `TextBasedChannel` class.
```js
channel.send('This is my message');
```

You can **get a sent message as an object** by assigning the result of the `send` method to a variable. This is an asynchronous function so you will **need to `await`** then result of this method.
```js
async () => {
  const myMessage = await channel.send('This is my message');
}
```

You can **get a message in a channel by id** by using the `fetch` method on the `messages` property of the channel. This is an asynchronous function that returns a `Promise`.
```js
async () => {
  const message = await channel.messages.fetch(messageId);
}
```

# User

The `User` class is the **base class of all user types**.

**Bot accounts have are represented by the `ClientUser` class**, which is a sub-class of `User`.

You can **check whether a user is a bot** by using JavaScript's `instanceof` function. 
```js
if(user instanceof Discord.ClientUser) {
  console.log("This user is a bot");
}
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNjQ5OTgwMTAsLTkwOTMzODAwNiwtMT
M4NjQ0MDMyLC0xNzMwMjY0OTgwLC01NDcxMjM1MjQsLTE1Nzc5
NDY5NDAsNzc0MTQ5MjQ1LDE3MTMyMDAzMjIsOTMxNTE5NTkyLD
E3Njk5NDYwMTUsLTE5NTA3MzIzNDYsLTEzNjA3MTEyMThdfQ==

-->