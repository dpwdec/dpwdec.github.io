---
title: Record Class
layout: page
exclude: true
---

You can **install the `recordclass` module** using `pip3`.
```
pip3 install recordclass
```

You can **create mutable structures for storing data** by using the `recordclass` object in the same way as you would a `namedtuple`.
```python
from recordclass import recordclass

Animal = recordclass('Animal', 'species gender name')

dog = Animal(species="Dog", gender="Male", name="Bruno")

print(dog.gender) # => "Male"

dog.gender = "Female"

print(dog.gender) # =>m "Female"
```