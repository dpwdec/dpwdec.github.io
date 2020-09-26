---
title: Discord
layout: page
exclude: true
---

It is **not recommended to interact directly with the Discord API** instead there are a [host community supported wrappers for the API](https://discord.com/developers/docs/topics/community-resources#libraries) that are much more reliable. The main purpose of building a discord integration directly from the discord API would be for learning.

`Guild` is the **internal technical name used for server** in discord documentation and by developers.

## Application

**Applications that you create are linked to your discord account**. You can **create a new discord application** by going to the [Developer Dashboard](https://discord.com/developers/applications/) and clicking `New Application`.

Applications come with a `CLIENT ID` on their hompage which can used for log in and authentication purposes.

## Bots

**Bots** are used to **control actions that happen on your server**. Bots are *contained* inside individual applications.

You can **create a new bot** by going to the `Bot` tab and selecting `New Bot` in the Developer Dashboard.

Bots have a **personal login** shown at the top of the bot page. The **bot token**, displayed on the bot page is used to control the bot account so **KEEP IT PRIVATE**.

You can **add a bot to a discord server that you have admin privileges on** by using an access url with `client_id` value substituted for your application's `CLIENT ID`.
```http
https://discordapp.com/api/oauth2/authorize?scope=bot&client_id=XXX
```






<!--stackedit_data:
eyJoaXN0b3J5IjpbNTczMTA2NTMsLTgyNTQ5NjA4OSwyMDkxOD
kzNjU0LC0yMDQ0NDE5NDk1XX0=
-->