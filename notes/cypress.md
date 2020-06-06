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
Because Cypress is an integration fram executes in a headless browser that does not have access to your server code.
<!--stackedit_data:
eyJoaXN0b3J5IjpbODY0NjUwMjIwLC0yMDM2NDk5ODE5LDIxMD
cyODA1OTJdfQ==
-->