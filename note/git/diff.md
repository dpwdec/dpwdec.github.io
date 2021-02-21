---
title: Git Diff
layout: page
exclude: true
---

Flags for `git diff` should come before the commit name arguments for the diff.
```bash
$ git diff <
```

You can **show just the names of the file that changed** when calling running a `diff` by using the `name-only` flag.
```bash
$ git diff --name-only HEAD^ HEAD
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY4NTc3ODg1MF19
-->