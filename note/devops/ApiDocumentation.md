---
title: API Documentation
layout: page
exclude: true
---

Swagger is a service that allows you to generate API documentation programmatically from `YAML` or `JSON`.

## Parameters

You can **define a list of parameters** by using the `paramters` tag and listing each parameter with a `-` hyphen before it.
```yaml
parameters:
  -
```

## ReDoc

ReDoc is a service built on top of Swagger that allows you to turn Swagger specs easily into HTML.

You can **generate a zero dependency HTML file for your spec** by using the `redoc-cli` command with the `bundle` utility.
```bash
$ npx redoc-cli bundle <spec file>
``` 


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1NTA1MzY1NSwtODM4MTUwMTYzLDIzMj
gzMTA2NV19
-->