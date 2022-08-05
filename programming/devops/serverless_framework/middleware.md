---
title: Middleware
layout: page
exclude: true
---

## Middy

You can use the `middy` package to **add middleware processing to your lambda functions**.

You can **install middy** with
```bash
npm install @middy/core
```

The core package provides the framework whereby other middy middlewares with actual functionality are run.

You can **install other packages offer by middy** using the `@middy` namespace with the specific package afterwards.
```bash
npm install @middy/<PACKAGE_NAME>
```

You can then **use the middleware** by wrapping a function export in the `middy` function from `core` and then `use`ing another installed function. In the example below the `@middy/http-json-body-parser` has been installed and is used to process the body of requests into JSON therefore obviating the need for JSON parsing in the function itself.
```js
const middy = require('@middy/core');
const httpJsonBodyParser = require('@middy/http-json-body-parser');

const someFunction = async event => {
    const { rawJson } = event.body; // body can be destructured without JSON.parse
}

module.exports - {
    // middy middleware handler is configured here
    handler: middy(someFunction).use(httpJsonBodyParser())
}
```