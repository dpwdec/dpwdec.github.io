---
title: CORS
layout: page
exclude: true
---

CORS (**Cross Origin Resource Sharing**) is a security feature as part of browsers. It only effects APIs that are interacted with directly through a browser. 

Browsers use CORS to block requests to endpoints that are at a different origin from the site that is making the call unless the endpoint that is being called explicitly permits traffic by returning a response with the `Access-Control-Allow-Origin` header pointing to the calling origin. Servers describe which origins are permitted to read the information they serve using these headers.

Browsers **establish whether a real request is safe to send** by making a **preflight request** to the endpoint with an `OPTIONS` HTTP verb that tells the browser whether or not the current origin is permitted to read information from the request server. If the current origin is permitted then the real request will be sent.

The browser does this with the `OPTIONS` verb and a `Access-Control-Request-Method` property describing what sort of request it would like to make.
```
OPTIONS /doc HTTP/1.1
Access-Control-Request-Method: POST
```






<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgyMTQwOTI2NywtMTYwMDU4NTYwOCwtMT
EyNzI3ODg5Ml19
-->