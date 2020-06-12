---  
layout:  post 
title:  "Uploading images using express and mongodb" 
---

This post will guide you through how to set up your express website to upload images through an upload form and store then in a mongoDB database. This solution uses a very simple express controller with most of the code bundled into the `app.js` file, but this can easily be extracted out into separate controllers and routers. Furthermore, this solution does not allow you store larger images due to mongodb's upload size limit of 16mb, to accomplish this you might need to use a more complex system like `gridfs`, however, the primary purpose of this post is as an introduction to the basics of image uploads and storage to a mongoDB database.

## Overview
The basics flow of uploading an image to our mongoDB database using express has a few steps:

1. Create an upload form that posts to a route on our server with the image file data.
2. Use the `multer` express middleware to *temporarily* store the uploaded image on our server in an `uploads` folder.
3. Read the uploaded image data from the `uploads` folder using the node `fs` library.
4. Store the image data that was read in by `fs` inside a `mongoose` model that 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM1NzUwOTg1OF19
-->