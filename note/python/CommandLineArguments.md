---
title: Command Line Arguments
layout: page
exclude: true
---

You can **access arguments passed into a python script** using the `argv` property of python's `sys` object. You will need to import `sys` for this to work.
```python
# args.py
import sys

for arg in sys.argv:
	print(arg)
```

I
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI1NDU3MDMyOCwxOTU3MzA1NDY2LDE3OT
E5NzE5OThdfQ==
-->