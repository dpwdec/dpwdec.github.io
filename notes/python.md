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

In python the **name of the string class** is 

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzOTU0NjQzNDAsLTU1NjQ2NDAxOCw3OT
A5MzE1MDEsMTIwMDkwMzQ0OCwtODY2MDI4NTI0LC0xNDMzNDcz
NDczLDI4MjExMDk0Nyw4NTk3NTI3LDYyMDk3MjMxN119
-->