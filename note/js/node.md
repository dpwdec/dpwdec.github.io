---
title: Node
layout: page
exclude: true
---

## REPL

You can start the `node` REPL by using the node command in the terminal.
```
$ node
```

## npm

To **create a new `package.json` file** use `init` command.
```
$ npm init
```

You can **install dependencies** specified in `package.json` by using the `install` command.
```
$ npm install some-package-name
```

You can **install multiple dependencies with a single install command** by separating each dependency name with a space.
```
$ npm install some-package-name another-package and-another-one
```

You can **abbreviate the `install` command** to `i`. You can use this in place of `install` on any command.
```
$ npm i some-package-name
```

To **install a dependency as a development dependency only** use the `--save-dev` flag.
```
$ npm install --save-dev some-dev-dependency-name
```

### Package

The `package.json` file contains a range of dependencies and descriptors for your project.

You can **add a list of development dependencies** using the `devDependencies` key.
```js
{
  "devDependencies": {
    "some-dependency": "*",
  }
}
```

### Link

You can **link a project's dependencies to a locally developed resource** by using the `npm link` command. This utility is useful if you are working on a project that has a dependency on a resource that you also develop and are modifying, by `link`ing your project's dependency to the locally developed version you can update the dependency and see those changes reflected immediately in your project.

You can **activate `npm link`** by navigating to the source folder for your package that acts as a dependency and executing the `npm link` command to create a global link to that package, then navigating to the project that uses that dependency and calling `npm link <DEPENDENCY FOLDER NAME>` to set up a link. In the example below, linked folders are indicated with a `~`.
```
projects
├── my-app
|   └── node_modules
|       └── my_dependency_project ~
└── my_dependency_project ~
```

For the file structure above you would run the following commands.
```bash
$ cd projects/my_dependency_project
$ npm link # set up global symlink
$ cd ../my-app
$ npm link my_dependency_project
```



## fs

You can **delete a file from a directory** using the `unlink` method (an asynchronous deletion method) or the `unlinkSync` method (the synchronous version of the same functionality), simply pass the file of the path you want to delete as an argument. The **async version also takes a callback** that runs when the deletion finishes.
```js
var path = './path/to/file.txt'
fs.unlinkSync(path); // delete file synchronously

fs.unlink(path, (err) => { // delete file asynchronously
  // do something when file is deleted
});
```

## Process

You can **make your node application exit** by using the `.exit` method on the process object.
```js
process.exit();
```

## Frameworks

#### Handlebars
[Handlebars][hb] is an extension for Express that allows you to pass content dynamically from your server to your web pages and set up web pages which injected reproducible code into multiple web pages.. The directory for Handlebars to work should be structured like so:
```
.
├── app.js
└── views
    ├── home.handlebars
    └── layouts
        └── main.handlebars
```
Where `views/layouts/main.handlebars` represents code that will appear on each page, and `layouts/main.handlebars` represents a page in our website. To insert the content from a page into a handlebars layout use the `{{{body}}}` indicator. In the below example the content from a specific page will be inserted where into a `<div>` with `class="my div"` for every page on our website.
```html
<div class="my div">
  {{{body}}}
</div>
```
To **create a route to your `main.handlebars` page** use express's routing function, which has `'/'` representing the root url.
```javascript
app.get('/', function (req, res) {
  res.render('home')
});
```
You can **variables to your web pages from your server** using the `app.get()` function and adding input variable dictionaries as an argument to the `render()` function.
```javascript
app.get('/', function (req, res) {
  res.render('home', {
    stuff: "Stuff variable"
  });
});
```
This can then be referenced from your `HTML` page using `{{ }}` braces which will inject that variables content into these html tags.
```html
<p>{{ stuff }}</p>
```
You can **pass in variables** to this dictionary as well to render logical parts of your code.
```javascript
const other_stuff = "Other stuff variable";
// pass the variable in
app.get('/', function (req, res) {
  res.render('home', {
    stuff: other_stuff
  });
});
```

[hb]: https://github.com/ericf/express-handlebars

### Nodemon
By default you must restart you node server every time you make a change to your serve code so that it can run. [Nodemon][nm] is an automated service that **monitors your node server** and **restarts it automatically when server code changes are made**. 

You can **install Nodemon** using `npm install -D nodemon`. The `-D` indicates that this install is for development purposes only and shouldn't be included with a release version of our node app.

You can **trigger nodemon server running** by adding a new script the `package.json` file that runs nodemon on whatever your root file is.
```
"scripts": {
  "dev": "nodemon SERVER_FILE_NAME"
}
```
You can then **trigger this nodemon script** with the command `npm run dev`. You can also give this script whatever name you want, like `tomato`.

[nm]: https://www.npmjs.com/package/nodemon

## Karma

The Karma framework allows you to run browser based javascript tests, like Jasmine, from the command line.

You can **specify the type of reporting you get** by changes the `reporters` section of the `karma.conf.js` file. You will often need to add and `npm install` these reporters as dependencies as well.
```
reporters: ['progress', 'spec', 'super-dots']
```

## Browserify
[Browserify](http://browserify.org/) allows you to bundle code written in `node` with many dependencies into a single `bundle.js` file that will run in the browser. After having written your node code, with standard requires and classes etc. Create a top level script (such as `main.js`) that calls the dependencies you have created to do something. This is the file you should target with Browserify which will take this file, scope out all its dependencies, and return a single `bundle.js` file that will run all the code. To install Browserify use:
```
$ npm install uniq
```

To then bundle your javascript into a single file use:
```
$ browserify main.js -o bundle.js
```

After this, all you need to do is require the `bundle.js` on a page as a script.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc2MDU2NDMxOSwtMTAxMDk1MTc3XX0=
-->