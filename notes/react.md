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

Components make up the core of React. Each component represents an element a logical element on the screen that will be rendered. **Components should be placed in a `/components` directory** that is on the same directory level as your `App` file. **Components should be named with pascal case** in the format `PascalCase`. Below is an example directory structure for how components should be laid out by convention.
```
project
├── components
|	├── SomeText.js
|   └── SomeButton.js
└── App.js
``` 

## JSX

JSX is a syntax extension in React that allows you write `HTML`-like code in the React `return` method and compile the result as `DOM` displayed to the client.

You **cannot use the `HTML` `class` attribute in JSX** and instead have to use a custom `className` attribute to assign classes to `HTML` elements.
```js
return(
  <div className="MyClass"></div>
);
```

## Create React App

Create React App is a light weight micro-framework for initialising a simple react app. CRA offers a minimal server side interface that transpiles react code into pages for clients.

You can **create a new react app** in an existing folder, **without installing it as a dependency** using the `npx` command. The `.` period at the end of the `create-react-app` command indicates that you want to create the app *in* the current directory so make sure you navigate to that directory in your `CLI` first.
```bash
$ npx create-react-app .
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI3MDA1NTcyMSwtOTUyNTk1MjQxLDgwNz
IzMzk0MCwzODg1NjE3MDUsLTUzNjAwNTU4XX0=
-->