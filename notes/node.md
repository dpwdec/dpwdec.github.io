
By default you must restart you node server every time you make a change to your serve code so that it can run. [Nodemon][nm] is an automated service that **monitors your node server** and **restarts it automatically when server code changes are made**. 

You can **install Nodemon** using `npm install -D nodemon`. The `-D` indicates that this install is for development purposes only and shouldn't be included with a release version of our node app.

You can **trigger nodemon server running** by adding a new script the `package.json` file.
```
"scripts": {
  "dev": "
}
```

[nm]: https://www.npmjs.com/package/nodemon

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTE4NTg4NjAxLC0xNTM4NTU4OTBdfQ==
-->