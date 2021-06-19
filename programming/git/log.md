---
title: log
layout: page
exclude: true
---

The `log` command **runs on whatever branch is currently checked out**.

You can **apply filters for particular types of changes** to the `log` command using the `--diff-filter` flag. The example below will only show logs for files that were added.
```bash
$ git log --raw --no-merges --diff-filter=A
```

## Period Log

You can **see a log of what changed over a period** by using the `since` flag with a string representing the relative time period of changes.
```bash
$ git log --raw --no-merges --since="1 day ago"
```

You can **filter by specific change types** by adding a `--diff-filter` flag.
```bash
git log --raw --no-merges --since="2 day ago" --diff-filter=RAD
```

You can **format the log results to show ONLY the names of a files that changed** by using the `--pretty` flag with the `--name-only` format.
```bash
$ git log --raw --no-merges --since="2 day ago" --diff-filter=RAD --pretty=format: --name-only
```

Wherever `git log --raw --no-merges` is used it can be replaced with `whatchanged`.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzI1MTg0Nzg1LDEwMzc4NDE1NzldfQ==
-->