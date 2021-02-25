---
title: CORS
layout: page
exclude: true
---

CORS (**Cross Origin Resource Sharing**) is a security feature as part of browsers. It only effects APIs that are interacted with directly through a browser. 

Browsers use CORS to block requests to endpoints that are at a different origin from the site that is making the call unless the endpoint that is being called explicitly permits traffic by returning a response with the `Access-Control-Allow-Origin` header pointing to the calling origin. Servers describe which origins are permitted to read the information they serve using these headers.

Browsers establish whether a request can be made by making a preflight request to the endpoint with an `OPTIONS` HTTP verb that tells the




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAwMTYwMjgzNCwtMTEyNzI3ODg5Ml19
-->