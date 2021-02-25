---
title: CORS
layout: page
exclude: true
---

CORS (**Cross Origin Resource Sharing**) is a security feature as part of browsers. It only effects APIs that are interacted with directly through a browser. 

Browsers use CORS to block requests to endpoints that are at a different origin from the site that is making the call unless the endpoint that is being called explicitly permits traffic by returning a response with the `Access-Control-Allow-Origin` header pointing to the calling origin. Servers describe which origins are permitted to read the information they serve using these headers.

Browsers **establish whether a real request is safe to send** by making a **preflight request** to the endpoint with an `OPTIONS` HTTP verb that tells the browser whether or not the current origin is permitted to read information from the request server. If the current origin is permitted then the real request will be sent.

An API can **allow ALL origins to access it** by setting the `Access-Control-Allow-Origin` header a `*`.
```
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: *
```

## Preflight flow

The browser does this with the `OPTIONS` verb and a `Access-Control-Request-Method` property describing what sort of request it would like to make.
```
OPTIONS /doc HTTP/1.1
Access-Control-Request-Method: POST
```

The server then responds with the supported methods, the allowed origins and the allowed headers. 
```
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://foo.example
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: X-PINGOTHER, Content-Type
```

The `Access-Control-Allow-Headers` notifies the browser what headers can be sent with the actual cross origin request.




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEzMDQxNzg5OCwtODM0MjUzMDE3LDQ2ND
M0NTU0LDgwODY5NzQyMiwtMTYwMDU4NTYwOCwtMTEyNzI3ODg5
Ml19
-->