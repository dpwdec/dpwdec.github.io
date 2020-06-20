---
title: React
layout: page
exclude: true
---

React is a front end Javascript framework for creating dynamic web pages.

## Structure

React is a designed as a **single page web application framework**. All elements of react are mediated through a single `.html` file (usually `index.html` which contains a `<div>` with an `id` or `root`. It is into this `div` that your react app will output all of its content.
```html
<div id="root"></div>
```

The **entry point for a React app** is `index.js`. This is where you **import react dependencies** such as `React` and `ReactDOM`.

This file also **imports the application's root React component** usually called `App` and uses the `ReactDOM.render` as an initialisation point that puts the component `App` *into* the `root` `div` (above) and renders it on the page. The `App` component is the entry point for React's internal rendering and all other components in the React system can then be rendered without referencing the `DOM` or `index.js` again.
```js
// index.js
import  React  from  'react';
import  ReactDOM  from  'react-dom';
import  App  from  './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

## Components
All react 

## Create React App

Create React App is a light weight micro-framework for initialising a simple react app. CRA offers a minimal server side interface that transpiles react code into pages for clients.

You can **create a new react app** in an existing folder, **without installing it as a dependency** using the `npx` command. The `.` period at the end of the `create-react-app` command indicates that you want to create the app *in* the current directory so make sure you navigate to that directory in your `CLI` first.
```bash
$ npx create-react-app .
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE0NTUwNDgxNSw4MDcyMzM5NDAsMzg4NT
YxNzA1LC01MzYwMDU1OF19
-->