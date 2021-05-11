---
layout: page
exclude: true
title: EC2
---

You can **SSH onto an Amazon Linux machine** by using the `ec2-user` user for the SSH.
```bash
$ ssh -i <KEY> ec2-user@<IP_ADDRESS>
```

To **run a web server on an ec2 machine that can be routed to from an external source** the host of the web server application needs to be set to `0.0.0.0` otherwise you will get a `Connection refused` error because the instance will not actually be listening.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUzMzE2MzkxMiwxMTM3MjYxNjkyXX0=
-->