---
title: Linux 
layout: page
exclude: true
---

`systemctl` can be used to start and stop services based on configuration in `systemd`.

`ps` shows running processes

`ps -ef` shows extra running process detail

`cut` to strip out

${variable:5}

You can **make your script executable for all users** by using the `chmod +x` command.
```bash
$ chmod +x my_script.sh
```

You can **invoke a previous command** by using the `!!` double exclamation indicator. This is useful for rerunning a command with `sudo`.
```bash
$ touch mysecure
$ sudo !!
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM5NTY0MDMyMSwxODI3OTU1MDIsLTE2ND
Y1OTQ0OTgsMTE4NzIwMDMyNiwxMjE5NjMzMjg1XX0=
-->