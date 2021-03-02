---
title: JWT
layout: page
exclude: true
---

## Anatomy of a JWT

Below is an example. JWT formatted so show the differ
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

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
eyJoaXN0b3J5IjpbLTExMjAyODIzNjRdfQ==
-->