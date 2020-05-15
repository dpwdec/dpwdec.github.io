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

You can answer them truthfully or just press `return` several times until the file has been created, it doesn't really matter at this stage. After the `package.json` file has been created, add the 


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcyNDc1NDM2Nl19
-->