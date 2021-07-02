---
title: Named Tuples
layout: page
exclude: true
---

Named tuples allow you to **store object like data without the need for an entire class definition** or the use of a more complex data structure.
```python
import collections

Animal = collections.namedtuple('Animal', 'species gender name')

dog = Animal(species="Dog", gender="Male", name="Bruno")

print(dog.name) # => "Bruno"
```

Importantly, **named tuples are NOT mutable**. You should use the `recordclass` module if you want a mutable data storage structure.