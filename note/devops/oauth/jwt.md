---
title: JWT
layout: page
exclude: true
---

## Anatomy of a JWT



```
(Header)
.
{

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
eyJoaXN0b3J5IjpbMTk5ODI5MTM3OV19
-->