---
title: Python
layout: page
exclude: true
---

## Importing

You can **import python code from a parallel directory** by setting up each directory as a `package` using the `__init__.py` file and then importing using the `from` and `import` keywords. Adding the `__init__.py` file makes the enclosing directory into a package structure that python can recognise with the enclosing files acting as modules that can be extended from and have their contents imported. Below is an example directory structure that would allow for package imports.
```
project
├── eggs
|	├── __init__.py
|   └── egg_classes.py
└── spam
	├── __init__.py
    └── spam_classes.py
```
 Given the directory structure above, imagine that there was a class defined in `spam_classes.py` called `Ham` that we wanted to import and use in `egg_classes.py`. To do this you would need to specify the `package` or folder that the file is in, then the `module` that class is in (this is done using `.` syntax in python) and finally the name of the class you want to import. Thus the import in `egg_classes.py` would match the example below. Note the file name of `spam_classes` is appended with `.` to the package name of `spam` and then the `import` function is used to specify exactly what class you would like.
```py
# egg_classes.py
from spam.spam_classes import Ham
```

You can also **import entire modules** by specifying them using the same pattern, however in this from we would be `import`ing `spam_classes` from `spam`. We can then get `Ham` from classes by appending a `.` dot to the namespace in our code.
```py
# egg_classes.py
from spam import spam_classes
# access Ham from the spam_classes namespace
ham_instance = spam_classes.Ham()
```

## Arithmetic Operators

You can **execute floor division**, division that removes any fractional remainder by using a `//` double forward slash in your division code. Essentially this is just the same as ensuring integer division where python defaults to returning floats.
```py
# fractional removal to 0
3 / 4 # => 0.75
3 // 4 # => 0

# fractical removal for integers
6 / 3 # => 2.0
6 // 3 # => 2
```

## Strings

In python the **name of the string class** is `str`. For example, if you wanted to check if something is a string you would use the `str` type as your comparison target.
```py
x = "hello"
isinstance(x, str) # => True
```

You can **convert an int to a string** using the `str` method.
```py
x = 5
print("this number is " + str(x))
# => this number is 5
```

You can use **string interpolation** by appending an `f` to the beginning of a string (outside the opening `"` quote marks) and using `{ }` curly brackets around the variables you want to interpolate.
```py
x = 7
print(f"this number is {x}")
# => this number is 7
```

You can **spread a python string over multiple lines** by containing the strings inside a set of `()` soft braces at assignment.
```py
multi_line_string = ("This is a long string that is"
"split over multiple lines"
"and takes upn a lot of space.")
```

You can also **define long multi-line strings** using the `"""` triple quotation mark python syntax.
```py
multi_line_string = """This is a long string that is"
"split over multiple lines"
"and takes upn a lot of space."""
```

You can **display a number with a set number of decimal places for a number** when you convert it to a string by using the `%` operator with a string in the form `"%.[NUMBER_OF_DECIMAL_PLACES]f"`. This will add decimal places as `0` zeroes if the number doesn't have enough and remove decimal places if the number has too many, it will also **round the last decimal place**.
```py
"%.2f" % 5 # => 5.00
"%.3f" % 78 # => 78.000
"%.4f" % 1.256932 # => 1.2569
"%.3f" % 9.9877 # => 9.988 (rounded)
```

You can **display a set number of decimal places** using a shorter string interpolation syntax.
```py
f"{5:.2f}" # => 5.00
f"{78:.3f}" # => 78.000
f"{1.256932:.4f}" # => 1.2569
# with variable insertion syntax
n = 9.9877
f"{n:.3f}" # => 9.988 (rounded)
```

## Arrays

You can **add an element to a python array** with the `append` method. Sadly `push` does not exist in python 😢.
```py
x = [1, 2, 3]
x.append(4)
# => [1, 2, 3, 4]
```

## Conditionals

You can **create a one line if statement** by placing the result of the conditional on the same line after the terminating `:` colon of the if.
```py
if 3 < 5: return True
```

## Main

When calling a file by name, such as `python3 my_file` that is not the `main` (or root) executable of your project, you can **create a conditional that will call the `main` file when that non-root file is called** using the `'__main__'` matcher. In the code below when `not_main.py` is called to execute it will instead call the correct main file.
```py
# not_main.py
if __name__ == '__main__':
  my_main_file.my_main_method()
```

## Functions

Python **supports Firstclass functions**. This means that functions and methods in python can be passed around as variables.

## Classes

You can **indicate that a variable or method is private** by prepending an `_` to the front of the variable name. This doesn't *enforce* privacy but is generally accepted as a privacy naming convention and so other developers shouldn't try to directly access these methods as an interface in their code.
```py
class PrivateClass():
  
  def __init__():
    self._prive_var = "I am private."

  def _private_method():
    return "This is a private method."
```

You can **obfuscate a method or variable name** by using a `__` double leading underscore making access even more difficult. In this case python generates an obfuscated name, however the method or variable *can* still be called by this name.
```py
class ReallyPrivateClass():

  def __really_private_method():
    return "I cannot be accessed unless you know my secret name."
```

You can **check that an object has a method or attribute** by using the `hasattr` method which takes the object you are inspecting and a string representing the attribute name you are testing for.
```py
class Foo():

  def __init__():
    self.bar = "bar"

  def baz():
    pass

foo = Foo()
hasattr(foo, "bar") # => True
hasattr(foo, "baz") # => True
hasattr(foo, "Que") # => False
```

### Uniform Access Principle

Python generally follow the [uniform access principle](https://en.wikipedia.org/wiki/Uniform_access_principle) meaning that class properties should be accessed directly and you should generally **not use getter and setter methods for properties**.
```py
my_object.set_x(20) # <-- NOT SO GOOD
my_object.x = 20 # <-- BETTER
```

## Pipenv

Pipenv is a programming for managing python dependencies and project builds similar to tools like `npm` for javascript or `bundler` for ruby. The `pipenv` creates a `pipfile` which can be used to manage dependencies, project meta-data and project scripts. You can **install pipenv** using `brew`.
```bash
$ brew install pipenv
```

You ** can initialise a new pipenv project** with the `pipenv` command followed by the version of python you want to use, `--three` for python3 and `--two` for python2.
```bash
$ pipenv --three
```

You can **add scripts to your pipfile** that can be run by calling `pipenv run` and the name of the script. These are defined by creating a `[scripts]` tag section in your `pipfile` and assigning a command name to a command string.
```
[scripts]
test = "python3 -m unittest"
```

To **run the script** above you would call:
```bash
$ pipenv run test
```

You **cannot use `:` characters in a script name** like `test:unit` or `run:main`.
```
[scripts]
test:unit = "python3 -m unittest" <-- NOT ALLOWED X
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDU5NDQ3NSw0ODg0NjcyNDgsLTg5Nz
A1OTc4MiwtNjk4MzcyOTUwLC0yODI3NDY1NCwxMzczNDY1ODM4
LC0xMTk1MTI3NDA2LC01NTY0NjQwMTgsNzkwOTMxNTAxLDEyMD
A5MDM0NDgsLTg2NjAyODUyNCwtMTQzMzQ3MzQ3MywyODIxMTA5
NDcsODU5NzUyNyw2MjA5NzIzMTddfQ==
-->