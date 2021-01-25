---
layout: page
exclude: true
title: Mkdir
---

You can **make all the folders in a file path** using the `-p` flag. Usually if you type `some/path` as the argument to `mkdir` it will try to create the folder `path` inside the *pre-existing* folder `some`, *however* using `-p` it will instead create the folder `some` and then the folder `path` inside it.
```bash
$ mkdir -p some/path
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxOTc1NDUyM119
-->