---
title: List Comprehensions
layout: page
exclude: true
---

You can **split a list comprehension over multiple lines** to make them easier to read.
```python
[ x.some_function()
  for x in some_list
  if math_element(x) ]
```

You can **pass list comprehensions directly into functions that accept lists** without the need for square brackets `[]` to indicate the lists creation.
```python
some_list_function(
  some_function(x)
  for x in some_list)
```

There *is* a `filter` function built into python that takes a list and a 


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk4MTgwODIyMiwxNTkzNDg3Nzg5LC0xMT
I2MjYzNTQ2XX0=
-->