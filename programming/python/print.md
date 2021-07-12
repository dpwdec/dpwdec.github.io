---
title: Print
layout: page
exclude: true
---

You can **update a line that you are printint to** by setting the `end` property character of the `print` command to a `\r` character. *Make sure that the last thing you print doesn't use the `\r` character*.
```python
import time

print("foo", end='\r')
time.sleep(1)
print("bar", end='\r')
time.sleep(1)
print("baz")
```

If you want to do more complex multiline terminal manipulation you will have to use a graphics library.