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

You can **create**

## Systemd



## Service

Linux uses service files to define how a service should start.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NzA1NDQ2MTgsLTE1ODM2NDQwNTcsND
Q0MjU4NjkxLDE5MDczNzg2MjgsNDE5OTk5Njc3LC0zOTU2NDAz
MjEsMTgyNzk1NTAyLC0xNjQ2NTk0NDk4LDExODcyMDAzMjYsMT
IxOTYzMzI4NV19
-->