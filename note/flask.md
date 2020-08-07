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

You can **define a function to run before each server request** with `before_request`.
```py
@app.before_request
def before():
  # do some set up etc. here
```

You can **define a function to run after each server request** with `after_request`. This passes a `response` object through to the inner implementation that needs to be handled in the argument definitions for the function. You **must return the `response` in `after_request`** to avoid server errors.
```py
@app.after_request
def before(response):
  # do some tear down etc. here
  return response
```

## Blueprints

You can **split your flask application in a modular fashion** using flask's `Blueprint` module. This allows you to define routing in separate modules and then register them in your main app file.
```py
# api.py module file
from flask import Blueprint

blueprint =  Blueprint('blueprint',  __name__)

@blueprint.route('/message')
def  show():
 return  "Hello, world!"
```

To **register a blueprint in your main flask app** you must `import` the module file that contains the blue print and then use the `register_blueprint` method. Once registered if the user navigates to the url extensions defined in the blueprints they will be served via those controllers.
```py
# app.py
from flask import Flask
from api import api

app = Flask(__name__)
app.register_blueprint(api.blueprint)
```

You can **prefix all of the routes a blueprint with a master route** by using the `url_prefix` property when registering a blueprint. In the example below this now means the `message` route define in the `api` blueprint will be available at `/api/message` to users.
```py
# app.py
app.register_blueprint(api.blueprint, url_prefix="/api")
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

### Jinja

Flask uses the `jinja2` templating engine.  

You can **embed `jinja` code for templating and logic** by using the `{[%] [%]}` curly brace, percent syntax indicators.
```html
{[%]  body [%]}
	<!-- code here -->
{[%] endblock [%]}
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
    {[%] block body [%]}{[%] endblock [%]}
  </body>
</html>
```

To **inherit from a template** use the `extends` keyword followed by the name of the template as a string.
```html
<!-- index.html -->
{[%] extends 'base.html' [%]}
```

You can **insert content for a templated block** by inserting regular HTML content between the `block` and `endblock` tags. This will then inject that content into the template when it is returned by flask.
```html
<!-- index.html -->
{[%] block body [%]}
  <h1>Hello, world!</h1>
{[%] endblock [%]}
```

### CSS and JS

You can **import static content** such as CSS and Javascript by setting their `href` and `src` respectively interpolating a file path using Jinja's `{{ }}` interpolation code and Flask's `url_for` method which takes the name of the `static` directory as its first argument and then a file path to the static file within that folder. The example below loads `main.css` from the `static/css/` directory and `index.js` from the `static/js` folder and inserts the correct file paths thus loading the resources.
```html
<link  rel="stylesheet"  href="{{ url_for('static', filename='css/main.css') }}">
<script  src="{{ url_for('static', filename='js/index.js') }}"></script>
```

## SQLAlchemy and Database Sessions

One way to **control database sessions** for different controller routes is to open and close them in the `before_reuqest` and `after_request` functions then make the scope `session` object available to the route using it via the `g`lobal scope of your flask application. In the code below `app.py` sets up opening and closing `session`s before each request to the server, the individual blueprint routes can then use the `session` as required by importing the `g` variable from flask. Flask `g` isn't really global in the traditional sense, while it encompasses the application context, each new request wipes the old `g` scope and keeps it just for that request.
```py
# app.py
from database import Session # import the main Session object
from flask import Flask, g

# --snip--

@app.before_request
def before():
  g.session = Session()

@app.after_request
def after(response):
  g.session.close()

# controller.py
# some other controller blueprint with routes
from flask import g

# --snip--

@blueprint.route("/users")
def save_user():
  user = User(name="Jimothy", age=10)
  g.session.add(user)
  g.session.commit()
```

## Testing

You can **test your flask application** by creating a `pytest.fixture` that initialises the `app` in `"TESTING"` mode (this suppresses exception handling so that the test environment can more easily manage errors with meaningful messages) and then `yield` or `return` a `test_client()` to your test functions. Below is the simplest example of a test set up for a flask application. This would usually be longer with database integration etc.
```py
import pytest
from app import app # import a flask app that has been initialised in your main file

@pytest.fixture
def client():
  app.config["TESTING"] = True

  with app.test_client() as client:
    yield client # send the test client to test methods
```

You can **test a flask route** by calling the `get` method on a client route. This **also works with blueprint define routes**, you just need to include the absolute url extension to that route. You can **access and test against the `status` of a `response` object**, this comes in the form of a string. 
```py
def test_index(client):
  response = client.get("/")
  assert response.status == '200 OK'
```

You can **access the `data` of a `response`** by using the `data` property.
```py
def test_index(client):
  response = client.get("/")
  assert response.data != None
```

You can **test the string data of that `response`**, this comes in the form of byte data and so needs to be prepended by the `b` character when testing strings to indicate it is a byte string.
```py
def test_index(client):
  response = client.get("/")
  assert response.data == b'This is a message'
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNjkxMzgxODgsMTgyMzAyODUwOCwtMT
Y2Nzk5ODc5MCwyMDI3OTEyNzYzLDE1NzI4ODY4NjAsLTE5NjM0
MjU5MDEsNTcwMDE4Mzc4LC0xNjk1NTQ1MDUwLDEwMzExMjc1Ny
w2MTAyNjQzMjIsLTE0MjYzNDc3NzAsLTE3ODUxODczMzEsLTE1
NTEyMzk2MzEsMjMyNjE5NjMxLC0xNzQ2Mjk5MTE1LC05Nzk5Mz
I3NDcsMTgzOTc2MTMxMiwtMjU3NzkzNDgwLDI1OTYzODIwOF19

-->