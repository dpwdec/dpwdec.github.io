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

## Controllers
Server controller code executes upon express receiving a client request and is routed through functions that have a `req` and `res` arguments. Information about the client request is found in the `req` argument and information an object representing the skeleton response to be sent back to the client is represented by the `res` object. The code below shows an example of a basic `app` route that uses the `req` / `res` function and a controller with an associated route. However, examples here will use the `app.js` syntax for brevity.
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

You can **send back a static page as response to the client** using `res` argument with the `render` method. This method searches the from the `views` directory. In the example below the `index` file that is getting rendered will be inside the `views/home/` folder.
```js
app.get('/', function(req, res) {
  res.render('home/index')'
});
```

You can **send data along with static content** by including the data in a javascript object as a second argument in the `render` function. In the example below the `appTitle` variable will be available to be embedded and used in the page that is served to the client. This allows you to send server based parameters to the client to be rendered on the page. This is similar to assigning instance variables in a route method in an framework like `sinatra`.
```js
app.get('/', function(req, res) {
  res.render('home/index'), {appTitle: 'My App'}'
});
```

You can **send server data directly** (such as JSON) without any associated rendering by using the `send` method. The client request to the `/info` controller below will return a stream of JSON data that can be used on the client side.
```js
app.get('/info', function(req, res) {
  var someJSON = {name: 'dec', age: 28};
  res.send(someJSON);
});
```

You can **retrieve parameters sent by the client** (such as by a `POST` request) by using the `body` component of the `req` argument.
```js
app.post('/save-name', function(req, res) {
  var userName = req.body.name; // retrieve username from the response body
  // do other stuff with name data
});
```

### Redirecting
You can **redirect from one url to another** using the `redirect` method of the `res` controller argument. The code below receives a `post` request and then routes the response to a new url as a `get` request to satisfy the *post-redirect-get* pattern of controller routing.
```js
app.post('/some-post-url', function(req, res) {
  // post information
  res.redirect('/url-success');
});
```

### Status Responses
You can **send a custom HTTP response** using the `status` method on `res` and then appending the return method of your choice. In the example below the `render` method is appended by the `status` method which simply updates the associated response status code for that resource. You are not constrained by express in the status codes you send, you can send a completely incorrect status code if you wish.
```js
app.get('/', function(req, res) {
  res.status(302).render('home/changed');
});
```

### Queries
You can **retrieve a `GET` request query** inside a controller using the `.query` property of `req` and then access the query's property that you want to use by name to retrieve the value.
```js
//route in response to a query:
//[http://mywebsite.com/query?name=foo

app.get('/query', function(req, res) {
  var name = req.query.name; // => foo
});
```

### Testing
You can **test and dependency inject express controller methods** by passing a **higher order function** to the express `router` that returns the controller method in the `(req, res)` format.


## Views
Express views are mediated through `view engine` that is set in the project's main file. 

You can **create a new express view engine** using the `.engine` method. This method takes an engine name and a set up method, usually from some external templating language. The example below uses handlebars.
```js
var handlebars = require('express-handlebars');
app.engine('.hbs', handlebars({extename: '.hbs'}));
```

You can **set the created engine as the app's dedicated view engine** using the `.set` method and specifying the `'view engine'` as the result of `app.engine`.
```js
app.set('view engine', '.hbs');
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA4ODMzMzU4OV19
-->