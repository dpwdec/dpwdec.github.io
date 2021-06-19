---
title: REPL
layout: page
exclude: true
---

You can **load a pre-written file into the python REPL**, so that you can access functions, classes etc. that you have created outside the repl by using the `exec` function and reading into the code from a file.
```bash
$ python3
>>> exec(open('my_script.py').read())
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMzNjQxNzgxNF19
-->