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

# Components

Components make up the core of React. Each component represents an element a logical element on the screen that will be rendered. **Components should be placed in a `/components` directory** that is on the same directory level as your `App` file. **Components should be named with pascal case** in the format `PascalCase`. Below is an example directory structure for how components should be laid out by convention.
```
project
├── components
|	├── SomeText.js
|   └── SomeButton.js
└── App.js
```

You can **render a component** by calling it as a tag in the format `<ComponentName />` inside the `return` or `render` function of another components. You must also **import components that you want to render**.
```jsx
// App.js

import SomeComponent from './components/SomeComponent'

class App extends React.Component {
  render() {
    return(
      <SomeComponent />
    );
  }
}
```

All React components **must return only a single parent `HTML` element**. This means that the `return` or `render` of the component must return (usually a single `div` element) that contains all of the different content for that component. In the example below the `render` functionally shows two elements, the `h1` and `p` information, however, by wrapping this all in a single `div` this multiple elements can be return from a single component.
```jsx
render() {
  return(
    <div>
     <h1>Title</h1>
     <p>Some information.</p>
    </div>
  )
}
```

## Props

You can **pass parameters to a component**, also called `props` in React, by passing them in as a key-value pair to the tag call of the component. In the example below the name of the key is `number` and the value, contained in `{ }` curly braces is 5. You could place any property of function call here that returns a value such as using the `App` classes `state` object etc.
```js
class App extends React.Component {
  render() {
    return(
      <SomeComponent number={5}/>
    );
  }
}
```

You can **pass in multiple parameters to a component** by ` ` whitespace separating the list of `props`.
```js
class App extends React.Component {
  render() {
    return(
      <SomeComponent firstProp={5} secondProp={'hello'} thirdProp={{name: 'Foo'}}/>
    );
  }
}
```

To **retrieve `props` inside components** see the functional and class based react component specifics below.

## Prop types

React comes with **type checking functionality for components `props`** using the `PropTypes` module which comes with a set validator expressions for making sure that the values passed into a component match in type to those defined. If the type does not match a warning will be displayed in the Javascript console. This is warning is **only displayed in developer mode** for performance reasons.

To use `PropTypes`, `import` them and then create a `propTypes` property on your component that is an object which contains a list of the expected property names with the value being a `PropTypes` validator. The example below defines a `propTypes` object on the `MyComponent` class with the `name` prop set to `string`. If you your code tries to pass in a value to the name prop that *isn't* a string, then a warning will be raised.
```js
import React from 'react';
import PropTypes from 'prop-types';

class MyComponent extends React.Component {
  // does something
}

MyComponent.propTypes = {
  name: PropTypes.string
}
```

A **full list of `PropType` values** can be found [here](https://reactjs.org/docs/typechecking-with-proptypes.html#proptypes).

You can **specify that a particular prop MUST be passed into a component** by appending the `isRequired` property to the `PropType`. The `propTypes` for the component below *must* have a `name` prop that is a `string` submitted to it when it is rendered to the page, otherwise React will raise a warning.
```js
MyComponent.propTypes = {
  name: PropTypes.string.isRequired
}
```

If you want to **specify that a particular prop MUST be provided but NOT give it a type** then you can use the `any` property with the `isRequired` property appended to it. This indicates below that `name` could be *any* type but that at least some value *must* be passed in.
```js
MyComponent.propTypes = {
  name: PropTypes.any.isRequired
}
```

## Lists

You can **display an array of information as a list** by using the javascript `map` method to transform the contents of the array into `JSX` elements. The usage of the `map` function is slightly different in react with the callback function for map using `()` soft braces instead of `{ }` curly brackets to define the return type from its operation. 

The code below uses `map` and immediately after the `=>` hash rocket showing the start of the function switches to `JSX` using brackets. Then `{ }` can be used again to indicate switching back to regular javascript syntax for retrieving information from each element of the array.
```jsx
render() {
  return props.names.map((name) => (
    <h3>{name}<h3>
  ));
}
```

It is recommended that you **assign a `key` value to each item in a React component list**. This is a reserved word that is passed in as a `props` element with the key of `key`. This **should be unique** and usually matches some sort of `id` attribute for the listed data. *Why is this important?* React uses these element keys to uniquely identify elements and uses it to check which elements have changed and optimise web page updating.

This is also why it is recommended that **when displaying lists of information you should render the information as components not directly as `HTML` elements** so that you can pass in a `key` value. The example above does not do this and renders the information in `name` directly. The example below shows a more idiomatic React method of doing this by creating a `Name` component and pass in the `body` of the `name` and the `id` as `key`.

If you want to **use the value that you assign to the `key` prop inside your component** then you should pass it as again as a separate prop into the component because `key` is [not available for access from the `props` object](https://stackoverflow.com/questions/47070997/how-to-get-key-prop-from-react-element-on-change).
```jsx
render() {
  return props.names.map((name) => (
    <Name name={name.body} key={name.id}/> 
  ));
}
```

There are **two ways to define React components**. They can be defined as **functional components** which use **React hooks** or they can be defined as **class based components** which extend the `React.component` class. Both component types have similar functionality however generally if your component has a lot of **state based logic** associated with it you will want to use a class based component and if it is just a simple, possibly stateless page element that simply accepts `props` you will want to use a functional component. 

## Functional Components

A **functional React component is simply a function that `return`s some renderable React elements** to the component or object that called it. The **name of the component is the same as the name of the function that defines it** . 

You **must `import` the `React` library** to create functional react components
```js
// basic functional React component
import React from 'react';

function MyFunctionalComponent() {
  return(
    <div id="my-component"></div>
  );
}
```

You can **access `props` inside a functional component** by adding `props` as an argument to the component's function. This doesn't *have* to be called `props`, but *should* be, by React convention. The information passed in as a `props` to the object can then be retrieve from this argument. In the example below we imagine that some parent component called `MyFunctionalComponent` to render and passed in a key-value pair with `name` as the key. This key can then be retrieved from the `props` object with `.` dot object syntax.
```js
function MyFunctionalComponent(props) {
  return(
    <div id="my-component">
      <p>{props.name}</p>
    </div>
  );
}
```

## Class based Components

A **class based React component extends the `React.component` class**.

You **must `import` the `React.component` element or `import` the `React` library** and call it manually to create class based components.
```js
// basic class based React component
import React, { Component } from 'react';

class MyComponent extends Component {
  return(
    <div id="my-component"></div>
  );
}
```

The **state of a class component is stored in its `state` object**. This is a javascript object with properties that represent the data that object holds. You can **define a class component's `state` object** by defining it directly in the body of the class. In the example below `MyComponent` contains a state object that contains a high level `name` property as well as a `subComponents` property that is itself an array of javascript objects containing more data.
```js
class MyComponent extends Component {
  state = {
    name: 'My Component',
    subComponents: [
      {
        id: 1,
        data: 'Sub Component'
      }
    ]
  }
}
```

You can **access a component's `state` object** by referencing it with `this.state`. Using the example above, accessing the `name` property of the state would return the string set to this value.
```js
this.state.name
// => My Component
```

You can **store and instantiate instances of other classes inside a React components `state`** object.
```js
import SomeClass from './SomeClass.js'

class MyComponent extends Component {
  state = {
    someClass = new someClass()
  }
}
```

You can **access `props` in a class based component** by using `this.props`.
```js
class MyComponent extends Component {
  render() {
    return(
      <div id="my-component">
        <p>{this.props.name}</p>
      </div>
    );
  }
}
```

# Events

You can **get the `value` (i.e. the text portion) of an element that triggered an event** by using the `target.value` property of the `event` callback argument triggered by an element's event. In the example below any time you type something in the `text area` element it will trigger the `onChange` event and call the `myEvent` method and then `log` the contents of the element.
```jsx

myEvent(event) {
  console.log(event.target.value); // => 'Type Something'
}

render() {
  return(
    <textarea onChange={this.myEvent}>Type Something</textarea>
  )
}
```

You can **get the entire HTML element that triggered an event** by using the `event.target` component of the `event` argument. This can used for triggering elementing specific methods.
```jsx
formReset(event) {
  event.target.reset() // reset form
  event.preventDefault() // prevent form submission from relaoding page.
}

render() {
  return(
    <form onSubmit={this.formReset}>
      <input type="text" placeholder="hello"/>
      <input type="submit" value="submit"/>
    </form>
  )
}
```


# JSX

JSX is a syntax extension in React that allows you write `HTML`-like code in the React `return` method and compile the result as `DOM` displayed to the client.

You **cannot use the `HTML` `class` attribute in JSX** and instead have to use a custom `className` attribute to assign classes to `HTML` elements.
```js
return(
  <div className="MyClass"></div>
);
```

## Styling

You can **add inline styling to an element** by using the `style=` indicator and then using double `{{ }}` curly braces. Furthermore you **must use camel cased style names** instead of hyphenated names. The example below uses `backgroundColor` instead of `background-color`. You **must submit the style element's value** as a `string` after you have defined the style element's name.
```jsx
return(
  <div style={{ backgroundColor: 'ffffff' }}>
    <p>Foo</p>
  </div>
);
```

You can **extract styling into a variable** that can be inserted into the `style=` indicator of an element arbitrarily. These style variables are defined in the class body as Javascript object's with camel cased style properties linked to value.
```jsx
class MyComponent extends Component {
  render() {
    return(
      <div style={ myStyle }>
        <p>Foo</p>
      </div>
    );
  }

  const myStyle = {
    backgroundColor: 'ffffff'
  }
}
```

# React Router

You can use the `react-router-dom` library to create top level **app components like traditional web pages based on the page url**. You can **install `react-router-dom` library** using `npm`.
```bash
$ npm i react-router-dom
```

To **set up page based routing** you must first **add a `BrowserRouter` component** to your `ReactDOM.render` method to enclose the top level component of your application (`App` in the example below).
```js
import { BrowserRouter } from 'react-router-dom'

ReactDOM.render(
  <BrowserRouter>
    <App  />
  </BrowserRouter>,
  document.getElementById('root')
);
```

To **initialise a structure for pages to routed from** you must return a `Switch` component inside the `App` component's `return` which will handle individual pages.
```js
import { Switch } from 'react-router-dom'

function  App()  {
  return  (
    <Switch>
      // routes go here
    </Switch>
  );
}
```

To **set up an individual page** you must use a `Route` component which takes a `path` which corresponds to the  domain extension and a `component` that points to the react component that will be rendered on the page.
```

```

# Create React App

Create React App is a light weight micro-framework for initialising a simple react app. CRA offers a minimal server side interface that transpiles react code into pages for clients.

You can **create a new react app** in an existing folder, **without installing it as a dependency** using the `npx` command. The `.` period at the end of the `create-react-app` command indicates that you want to create the app *in* the current directory so make sure you navigate to that directory in your `CLI` first.
```bash
$ npx create-react-app .
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTk1Mzg1MTkzLC02Mzk4MzM5MzQsNDI4OT
cxMjgxLDMzNTQyMjk5OSwtMTI1MzAzMTI2MiwtMTM3MzM3OTIx
OSw0NDIyODg1ODMsODk1OTc4MDE5LC0xODQ4NTAxOTQ4LDEyOT
MwNTQ4MjYsMTkxNjczMDM5NywxNTcyNDY4ODc4LC0yMTQ0MjE4
MjA3LDEzOTE3Njc2MzgsMTAzMTQwMTExMCw0MDczNzk4MjIsMT
M0NzU1ODk3MywxNjIwMjkwMjQzLC02MTkwNDMzNzQsLTI3MDA1
NTcyMV19
-->