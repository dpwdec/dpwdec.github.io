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

You can **create global environment variables** for all users by adding to the `/etc/environment` file.

## Sudo

You can **assume the sudo user role** using the `-s` flag on the `sudo` command. This essentially starts a shell with root user.
```bash
sudo -s
```

This is useful if you want to use a command like `source` with the root user. The `source` command isn't actually a program so can't be run directly with `sudo`. Instead you need to switch to the root user's shell first. This is because `source` is a shell builtin.

## Systemd



## Service

Linux uses service files to define how a service should start.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzgyNDYyNTYxLC0xMzU1OTYzMDc0LC0xNT
gzNjQ0MDU3LDQ0NDI1ODY5MSwxOTA3Mzc4NjI4LDQxOTk5OTY3
NywtMzk1NjQwMzIxLDE4Mjc5NTUwMiwtMTY0NjU5NDQ5OCwxMT
g3MjAwMzI2LDEyMTk2MzMyODVdfQ==
-->