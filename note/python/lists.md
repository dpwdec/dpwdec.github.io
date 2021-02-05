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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg3OTcyMTgyM119
-->