---  
layout:  post 
title:  "Setting up CLI output for Jasmine Tests" 
---

Jasmine allows you to use `SpecRunner.html` to view the results of Javascript testing. While this is a nice interface for getting set up initially it can quickly break the flow of coding to have to constantly tab out to a browser and refresh while setting up the backend sections of your application. The following method allows you to:

1. Run Jasmine tests from the command line using the `npm test` command.
2. Upload your project to a continuous integration like Travis for testing.

## Overview

We can set up Jasmine to run through the command line by using the Headless Chrome application and the package Karma. Karma automates testing and produces CLI output for your tests as well as defining how tests should be run, it is essentially a command line replacement for the `SpecRunner.html` file. Headless Chrome is simply a version of chrome that runs without an interface so that browser based tests can be run without the added resource requirements of displaying the testing interface. The output from these tests, when run, is then displayed by Karma in the command line.

## Walkthrough
**Create a new repository** for your project and set up git without your project.

### Install Node Modules

**Create a new repository** and run `npm init` to create a new `package.json` file. You'll be greeted with a set of questions. 
```
$ npm init
```

You can answer them all properly or just press `return` several times until the file has been created, it doesn't really matter at this stage. After the `package.json` file has been created, add the Karma and Jasmine dependencies to the project using the `devDependencies` property. Your `package.json` should look something like the example below. Don't worry if it differs somewhat in terms of extra lines or fields. The post important thing is that the `devDependencies` property matches what is shown below by specifying `jasmine-core`, `karma`, `karma-cli`, `karma-jasmine` and `karma-chrone-launcher` as dependencies.
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

### Check Testing Framework
You can now **check that your basic tests are working** *without the command line by* by setting up `SpecRunner.html` to use the Jasmine `npm` libraries. You can do this by specifying the a path to the `node_modules` directory from the `SpecRunner.html` in the `src` tags of the file.
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

    <!-- include your test files here... -->
    <script  src="mySpec.js"></script>
  </head>
<body>
</body>
</html>
```
The file paths above assume that `SpecRunner.html` is placed in a directory (usually called `spec` or `test` where your tests will also live. This is why the `src` command begins with `..` to move up and out of that directory. You'll need to alter the file path if you want to place `SpecRunner.html` somewhere else.

Now **write a basic passing test in Jasmine** and load `SpecRunner.html`, if your Jasmine library was installed correctly and you are targeting the sources with your `SpecRunner.html` your test should pass. Your basic test will be something like the example below.
```js
describe('Test', function() {
  it('passes a test' function() {
    expect(true).toBe(true);
  });
);
```

### Set up Karma
Next **set up Karma to run your Jasmine tests**. This requires you to use the `karma init` command. After the command has run you will asked a series of questions to set up Karma. The questions are pretty self explanatory and the answers should be clear. Just get it to match the `karma.conf.js` file shown below. I've commented the fields below in the `karma.conf.js` file that require answers.

The other tricky thing is setting up the `files` property correctly. This should reflect whatever file structure you are using for your project and tests. In my project all the spec files are placed in the `spec` directory and have the naming convention of ending with `Spec.js` therefore I specify that in the `files` section of the `karma.conf.js` file with `spec/*Spec.js` line. I also keep the code that is being tested in the `src` directory, so I need to add `src/*.js` to load the files that will be tested by the spec when the tests are run.
```js
module.exports = function(config) {
  config.set({
    basePath:  '',
    frameworks: ['jasmine'], // => ANSWER
    files: [
      'spec/*Spec.js',
      'src/*.js'
      ],
    exclude: [],
    preprocessors: {}, 
    reporters: ['progress'],
    port:  9876,
    colors:  true,
    logLevel:  config.LOG_INFO,
    autoWatch:  true,
    browsers: ['ChromeHeadless'], // => ANSWER 'ChromeHeadless' not just Chrome
    singleRun:  false,
    concurrency:  Infinity
  })
}
```

### Automate Test Running
Finally, to **set up the tests to run with a single command** you need to add an `npm script` to `package.json`. Add the `scripts` property below to `package.json` and create a script called `test` that runs `karma`.
```js
"scripts": {
  "test": "karma start karma.conf.js --single-run"
},
```

You should be able to **run your Jasmine tests from the command line** now by using the `test` command.
```js
npm test
```

### CI with Travis

To **integrate this approach with Travis**. Create a `.travis.yml` file, specify that you are running a `node` project and call a script that executes your `karma` tests. When you push to github with Travis enabled your tests should run successfully.
```yml
language: node_js
script: karma start karma.conf.js --single-run
node_js:
- "node"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY5MTQ3OTI2OV19
-->