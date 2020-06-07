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


<!--stackedit_data:
eyJoaXN0b3J5IjpbOTU2MjI2NzI2XX0=
-->