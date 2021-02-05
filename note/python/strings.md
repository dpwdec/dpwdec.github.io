---
title: Strings
layout: page
exclude: true
---

You can **remove a character from a python script** using the `strip` function. It seems that you may *have* to use `''` single quotes around the `strip` argument for this to work.
```python
'hello there\n'.strip('\n') # => 'hello there'
```

If you want to **remove trailing characters at the end of a string** use the `rstrip` method. 

You **must use single quotes `''` inside an `f` string** if you want to specify string types inside of it.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg4ODA0ODc2OF19
-->