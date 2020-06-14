---
title: Python
layout: page
exclude: true
---

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

## Main

When calling a file by name, such as `python3 my_file` that is not the `main` (or root) executable of your project, you can **create a conditional that will call the `main` file when that non-root file is called** using the `'__main__'` matcher. In the code below when `not_main.py` is called to execute it will instead call the correct main file.
```py
# not_main.py
if __name__ == '__main__':
  my_main_file.my_main_method()
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg2NjAyODUyNCwtMTQzMzQ3MzQ3MywyOD
IxMTA5NDcsODU5NzUyNyw2MjA5NzIzMTddfQ==
-->