---
title: argparse
layout: page
exclude: true
---

`argparse` is a python library for creating command line interfaces and parsing command line arguments.

`argparse` **creates an object that matches the different input fields defined for your command line interface**, these fields are populated from the data submitted by a user or are assigned as defaults, or otherwise unused. In the example below we define a CLI that has an optional flag `--message`, this value is set by the user but defaults to `hello` and is placed on the `dest`ination object when `parse_args` is called in a field called `message`.
```py
#cli.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--message", default="hello", dest="message")

args = parser.parse_args()

print(args.message)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYyNzI4NjU4MiwtNDA0Nzc5Nzc2XX0=
-->