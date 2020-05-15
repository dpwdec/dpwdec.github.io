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

## Frameworks
### Express
After installing express. You can **create a new instance of the express framework and start a server** using the following code:
```javascript
//
const app = express();

app.listen(4000, 127.160.0.1, () => console.log("Starting server));
```
You can **set up static paths** to web pages using with the `use` command.
```javascript
app.use(express.static(path.join(__dirname, 'public')));
```
Where `__dirname` is the directory from which you main `.js` file is executing and `'public'` is another directory that contains static html web pages. These commands are essentially all you need to create a basic static website.

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

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcyMTg2MjA0MCwxNzE3Njk4MjEzLDkzND
MyMjg5OSwtNTQ0MzQ2NTUzLC0xMzU4ODE2MTk4LDEzODI4NzIx
NjUsLTcwNTAzODM1NiwtMTU0NjQzMjY3MSwtMTUzODU1ODkwXX
0=
-->