---
title: Functions
layout: page
exclude: true
---

## Handlers

You can **specify locations of handlers** by using the `handler` property under the function definition. This uses a relative file path to the folder where the handler file code is stored and then the name of file *without the file extension* and then any sub objects within the file.
```yaml
functions:
  myFunction:
    handler: src/index.handler
```

For example the handler above would work for lambda code stored in an `src` folder with an `index.js` file and a export of an object with a property `handler` pointing to the function in the lambda.
```js
// index.js
const f = () => {}
module.exports = {
    handler: f
}
```

## Events

You can **control how lambda functions are triggered** using the `events` list underneath a function declaration.
```yaml
functions:
  myFunction:
    handler: index.myFunction
    events:
      # events here that trigger the function
```

You can **trigger a function using an HTTP request** by adding an `http` type object to the list of `events` with the `path` and `method` specified. *Serverless will automatically create an configure an API Gateway when using an HTTP endpoint.*
```yaml
functions:
  myFunction:
    handler: index.myFunction
    events:
      - http:
        path: /
        method: get
```

### HTTP

You can **add dynamic query string attributes to a serverless request URL** by adding `{}` curly brackets into the the `path` of an `httpApi` event.
```yaml
myFunction:
handler: index.myFunction
  events:
    - http:
      path: /mypath/{id}
      method: get
```