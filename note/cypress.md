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

If you want to **execute server side configuration requests** during your Cypress tests you should use the `cy.task` method. This method takes the name of a task defined in the `plugins/index.js` of your `Cypress` directory and runs it. In the `index.js` below we use the `on` callback to define a method that will executed when `task` is called with the name of the function in `task` passed to it. Cypress tasks **must explicitly return a value, nothing or a promise** to indicate to the main test calling them that the task has finished executing, this is why the tasks below return null after they have printed to the console.
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

You can **define multiple possible tasks that could be called by name** in the `plugins/index.js` file by comma separating them within the second argument object to the `on` method.
```js
module.exports = function(on) {
  on('task', {
    myTask() {
      console.log('This task was executed');
      return null;
    },
    anotherTask() {
      console.log('This is another task');
      return null;
    }
  });
}
```

You can **pass argument values from your cypress tests to tasks** by adding a second argument after the task name specification and an input argument to the task definition in `plugins/index.js`.
```js
// cypress/plugins/index.js
module.exports = function(on) {
  on('task', {
    myTaskWithArgument(arg) {
      console.log(arg);
      return null;
    }
  });
}
```

The corresponding test can then pass in an argument value. This input argument can take many different argument forms, such as a callback, object or other class parameter to be used by your Cypress tasks.
```js
// call_task_with_argument_spec.js
describe('Task Example', function() {
  it('Calls a task', function() {
    cy.task('myTask', 'an argument message');
  });
});
// => 'an argument message'
```

**Asynchronous cypress tasks should return a `Promise` that resolves when the asynchronous behaviour has completed.** This can then be combined with the `then` keyword inside your cypress test to execute the rest of the test once the asynchronous task has completed.
```js
// cypress/plugins/index.js
module.exports = function(on) {
  on('task', {
    myAsyncTask() {
      return new Promise(function(resolve) {
        mongoose.connect('mongodb://localhost/mydatabase_test', function(err) {
          // do some database stuff
          resolve('done');
        });
      });
    }
  });
}
```

In the corresponding cypress test file where the `task` is called we use `then` to execute once a database connection is achieved.
```js
// call_task_with_async_spec.js
describe('Task Example', function() {
  it('Calls a task', function() {
    cy.task('myAsyncTask').then(function(result) {
      // do some more tests here now the async task has finished.
    });
  });
});
```

It's important to note that **promises returned by `cy.task` MUST have a return value on their `resolve`**. You **cannot return an empty promise** back to the cypress test calling the task, otherwise it will give you a misleading error saying that a promise is not even being returned.

You can **combine the use of task promises with `async` and `await`** behaviour within your cypress test to streamline your test calls to async functions. In the example below, the `it` function definition is changed to `async` and `cy.task` instead of using `then` uses `await` and then executes the rest of the test code once it is finished.
```js
// call_task_with_async_await_spec.js
describe('Task Example', function() {
  it('Calls a task', async function() {
    await cy.task('myAsyncTask');
    // rest of cypress test
  });
});
```

You can **set the `timeout` limit of `task` manually when calling it** by submitting as the third argument to the `cy.task` method an object with a property `timeout` linked with the maximum wait time for a task to execute in milliseconds. The below code passes in `null` for the second argument, because there is not explicit argument for this task and sets the timeout to 20 seconds.
```js
// call_task_with_custom_timeout_spec.js
describe('Task Example', function() {
  it('Calls a task', function() {
    cy.task('myTask', null, {timeout: 20000});
  });
});
// => This task was executed.
```

### Mongoose database and Tasks
Cypress tasks **do not maintain a direct connection to the database** even if your server code uses the database Cypress does not have access to that connection, this means that if you want to execute database seeding or dropping during a Cypress test with `cy.task` you will need to establish a new database connection. The below example demonstrates importing `mongoose` and a `User` model into the `plugins/index.js` file and then connecting to a database before creating a new mongoose model instance and saving the new object to the database and then calling `resolve` on the promise to signal that the async behaviour of the function is complete.
```js
// cypress/plugins/index.js
var mongoose = require('mongoose');
var User = require('../../models/user');

module.exports = function(on) {
  on('task', {
    myAsyncTask() {
      return new Promise(function(resolve) {
        mongoose.connect('mongodb://localhost/mydatabase_test', function(err) {
          var newUser = new User({name: 'dec'});
          newUser.save(function(err) {
            resolve('done');
          });
        });
      });
    }
  });
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk3OTY4NjE1NiwtMjk5MDc2ODczLC0xMD
I4Nzc4Nzg3LC00MTYwMzk0NjMsMjExMDYxNzQzMiwtMzE1MzYw
MDQsODE1NzY3NTUwLDUwNTcwODM0MiwtMTU2OTM4MzgzMSwtMj
AzNjQ5OTgxOSwyMTA3MjgwNTkyXX0=
-->