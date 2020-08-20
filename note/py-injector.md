---
title: Injector
layout: page
exclude: true
---

Injector is a Python IOC for Pythonic class dependency injection. It allows you to define dependencies on classes as constructor arguments and then use the `Injector` class to create the object without having to reference all the dependency arguments directly. To **install injector** use the `injector` handle with `pip`.
```bash
$ pip3 install injector
```

To **define a dependency injected constructor** use the `@inject` decorator on a class constructor. The **dependencies must also be typed** with hints so `Injector` knows which classes to inject. In the example below the `Container` class' constructor is marked with the `@inject` decorator and then the type hinter `Dependency` class is indicated as its dependency.
```py
# class_examples.py
from injector import inject

class Dependency:
  __init__(self):
    self.data = 6744

class Container:
  @inject
  __init__(self, dependency: Dependency):
    self.dependency = dependency
```

You can **instantiate a dependency injected class** by creating a new instance of `Injector` and using the `get` method with the class you want to instantiate as its argument.
```py
from injector import Injector

# make a new injector instance
injector = Injector()
container = injector.get(Container)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MTM4MjIyNzcsMTc4MjkyMzU4N119
-->