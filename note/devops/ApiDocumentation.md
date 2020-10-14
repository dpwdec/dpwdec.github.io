---
title: API Documentation
layout: page
exclude: true
---

Swagger is a service that allows you to generate API documentation programmatically from `YAML` or `JSON`.

## Parameters

You can **define a list of parameters** by using the `paramters` tag and listing each parameter with a `-` hyphen before it. *It doesn't seem like there are any required fields for this list of information about a parameter*.
```yaml
parameters:
  - in: query # first properties do not have to be consistent
    name: userId
    required: true
    type: integer
  - name: globalId
    required: false
    type: integer
```

## ReDoc

ReDoc is a service built on top of Swagger that allows you to turn Swagger specs easily into HTML.

You can **generate a zero dependency HTML file for your spec** by using the `redoc-cli` command with the `bundle` utility.
```bash
$ npx redoc-cli bundle <spec file>
``` 


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NTQxODQ0NDUsLTgzODE1MDE2MywyMz
I4MzEwNjVdfQ==
-->