---
title: log
layout: page
exclude: true
---

You can **apply filters for particular types of changes** to the `log` command using the `--diff-filter` flag. The example below will only show logs for files that were added.
```bash
$ git log --raw --no-merges --diff-filter=A
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzg4ODI4NDQxXX0=
-->