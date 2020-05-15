---  
layout:  post 
title:  "Setting up CLI output for Jasmine Tests" 
---

Jasmine allows you to use `SpecRunner.html` to view the results of Javascript testing. While this is a nice interface for getting set up initially it can quickly break the flow of coding to have to constantly tab out to a browser and refresh while setting up the backend sections of your application. The following method allows you to:

1. Run Jasmine tests from the command line using the `npm test` command.
2. Upload your project to a continuous integration like Travis for testing.

### Overview

We can set up Jasmine to run through the command line by using the Headless Chrome application and the package Karma. Karma automates testing and produces CLI output for your tests as well as defining how tests should be run, it is essentially a command like replacement for the `SpecRunner.html` file. Headless Chrome is simply a version of chrome that runs without an interface so that browser based tests can be run without the added resource requirements of displaying the testing interface.

### Walkthrough

**Create a new repository** and run `npm init` to create a new `package.json` file. You'll be greeted with a set of questions. 
```
$ npm init
```

You can answer them truthfully or just press `return` several times until the file has been created, it doesn't really matter at this stage. After the `package.json` file has been created, add the Karma and Jasmine dependencies to the project using the `devDependencies` property. Your `package.json` should look something like the example below. Don't worry if it differs somewhat in terms of extra lines or fields. The post important thing is that the `devDependencies` property matches what is shown below by specifying `jasmine-core`, `karma`, `karma-cli`, `karma-jasmine` and `karma-chrone-launcher` as depdencies.
```js
{
"name": "bowling-challenge",
"version": "1.0.0",
"main": "index.js",
"devDependencies": {
  "jasmine-core": "*",
  "karma": "*",
  "karma-cli": "*",
  "karma-jasmine": "*",
  "karma-chrome-launcher": "*"
  }
}
```

**Install the dependencies** using the `install` command. This should create a `node_module` directory and `package-lock.json` file in your repository.
```
$ npm install
```

You can now check that your basic tests are working *without the command line by* by setting up `SpecRunner.html` to use the Jasmine `npm` libraries. You can do this by specifying the opat them in the `src` tags of the file.
```html
<!DOCTYPE  html>
<html  lang="en">
  <head>
    <meta  charset="UTF-8"  />
    <title>Document</title>
    <link  rel="shortcut icon"  type="image/png"  href="../node_modules/jasmine-core/lib/jasmine-core/jasmine_favicon.png">
    <link  rel="stylesheet"  href="../node_modules/jasmine-core/lib/jasmine-core/jasmine.css">
    <script  src="../node_modules/jasmine-core/lib/jasmine-core/jasmine.js"></script>
    <script  src="../node_modules/jasmine-core/lib/jasmine-core/jasmine-html.js"></script>
    <script  src="../node_modules/jasmine-core/lib/jasmine-core/boot.js"></script>

    <!-- include the library you want to test here... -->
    <script  src="../src/roll.js"></script>

    <!-- include your test files here... -->
    <script  src="testFrameworkSpec.js"></script>
    <script  src="rollSpec.js"></script>
  </head>
<body>
</body>
</html>
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2MjIyMzg1OF19
-->