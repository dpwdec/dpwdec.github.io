---
title: OpenAPISpec
layout: page
exclude: true
---

Swagger is a service that allows you to generate API documentation programmatically from `YAML` or `JSON`.

You can **validate an API specification** with the `validate` command of the `swagger-cli` tool. This will exit with an error if validation fails.
```bash
$ npx swagger-cli validate <spec file>.yaml
```

You can **validate an API specific with a more descriptive error message** using the `swagger-repo` tool.
```bash
$ npx swagger-repo validate <spec file>.yaml
```

## Parameters

You can **define a list of parameters** by using the `paramters` tag and listing each parameter with a `-` hyphen before it. *It doesn't seem like that there are any required fields for this list of information about a parameter*.
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

## Inheritance

You can **inherit from schemas that are already defined** and extend them in new schemas by using the `allOf` property when defining a schema with the `$ref` property as a path to the schema that you are inheriting from as a named property under the `allOf` property.
```yaml
# child_schema
properties: object
allOf:
  $ref: path/to/parent/schema.yaml
extendedProperty:
  type: string
  description: This is a property being added to the child schema on top of those in the parent
```

## ReDoc

ReDoc is a service built on top of Swagger that allows you to turn Swagger specs easily into HTML.

You can **generate a zero dependency HTML file for your spec** by using the `redoc-cli` command with the `bundle` utility.
```bash
$ npx redoc-cli bundle <spec file>
``` 

You can find **a template for doing basic redoc styling** [here](https://github.com/Redocly/redoc/blob/master/src/theme.ts).


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIzOTI5ODY3NCw0NzUwNzczNTZdfQ==
-->