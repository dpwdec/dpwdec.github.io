

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
[Handlebars][hb] allows you to set up web pages with injected reproducible code and a views format. The directory for Handlebars to work should be structured like so:

```
.
├── app.js
└── views
    ├── home.handlebars
    └── layouts
        └── main.handlebars
```
Where `views/layouts/main.handlebars` represents code that will appear on each page, and `layouts/main.handlebars` represents a page in our website. To insert the content from a page into a handlebars layout use the `{{{body}}}` indicator.
```html

//
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
eyJoaXN0b3J5IjpbMTk1MDY4MjYyMywxMzgyODcyMTY1LC03MD
UwMzgzNTYsLTE1NDY0MzI2NzEsLTE1Mzg1NTg5MF19
-->