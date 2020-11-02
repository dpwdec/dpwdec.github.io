---
title: argparse
layout: page
exclude: true
---

`argparse` is a python library for creating command line interfaces and parsing command line arguments.

`argparse` **creates an object that matches the different input fields defined for your command line interface**, these fields are populated from the data submitted by a user or are assigned as defaults, or otherwise unused.
```py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--message", default="hello", dest="message")

args = parser.parse_args()
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQwNzU4NjM5LC00MDQ3Nzk3NzZdfQ==
-->