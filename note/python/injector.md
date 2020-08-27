---
title: Injector
layout: page
exclude: true
---

Injector is a Python IOC for Pythonic class dependency injection. It allows you to define dependencies on classes as constructor arguments and then use the `Injector` class to create the object without having to reference all the dependency arguments directly. At its heart `Injector` is just a dictionary that returns an object when a type is specified.

To **install injector** use the `injector` handle with `pip`.
```bash
$ pip3 install injector
```

## Bindings

A **binding** allows you to define how "typed" dependency argument is constructed and returned to the object that uses it. This is essentially just a way of generating a dictionary with the keys as a types that you want to use the values as the instantiaton of those types. The example below shows a `user` function that has a `DatabaseConnection` as its dependency which is indic
```py
def user(db: DatabaseConnection):
  # use database connection

def configure(binder):
  binder.bind(DatabaseConnection, to=DatabaseConnection)
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

You can **instantiate a dependency injected class** by creating a new instance of `Injector` and using the `get` method with the class you want to instantiate as its argument. You **only need to import the highest level class** to the place where it is instantiated with all dependencies to be found.
```py
from injector import Injector

# make a new injector instance
injector = Injector()
# create a new container instance with dependencies automatically injected
container = injector.get(Container)
container.dependency.data # => 6744
```

You can **nest injected classes** by placing the `@inject` decorator on injected sub classes. You **still only need to create the outer class** for all nested dependencies to be found.

## Flask-Injector


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MTU4MTYxMTksMTM4ODA3MzcxMV19
-->