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

## Special Variables

Special Python variables are specially defined names for program specific or operational variables that usually come in the form `__VARNAME__` with `__` double underscores on each end of them.

### Name

The `__name__` variable is set to `"__main__"` inside files that are executed directly and is otherwise set to the name of the file. If `name.py` below were execute directly then it would print `"__main__"`, however if the `sayName` function were to be imported into another main file then it would output `name` as the `__name__` variable.
```py
# name.py
def sayName():
  print 'The value of __name__ is ' + __name__
```

### Main

When calling a file by name, such as `python3 my_file` that is not the `main` (or root) executable of your project, you can **create a conditional that will call the `main` file when that non-root file is called** using the `'__main__'` matcher. In the code below when `not_main.py` is called to execute it will instead call the correct main file.
```py
# not_main.py
if __name__ == '__main__':
  my_main_file.my_main_method()
```

## With and As

The `with` and `as` pattern is syntactic sugar for writing `try` and `finally` code blocks. A `with` block will assign the result of an `__enter__` method of an object and then call the `__exit__` method of the object when the `with` block finishes. The `__enter__` and `__exit__` methods represent some opening and closing of a file or data stream that needs to be sealed to avoid bugs.
```py
# 1) without using with statement
file = open("file_path", "w") 

`file` `=` `open``(``'file_path'``,` `'w'``)`

`file``.write(``'hello world !'``)`

`file``.close()`

`# 2) without using with statement`

`file` `=` `open``(``'file_path'``,` `'w'``)`

`try``:`

`file``.write(``'hello world'``)`

`finally``:`

`file``.close()`

_filter_none_

_brightness_4_

`# using with statement`
`with` `open``(``'file_path'``,` `'w'``) as` `file``:`

`file``.write(``'hello world !'``)`
```

## Functions

### Inner Functions

You can **define inner functions** in python by simply using the `def` keyword inside a python function. You **can also call these functions from their outer context**.
```py
def outer_func():
  
  print("Hello...")
  
  def inner_func():
    print("..from the otherside.")

  inner_func()

outer_func() 
# => Hello...
# => ...from the otherside.
```

Inner functions are **locally scoped to the parent function** and cannot be called outside of the function they are defined in. Calling `inner_func()` in the main scope on the code above with result in an error.

### Function objects

Python **supports functions as first-class objects**. This means that functions and methods in python can be passed around as variables and submitted as arguments to other functions. You can **call function variables** by appending two `()` soft braces to the end of the function variable.
```py
def my_func(x):
  print(x)

my_func_var = my_func

my_func_var("Hello") # => Hello
```

### Higher Order Functions

You can construct **higher order functions** by **using these function objects as function arguments**.  In the example below `my_func` is passed into `my_higher_function` where it is called with hard coded argument.
```py
def my_func(x):
  print(x)

def my_higher_function(func):
  func("Goodbye")

my_high_function(my_func) # => "Goodbye"
```

You can also construct **higher order functions** by **returning inner functions from functions**. In the example below `my_higher_function` returns an inner function as variable that can then be called.
```py
def my_higher_function():
  
  def my_func():
    print("Hello")

  return my_func

my_func_var = my_higher_function()
my_func_var() # => Hello
```

### Closures

You can ** create closures in python** by using variables define in the outer scope of a function in the inner scope and then calling the function. This **lexical scoping** allows the function to remember the context it was defined in. In the example below `outer_func` contains a `outer_var` that is then referenced inside the `inner_func` function that it returns. Even when this function is called outside of that context having been extracted in `func_var` later in the code the value of `outer_var` is still known by the `func_var` function.
```py
def outer_func():

  outer_var = "Hello"

  def inner_func():
    print(outer_var)

  return inner_func

func_var = outer_func()
func_var() # => Hello
```

### Decorators

A decorator function is a **higher order function** which **takes in a function and wraps or modifies** using a `wrapper` function. In the example below the `simple` function is passed into the `deocorate` function as an argument, then the inner `wrapper` function calls the `func` variable and adds some extra functionality. After this definition the `simple` function is then reassigned to its decorated version and called. The name `wrapper` **is purely by convention** you can call this function whatever you like as long as it doesn't clash with some other name in your application.
```py
def simple():
    print("I am simple function.")

def decorate(func):
    
    def wrapper():
        func()
        print("I've made this function much better.")

    return wrapper

simple = decorate(simple)
simple()
# => I am simple function.
# => I've made this function much better.
```

You can **define a decorator function more easily** by using python's `@` at symbol, also known as **pie syntax** to invoke a decorator function on another function without having to actively re-assign the function definition through the decorator. By using `@decorate` in the example below the `simple` function is automatically assigned to use the `decorate` decorator and is altered very easily. This also means that you can **re-use and generalise decorators** for a range of different functions.
```py
def decorate(func):
    
    def wrapper():
        func()
        print("I've made this function much better.")

    return wrapper

@decorate
def simple():
    print("I am simple function.")

simple()
# => I am simple function.
# => I've made this function much better.
```



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

### Inheritance

You can **use the superclass version of a method** by using the `super()` method to return the superclass instance of your current object and then call the method you want to invoke. In the example below the `Bar` class inherits from the `Foo` class and overrides the `Foo` method `hello`. Using the `super()` method we call the `Foo`'s implementation of `hello` before `Bar` executes its own implementation.
```py
class Foo():
  def hello():
    print("hello...")

class Bar(Foo):
  def hello():
    super().hello()
    print("..from the otherside.")

bar = Bar()
bar.hello()
# => hello...
# => ...from the otherside.
```

### Uniform Access Principle

Python generally follow the [uniform access principle](https://en.wikipedia.org/wiki/Uniform_access_principle) meaning that class properties should be accessed directly and you should generally **not use getter and setter methods for properties**.
```py
my_object.set_x(20) # <-- NOT SO GOOD
my_object.x = 20 # <-- BETTER
```

## Magic Methods

Magic Methods, such as `__init__` or `__add__`, also known as Dunder methods (because they have *double underscores* in their name) are special python methods for doing specific object related tasks in python. They also define arithmetic and comparative operator functions on objects in python.

Magic methods **cannot be reassigned**, they are **read only** properties. This is a hard coded property of python.
```py
def sum_func():
  pass

num = 2
num.__add__ = sum_func
# => __add__ is READ ONLY
```

### repr

The `__repr__` method **allows you to change how an object is represented when it is printed**. By implementing this method inside your class when an instance of the class is passed to the `print` method it will use the `__repr__` method. 
```py
class MyObject():
  def __init__(self):
    self.name = "foo"

  def __repr(self):
    return self.name

my_object = MyObject()
# before defining repr:
print(my_object) # => <__main__.MyObject object at 0x10eac8490>
# after defining repr:
print(my_object) # => foo
```

If  `__repr__` had not been defined in `MyObject` when we printed an instance of it we would have instead printed our the path to our object with an address in memory where the object is stored, something like this:
```
<__main__.MyObject object at 0x10eac8490>
```

### Comparative Magic Methods

| Magic Method Symbol | Equivalent Implementation |
| --- | --- |
| `__eq__` | `==` |
| `__gr__` | `>` |
| `__lt__` | `<` |

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

### Installation

You can **install everything from you pipfile's `[package`] section** by using the `install` command. This **does not install anything from the `[dev-packages]` section** of the `pipfile`.
```bash
$ pipenv install
```

You can **install dependencies from your pipfile's `[dev-packages]` section** by using the `--dev` flag with the `install` command.
```bash
$ pipenv install --dev
```

### .env

If you have a `.env` file in your project directory running `pipenv` commands like `run` and `shell` should automatically load environmental variables defined in that file.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcwODMxNzg1OSwyODM5ODg0NzksMTkwNT
E4NTMwMiwtMjkzOTk5MDczLC05Nzg4MzkzOTUsMTk5ODE4NzE4
OCw1NjE4NTkwOCwtMTk5MzU5MzE2NCwtMjQ1MzI4NzUyLDI1Nz
YyNjc5NywyMDE3ODk1MzgwLC0xODY2OTIzMDI3LDEzNzMxMzM1
NzEsLTE0NDU5NDQ3NSw0ODg0NjcyNDgsLTg5NzA1OTc4MiwtNj
k4MzcyOTUwLC0yODI3NDY1NCwxMzczNDY1ODM4LC0xMTk1MTI3
NDA2XX0=
-->