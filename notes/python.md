---
title: Python
layout: page
exclude: true
---

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

When calling a file by name, such as `python3 my_file` that is not the `main` (or root) executable of your project, you can **create a conditional that will call the `main` file when that non-root file is called** using the `'__main__'` c
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM4MDc3OTQ3MSwyODIxMTA5NDcsODU5Nz
UyNyw2MjA5NzIzMTddfQ==
-->