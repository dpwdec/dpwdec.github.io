---  
layout:  post 
title:  "Uploading images using express and mongodb" 
---

This post will guide you through how to set up your express website to upload images through an upload form and store then in a mongoDB database. This solution uses a very simple express controller with most of the code bundled into the `app.js` file, but this can easily be extracted out into separate controllers and routers. Furthermore, this solution does not allow you store larger images due to mongodb's upload size limit of 16mb, to accomplish this you might need to use a more complex system like `gridfs`, however, the primary purpose of this post is as an introduction to the basics of image uploads and storage to a mongoDB database.

## Overview
There are several dependencies we will need to successfully upload images, these are:

- `express` => a node web framework to serve our website and process uploads / interface with the database
- `handlebars` => a templating language for serving custom static HTML with server data
- `mongoDB` => a noSQL database for storing image data
- `mongoose` => an ORM that wraps the creation of mongoDB schema and requests to the database in an easy to use API
- `multer` => an express middleware that allows us to upload image data to our sever
- `fs` => a node file streaming utility for converting our images to string of binary byte data for storage

The basics flow of uploading an image to our mongoDB database using express has a few steps:

1. Create an upload form that posts to a route on our server with the image file data.
2. Use the `multer` express middleware to *temporarily* store the uploaded image on our server in an `uploads` folder.
3. Read the uploaded image data from the `uploads` folder using the node `fs` library as a string of binary byte data (image data string).
4. Store the image data string that was read in by `fs` inside a `buffer` type property of a `mongoose` `image` model.
5. Save the `image` model to the database.

The basic flow of retrieving the image from our database is slightly simpler:

1. Make a request for the image data with a query string identifying the image you want from the server.
2. Retrieve the `image` database record based on the query in the request.
3. Convert the `buffer` property that contains the image data string into a `base64` string.
4. Send the string to the client's web page and render it on the page using the `src` component of an `<img>` HTML element.

## Basic app set up

First, let's create the basic express app that will act as the server for our image upload system. Create a new folder for your project and run `npm init` to set up the project's `package.json` file. Set the `entry point` to `app.js` during set up.

Create a new `app.js` file to act as your projects main file.

Set up a basic express `get` route in your `app.js` file by `require`ing `express`, creating a new `app` and listening on port `3000` and check that if you load `http://localhost/300` you see a string with the message inside `send`.
```js
// app.js
// basic app code
const  express  =  require('express');
const  app  =  express();
const  port  =  3000;

app.get('/', (req, res) => res.send('This is an image upload app!'));
app.listen(port);
```

## Upload Form

Next, we need to install `handlebars` into our project using `npm install express-handlebars` then `require` the `handlebars` module inside our `app.js` file.
```bash
$ npm install express-handlebars
```

Create a new express render engine for handlebars using the `app.engine` command. Here we call the engine `.hbs` and then submit an object to the `exphbs` function with configuration parameters, in this case setting the extension name to `.hbs`. 

Set the `'view engine'` as the engine that was just created, this allows express to use the `render` command with the `handlebars` code to display these templating source files (`.hbs`) correctly.

```js
// app.js (example truncated to show only additions)
const exphbs = require('express-handlebars');

//add the express-handlebars view engine to express
app.engine('.hbs', exphbs({extname: '.hbs'}));
// set the view engine for your app
app.set('view engine', 'handlebars');
```

Create a `views` folder inside your project's root directory add an `index.hbs` file inside the `views` directory. Express matches the `render` command against this directory pattern so that when you call the `render` method it searches for the files to render relative to the `views` folder.

Add another folder inside `views` called `layouts` with a `main.hbs` file inside.
```
.
├── app.js
└── views
    ├── index.hbs
    └── layouts
        └── main.hbs
```

Inside `main.hbs` add a single line that says `{{{render}}}`. This is where express will insert content from `index.hbs` when it loads your web pages.
```html
<!-- main.hbs -->
{{{render}}}
```

Create a basic HTML upload form inside `index.hbs`.  The form's submission `method` is set to `POST` because we are "posting" data to the server to be added to our database when it is submitted. The `enctype` is also set to `multipart/form-data` so that file encoding is correct when it arrives at our server.
```html
<form  action="/"  method="POST"  enctype="multipart/form-data">
  <input  type="file"  id="img-upload-input">
  <input  type="submit"  value="upload">
</form>
```

After this your `app.js` file should look something like the example below and you should be able to start your server and load up the page with your submission form.
```js
//app.js
const  express  =  require('express');
const  app  =  express();
const  port  =  3000;

const  exphbs  =  require('express-handlebars');
app.engine('.hbs', exphbs({extname:  '.hbs'}));
app.set('view engine', '.hbs');

app.get('/', (req, res) => res.render('index.hbs'));

app.listen(port);
```

## Uploading the image to temp folder

Next, we'll use the `multer` middleware to convert the data from the form into a file on our server, we'll use a temporary folder called `uploads`.

Create the `uploads` folder in your project's root directory. It's worth also adding the contents of this folder to `.gitignore` file and also creating a `.gitkeep` file inside it and adding this as an exception to the `.gitignore` command. The result of this is that the uploads folder will be added to git if you commit the project but the contents of the folder (i.e. the temporarily uploaded images) will NOT be commited.
```git
# .gitignore
uploads/*
!uploads/.gitkeep
```

Install `multer` with the `npm install multer` command. Then `require('multer')` inside your `app.js` file. Next, use the result of the `require` to create an `upload` object (this is what will be used as the middleware inserted into our express route to grab the file data and upload it to the server). Submit an object as an argument to this function with `dest: './uploads'` which essentially tells multer where to save the data it gets from the form.
```js
// app.js - only multer additions
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMDA2MzU2NiwxNzQzNzIzNTc1LC0yMD
c2MTM1OTU4LDM4NzkwMjY5MCw1MDU2NTUxNjYsLTE4NzcyMTI5
MzQsLTE1MDE1MDYzNzUsMjM4Mjc3NTkyLC05NTg3NDUxMDUsMT
c3NzIxNDg5NSwxNTIxMzM4ODU1LDE1NjcxMjM3OTMsLTE3ODgx
MDgwNDNdfQ==
-->