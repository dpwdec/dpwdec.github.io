---
title: Linux 
layout: page
exclude: true
---

`systemctl` can be used to start and stop services based on configuration in `systemd`.

`ps` shows running processes

`ps -ef` shows extra running process detail

${variable:5}

You can **make your script executable for all users** by using the `chmod +x` command.
```bash
$ chmod +x my_script.sh
```

You can **invoke a previous command** by using the `!!` double exclamation indicator. This is useful for rerunning a command with `sudo`.
```bash
$ touch mysecurefile.yml
$ sudo !! # => evaluates to $ sudo touch mysecurefile.yml
```

## Service


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAwNDE3NTU1OSwxOTA3Mzc4NjI4LDQxOT
k5OTY3NywtMzk1NjQwMzIxLDE4Mjc5NTUwMiwtMTY0NjU5NDQ5
OCwxMTg3MjAwMzI2LDEyMTk2MzMyODVdfQ==
-->