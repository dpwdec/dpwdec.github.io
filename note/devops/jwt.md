---
title: JWT
layout: page
exclude: true
---

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

### Reserved Claims


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ4NzI1MDUzOCwtNTI0MjQ1ODI2XX0=
-->