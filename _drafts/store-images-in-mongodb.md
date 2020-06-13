---  
layout:  post 
title:  "Uploading images using express and mongodb" 
---

This post will guide you through how to set up your express website to upload images through an upload form and store then in a mongoDB database. This solution uses a very simple express controller with most of the code bundled into the `app.js` file, but this can easily be extracted out into separate controllers and routers. Furthermore, this solution does not allow you store larger images due to mongodb's upload size limit of 16mb, to accomplish this you might need to use a more complex system like `gridfs`, however, the primary purpose of this post is as an introduction to the basics of image uploads and storage to a mongoDB database.

## Overview
There are several dependencies we will need to successfully upload images, these are:

- `express` => a node web framework to serve our website and process uploads / interface with the database
- `handlebars` => a 
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

Create a new folder for your project and run `npm init` to set up the project's `package.json` file. Set the `entry point` to `app.js` during set up.

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







<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NzIzOTQ4NzAsLTk1ODc0NTEwNSwxNz
c3MjE0ODk1LDE1MjEzMzg4NTUsMTU2NzEyMzc5MywtMTc4ODEw
ODA0M119
-->