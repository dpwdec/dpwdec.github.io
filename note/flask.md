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

Flask uses the `jinja2` templating engine.  

You can **embed `jinja` code for templating and logic** by using the `{% %}` curly brace, percent syntax indicators.
```html
{% block body %}
{%
```

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NzU0NjQ2NzAsMjMyNjE5NjMxLC0xNz
Q2Mjk5MTE1LC05Nzk5MzI3NDcsMTgzOTc2MTMxMiwtMjU3Nzkz
NDgwLDI1OTYzODIwOF19
-->