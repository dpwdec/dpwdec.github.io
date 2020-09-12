---
title: Curl
layout: page
exclude: true
---

Curl is a tool for transferring data between servers and locations.

You can **separate requests over multiple lines** by escaping them with a `\` backslash.
```bash
$ curl -i -X POST 
```

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

You can **send data with a request** by using the `data` flag followed by data you want to send as a key value pair in `''` quotes followed by the url you want to send the data to.
```bash
$ curl --data 'name=Lomothy' https://website.com/post
```

You can also **specify the url you want to send data to explicitly** with the `url` flag.
```bash
$ curl --url https://website.com/post --data 'name=Lomothy'
```

You can **change the HTTP verb associate with a request** by using the `X` flag followed by the verb you want to use. It's important to note that **curl automatically selects the appropriate verb for a request** so even if you change the verb manually if it doesn't fit the request type it will still just send the most appropriate request. The example below changes a standard `GET` request to a `POST` request (but given the caveat above, under the hood, this is still just a standard `GET` request).
```bash
$ curl -X POST https://website.com
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MjI0NjIzNzVdfQ==
-->