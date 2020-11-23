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

Linux uses service files
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDQ0MjU4NjkxLDE5MDczNzg2MjgsNDE5OT
k5Njc3LC0zOTU2NDAzMjEsMTgyNzk1NTAyLC0xNjQ2NTk0NDk4
LDExODcyMDAzMjYsMTIxOTYzMzI4NV19
-->