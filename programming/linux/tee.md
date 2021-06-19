---
layout: page
exclude: true
title: Tee
---

You can **use `tee` instead of double redirection modifier `>>`** as the implementation of the redirection modifier `>>` on different linux distributions is inconsistent.

You can **append to a file** by using the `tee` command with the `echo` of what you want to append piped `|` to the command. The **`-a` flag indicates that the text you should appended** to the target file.
```bash
$ echo "some text" | tee -a file.txt
``` 

If you have **problems with user permissions** you can `sudo` the `tee` part of the command.
```bash
$ echo "some text" | sudo tee -a file.txt
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDcyMzU3MDddfQ==
-->