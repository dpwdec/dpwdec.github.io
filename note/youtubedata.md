---
layout: page
exclude: true
title: Youtube Data
---

You can **start using the youtube data api** by enabling the API in the [Google Developers](https://console.developers.google.com/) dashboard. Here you can find and copy your API key.

## Node

You can **start using the youtube data api with node** by installing `googleapis` module.
```bash
$ npm install googleapis
```

You can then **create an object which can make youtube data api requests** by using the `youtube` function of the `google` object with your api credentials.
```js
const  youtube  = google.youtube({
  version:  'v3',
  auth: '<YOUR API KEY>'
});
```

## Playlists

You can **find the `id` property of any playlist** from taking the `list` string from a link to a playlist. In the example below the `id` of this playlist is `PLMC9KNkIncKtGvr2kFRuXBVmBev6cAJ2u`.

```
https://www.youtube.com/playlist?list=PLMC9KNkIncKtGvr2kFRuXBVmBev6cAJ2u
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MDE0Mzg1NzksNTAzNTQ3MjAzXX0=
-->