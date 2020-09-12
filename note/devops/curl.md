---
title: Curl
layout: page
exclude: true
---

Curl is a tool for transferring data between servers and locations.

## Fetching

You can **make a simple `GET` request** to a page using the `curl` command without any flags.
```bash
$ curl https://website.com
```

You can **display `GET` request headers** by adding the `i` flag to the request, thus showing metadata about the request as well as the returned information.
```bash
$ curl -i https://website.com
```

## Post

You can **change the HTTP verb associate with a request** by using the `X` flag followed by the verb you want to use. It's important to note that **curl automatically selects the appropriate verb for a request** so even if you change the verb manually if it doesn't fit the request type it will still just send the most appropriate rThe example below changes a standard `GET` request to a `POST` request.
```bash
$ curl -X POST https://website.com
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MzUxMDkzNzVdfQ==
-->