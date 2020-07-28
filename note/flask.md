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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI1Nzc5MzQ4MCwyNTk2MzgyMDhdfQ==
-->