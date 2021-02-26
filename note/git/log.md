---
title: log
layout: page
exclude: true
---

You can **apply filters for particular types of changes** to the `log` command using the `--diff-filter` flag. The example below will only show logs for files that were added.
```bash
$ git log --raw --no-merges --diff-filter=A
```

## Period Log

You can **see a log of what changed over a period** by using the `since`
```bash
$ git log --raw --no-merges --since="2 day ago" --diff-filter=RAD --pretty=format: --name-only
```

```bash
git log --raw --no-merges --since="2 day ago" --diff-filter=RAD
```

```bash
git log --raw --no-merges --since="2 day ago" --diff-filter=RAD --pretty=format: --name-only
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjY3MzE0MjIzXX0=
-->