---
layout: page
exclude: true
title: Cut
---

You can **get a substring in a range** using the `cut` command. This command takes a flag `-c` followed by a range of 0 indexed characters to return, described in the format `-cI-N` where `I` is the ith character to start from and `N` is the nth to strip to.
```bash
$ echo "STRING" | cut -c1
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NDc1ODM2LDc4MzY4NTYwMSwtMTg3NT
Y5NzkwMl19
-->