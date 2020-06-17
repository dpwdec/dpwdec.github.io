---
title: Python
layout: page
exclude: true
---

## Importing

You can **import python code from a parallel directory** by setting up each directory as a `package` using the `__init__.py` file and then importing using the `from` and `import` keywords.

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

## Pipenv

Pipenv is a programming for managing python dependencies and project builds similar to tools like `npm` for javascript or `bundler` for ruby. The `pipenv` creates a `pipfile` which can be used to manage dependencies, project meta-data and project scripts. You can **install pipenv** using `brew`.
```bash
$ brew install pipenv
```

You ** can initialise a new pipenv project** with the `pipenv` command followed by the version of python you want to use, `--three` for python3 and `--two` for python2.
```bash
$ pipenv --three
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM3MzQ2NTgzOCwtMTE5NTEyNzQwNiwtNT
U2NDY0MDE4LDc5MDkzMTUwMSwxMjAwOTAzNDQ4LC04NjYwMjg1
MjQsLTE0MzM0NzM0NzMsMjgyMTEwOTQ3LDg1OTc1MjcsNjIwOT
cyMzE3XX0=
-->