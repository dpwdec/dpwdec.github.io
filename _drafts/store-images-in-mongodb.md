---  
layout:  post 
title:  "Uploading images using express and mongodb" 
---

This post will guide you through how to set up your express website to upload images through an upload form and store then in a mongodb database. This solution uses a very simple express controller with most of the code bundled into the `app.js` file, but this can easily be extracted out into separate controllers and routers. Furthermore, this solution does not allow you store larger images due to mongodb's upload size limit of 16mb, to accomplish this you might need to use a more complex system like `gridfs`, however, the primary purpose of this post is to introduce

## Overview
There are a few steps that we will have to take to
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MTI3ODcxOTldfQ==
-->