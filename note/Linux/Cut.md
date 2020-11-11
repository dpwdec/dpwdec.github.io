---
layout: page
exclude: true
title: Cut
---

You can **get a substring in a range** using the `cut` command. This command takes a flag `-c` followed by a range of 1 indexed characters to return, described in the format `-cI-N` where `I` is the ith character to start from and `N` is the nth to strip to, this also **includes the character that you strip from**.
```bash
$ echo "STRING" | cut -c2-4 # => TRI
```

You can **get a substring until the end of a string** by leaving the second number (`N`) empty.
```bash
$ echo "STRING" | cut -c2- #
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMjUyNDc0MjksLTE5NDc1ODM2LDc4Mz
Y4NTYwMSwtMTg3NTY5NzkwMl19
-->