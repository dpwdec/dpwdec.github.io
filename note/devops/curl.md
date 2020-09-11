---
title: Curl
layout: page
exclude: true
---

Curl is a tool for transferring data between servers and locations.

## Fetching

You can **make a simple `GET` request** to a page using the `curl` command without any flags.
```bash
$ curl https://someurl.com
```

You can **display `GET` request headers** by adding the `i` flag to the request, thus showing metadata about the request as well as the returned information.
```bash
$ curl -i https://someurl.com
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkwNzkxNzA3Nl19
-->