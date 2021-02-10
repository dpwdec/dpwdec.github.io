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

You can **execute a command** by using the `run` method on `subprocess` and a string that contains the command to be executed. This followed by a set of configuration arguments. If you want **to execute something on the command line** then the `shell` argument should be set to `True` (this allows you to use things like pipes and other features of the shell in your command).
```python
subprocess.run("echo Hello World", shell=True)
```

If `shell` is set to `False` then the command should simply name another program to execute.

If you want to **get output from the command that is run** and **store this output into a value that can be used by the python script that called this process** set the `capture_output` argument to `True`. This captures the `stdout` and `stderr` from the executing command which can be referenced from the object that the command returns. This is returned in the form of a byte string that needs to be `decode`d into some value - usually a string using `utf-8`.
```python
subprocess.run("echo Hello World", shell=True, capture_output=True).stdo
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU1ODI5OTI1M119
-->