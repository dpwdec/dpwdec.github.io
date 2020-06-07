---
title: Express
layout: page
exclude: true
---
You can **create a basic express website** using the following code:
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

## Request / Response
Server code that executes upon express receiving a client request is routed through functions that have a `req` and `res` arguments. Information about the client request is found in the `req` argument and information an object representing the skeleton response to be sent back to the client is represented by the `res` object. The code below shows an example of a basic `app` route that uses the `req` / `res` function and a controller with an associated route. However, examples here will use the `app.js` syntax for brevity.
```js
// in app.js
app.get('/', function(req, res) {

});

// in homeController.js
var homeController = {
  Index: function(req, res) {
    
  }
}
```
You can **send back a static page as response to the client** using `res` argument with the `render` method. This method searches the from the `views` directory. In the example below the `index.html` (or `index.hb
```js
app.get('/', function(req, res) {
  res.render('home/index')'
});
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc5ODQxMTM0Nl19
-->