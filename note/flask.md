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

You can **run the application in debug mode so that **
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI0MTczNzEzMCwtMjU3NzkzNDgwLDI1OT
YzODIwOF19
-->