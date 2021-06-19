---
title: JWT
layout: page
exclude: true
---

## Anatomy of a JWT

Below is an example. JWT formatted so show the different parts of a valid JWT. Usually these will just be displayed as a single long string.
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

The JWT contains a `Header`, `Payload` (with associated user information, also sometimes called the `Claims` portion) and `Signature`.
```
(Header)
.
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
.
(Signature)
```

The `Claims` section of the JWT can be decoded by your application to extract authentication information.

The `Signature` is used to **confirm that the contents of the JWT has not been altered in flight**. By checking the `Signature` against the OAUTH client's private key.

## Claims

A JWT claim is **a piece of information contained in the token that is asserted about its subject** in JSON format. For example, this might be the `name` of the user or some other information about them.
```json
{
  "name": "Treyane Fitzput"
  "admin": true
}
```

There are two types of claims:

1. **Reserved** claims that are part of the JWT standard.
2. **Custom** claims that can be defined by you


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MjE3OTU3MjMsLTExMjAyODIzNjRdfQ
==
-->