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

There *is* a `filter` function built into python that takes a list and a predicate to filter that list again. However, its much easier to use the filter built into list comprehension syntax with the `if` statement, if you want to operate on the contents of the list at the same time rather than *just* filter it.


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA4MzY5NjI2NiwxNTkzNDg3Nzg5LC0xMT
I2MjYzNTQ2XX0=
-->