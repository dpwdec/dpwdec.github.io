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

Below is an example of the above script called with a list space separated inputs. The **first argument** at index `0` in the `argv` property will be the script that was called for python execution, followed by the arguments used.
```bash
$ python3 args.py 1 hello 3.2
> args.py
> 1
> hello
> 3.2
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzNzA2OTQ4MiwxOTU3MzA1NDY2LDE3OT
E5NzE5OThdfQ==
-->