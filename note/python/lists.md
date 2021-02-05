---
title: Lists
layout: page
exclude: true
---

You can **destructure python lists** by adding the variable names for the elements you want to destructure inline with the list. The destructured "tail" of the list has a `*` appended to it.
```python
xs = [1, 2, 3, 4, 5, 6, 7]
x, y, *tail = xs
print(x) # => 1
print(y) # => 2
print(tail) # => [3, 4, 5, 6, 7]
```

The "tail" of the list will an empty list `[]` *if* you consume all the values in the list by destructuring.
```python
xs = [1, 2]
x, y, *tail = xs
print(x) # => 1
print(y) # => 2
print(tail) # => []
```

If you **don't intend to use the "tail" values** then you should destructure them into an underscore `_` character.
```python
xs =
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA3ODM3MDE5NV19
-->