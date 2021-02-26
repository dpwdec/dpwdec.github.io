---
title: Git Diff
layout: page
exclude: true
---

Flags for `git diff` should come before the commit name arguments for the diff.
```bash
$ git diff <FLAG_ONE> <FLAG_TWO> <COMMIT_1> <COMMIT_2>
```

You can **limit the diff to particular folders** in a repository by appending a list of repository paths *after* the diffed commit identifiers. In the example below, the `diff` will only be run on files in the specified folders.
```bash
git diff HEAD^ HEAD my_folder another/folder/path
```

You can **show just the names of the file that changed** when calling running a `diff` by using the `name-only` flag.
```bash
$ git diff --name-only HEAD^ HEAD
```

You can **limit the type of changes that get displayed by the diff** using the `diff-filter` flag followed by a string of letters that indicate different actions. For example, the `diff` query below will only pick up diffs between the commits for files that are *added* `A` or *deleted* `D` to the project.
```bash
$ git diff --diff-filter=AD HEAD^ HEAD
```

You can **diff files that are moved** by using the `R` filter for *rename*. Git counts files that get moved to a different location in the project as *renamed* file and thus uses the `R` `diff-filter` tag.
```bash
$ git diff --diff-filter=R HEAD^ HEAD
```

## Period diff

You can **do a diff on commits between to dates** by passing the result of `rev-list` into a `diff` command. 
```bash
$ git diff $(git rev-list -n1 --before="1 day ago" master)
```

You can see more information about this [here](https://stackoverflow.com/questions/1161609/how-can-i-get-the-diff-between-all-the-commits-that-occurred-between-two-dates-w).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NjI0Nzc5OTYsNDU5MDI3MzIwLC0xOT
YzOTUzMjA3LC0xNDUyNzM5MTQzLC0zMzY3MjY3NTksLTIyMDcw
NDNdfQ==
-->