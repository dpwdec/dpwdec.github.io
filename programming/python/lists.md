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
xs = [1, 2, 3, 4, 5, 6, 7]
x, y, *_ = xs
print(x) # => 1
print(y) # => 2
```

You can **destructure a list in reverse** taking the "init" and "last" elements from a list by including the `*` property first.
```python
*init, last = [1, 2, 3, 4, 5]
print(init) # => [1, 2, 3, 4]
print(last) # => 5
```

You can **match arbitrarily on these elements as well**.
```python
head, x, *middle, last = [1, 2, 3, 4, 5]
print(head) # => 1
print(x) # => 2
print(middle) # => [3, 4]
print(last) # => 5
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc3OTk2NzkwNCwxMDczMzI2NDg5XX0=
-->