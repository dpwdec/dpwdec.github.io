---
title: whatchanged
layout: page
exclude: true
---

The `whatchanged` command is an **alias for a `git log` command**  with `--raw` and `--no-merges`.
```bash
$ git log --raw --no-merges
```

You can **show a log of everything that changed by date** using the `whatchanged` command with the `--since` flag. This will show a rich set of outputs showing all changes for a relative period of time from when the command is executed.
```bash
$ git whatchanged --since="1 day ago"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEwMTAyNjQ0MywxNDg2MDI4NzA4XX0=
-->