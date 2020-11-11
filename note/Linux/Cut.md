---
layout: page
exclude: true
title: Cut
---

You can **get a substring in a range** using the `cut` command. This command takes a flag `-c` followed by a range of 1 indexed characters to return, described in the format `-cI-N` where `I` is the ith character to start from and `N` is the nth to strip to.
```bash
$ echo "STRING" | cut -c2-4 # => TRI
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjIxNjEyNTMwLC0xOTQ3NTgzNiw3ODM2OD
U2MDEsLTE4NzU2OTc5MDJdfQ==
-->