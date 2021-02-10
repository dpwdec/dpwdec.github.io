---
title: subprocess
layout: page
exclude: true
---

Python's subprocess library allows you to execute other programs and OS commands from within a python program.

To **start using subprocess** you need to import the `subprocess` dependency. This is the entry point for all subprocess calls.
```python
import subprocess
```

You can **execute a command** by using the `run` method on `subprocess` and a string that contains the command to be executed. This followed by a set of configuration arguments. If you want **to execute something on the command line** then the `shell` argument should be set to `True`.
```python
subprocess.run("echo Hello World"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA5Mzc3MDI3NV19
-->