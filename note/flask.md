---
title: Flask
layout: page
exclude: true
---

You can **initialize a new flask application** by using the `Flask` function with the name of the app. It is idiomatic to use the `__name__` property for app object naming.
```py
from flask import Flask 

app = Flask(__name__)
```

You can **run your flask application** with the `.run` method.
```py
app.run()
```

You can **run the application in debug mode** so that it displays errors on the output webpages by setting the `debug` flag to `True` as an argument to `run`
```py
app.run(debug=True)
```

## Routes

You can **define an application route** by using the `app.route` method as a decorator for your controller functions. The argument to the `route` method is the url extension that will route to that controller function.
```py
@app.route("/")
def index():
  return "Hello, world!"
```

## Blueprints



## JSON

You can **send JSON responses** by using the `jsonify` method. This accepts JSON formatted data (or a Python `dict`) as its argument between `{}` curly braces. Keys and values must be in string format.
```py
jsonify(
  {
    "codec": "73-ZXX14", # key value pairs
    "users": [ # arrays
      "Nelson",
      "Lauren",
      "Vlad"
    ],
    "scheme": { # nested objects
      "platform": "spectrum",
      "version": "1.1.2"
    }
  }
)
```

## Templating

You can **render and return a page template** by importing the `render_template` function from flask and returning it in your flask route with the path to the template you want to render as the argument. The `render_template` function will look for a directory called `templates` in the directory that the app is being run from to find a file path to the file you want to render.
```py
from flask import render_template

# --snip--

@app.get("/")
def index():
  return render_template("index.html")
```

### Jinja

Flask uses the `jinja2` templating engine.  

You can **embed `jinja` code for templating and logic** by using the `{% %}` curly brace, percent syntax indicators.
```html
{% block body %}
	<!-- code here -->
{% endblock %}
```

You can **interpolate code results as a string** using `{{ }}` double curly braces.
```html
<link rel="stylesheet" href="{{ # python code here }}">
```

### Templates

The `jinja2` engine works by inheriting from other templates by name and then use named `block`s to insert content. For example a very simple template might look like the `base.html` file below which defines a `block` called `body`.
```html
<!-- base.html -->
<html  lang="en">
  <head>
    <meta  charset="UTF-8">
    <meta  name="viewport"  content="width=device-width, initial-scale=1.0">
    </head>
  <body>
    {% block body %}{% endblock %}
  </body>
</html>
```

To **inherit from a template** use the `extends` keyword followed by the name of the template as a string.
```html
<!-- index.html -->
{% extends 'base.html' %}
```

You can **insert content for a templated block** by inserting regular HTML content between the `block` and `endblock` tags. This will then inject that content into the template when it is returned by flask.
```html
<!-- index.html -->
{% block body %}
  <h1>Hello, world!</h1>
{% endblock %}
```

### CSS and JS

You can **import static content** such as CSS and Javascript by setting their `href` and `src` respectively interpolating a file path using Jinja's `{{ }}` interpolation code and Flask's `url_for` method which takes the name of the `static` directory as its first argument and then a file path to the static file within that folder. The example below loads `main.css` from the `static/css/` directory and `index.js` from the `static/js` folder and inserts the correct file paths thus loading the resources.
```html
<link  rel="stylesheet"  href="{{ url_for('static', filename='css/main.css') }}">
<script  src="{{ url_for('static', filename='js/index.js') }}"></script>
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5OTI4OTA4NDYsLTE3ODUxODczMzEsLT
E1NTEyMzk2MzEsMjMyNjE5NjMxLC0xNzQ2Mjk5MTE1LC05Nzk5
MzI3NDcsMTgzOTc2MTMxMiwtMjU3NzkzNDgwLDI1OTYzODIwOF
19
-->