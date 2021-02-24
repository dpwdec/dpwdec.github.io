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


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMzNjcyNjc1OSwtMjIwNzA0M119
-->