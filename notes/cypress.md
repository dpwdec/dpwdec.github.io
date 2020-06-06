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

If you want to **execute server side configuration requests** during your Cypress tests you should use the `cy.task` method. This method takes the name of a task defined in the `plugins/index.js` of your `Cypress` directory and runs it. In the `index.js` below we use the `on` callback to define a method that will executed when `task` is called with the name of the function in `task` passed to it.
```js
// cypress/plugins/index.js
module.exports = function(on) {
  on('task', {
    myTask() {
      console.log('This task was executed');
      return null;
    }
  });
}
```
This is the corresponding Cypress test that calls the `myTask` function by name when it executes using the `cy.task` method.
```js
// call_task_spec.js
describe('Task Example', function() {
  it('Calls a task', function() {
    cy.task('myTask');
  });
});
// => This task was executed.
```
You can **define multiple possible tasks that could be called by name** in the `plugins/index.js` file by comma separating them.
```js
module.exports = function(on) {
  on('task', {
    myTask() {
      console.log('This task was executed');
      return null;
    }
  },);
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDczMjQ2MjE3LDUwNTcwODM0MiwtMTU2OT
M4MzgzMSwtMjAzNjQ5OTgxOSwyMTA3MjgwNTkyXX0=
-->