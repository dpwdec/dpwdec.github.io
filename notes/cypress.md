---
title: Cypress
layout: page
exclude: true
---
Cypress is an integration/feature testing framework for node based web servers. When Cypress tests are executed they create a headerless browser through which Cypress contacts a test server version of the web server being tested and runs integration tests created by the developer.

You can **run a single specific integration test file** by using the `run --spec` command followed by a path that points to the file which contains the Cypress integration test.
```
$ npx cypress run --spec path/to/file.spec.js
```

## Tasks
Because Cypress is an integration framework designed for testing the front end of your application it executes in a headless browser that does not have access to your server code. This means that any configuration code that you might want to use for tests, like database insertions, cannot be executed directly inside a Cypress test.

If you want to **execute server side configuration requests** during your Cypress tests you should use the `cy.task` method. This method takes the name of a task defined in the `plugins/index.js` of your `Cypress` directory and runs it.
```js
// cypress/plugins/index.js
module.exports = function(on) {
  
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA4Nzc4ODQxMiwtMTU2OTM4MzgzMSwtMj
AzNjQ5OTgxOSwyMTA3MjgwNTkyXX0=
-->