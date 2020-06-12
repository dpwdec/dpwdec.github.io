---
title: Travis CI
layout: page
exclude: true
---
Travis is a continuous integration platform which can be used to run test builds of your application and then automatically trigger jobs such as merging or deployment based on the results of those tests.

## Scripts

### Before Script
You can use the `before_script` tag to **trigger set up events before your main scripts run**. These would typically be commands that occur before the main tests for your application are run in script but *after* installation of dependencies has taken place, such as database migrations.
```yml
before_script:
  - db:migrate
```

You can also **trigger background processes** from the `before_script` tag by appending an `&` ampersand to the end of the command. This allows you to do things like start test servers running which is useful for integration testing platforms that need to visit a local hosted version of your application. 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2MTgwNDcyOF19
-->