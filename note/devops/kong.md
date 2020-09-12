---
title: Kong
layout: page
exclude: true
---

Kong is a tool that faciliatates managing a microservices architecture.

## Installation

Kong can be installed on a vartiety of services.

### OSX

First **create a new postgresql user and database** called `kong` and set the owner to the `kong` user.
```bash
$ CREATE USER kong;
$ CREATE DATABASE kong OWNER kong;
```

Then **create a new `kong.conf`** file. It doesn't matter where this file is created.
```bash
$ touch some/folder/path/kong.conf
```

Next, **migrate your kong database** using the `migrations bootstrap` with the relative path from your current folder location to the `kong.conf` file.
```bash
$ kong migrations bootstrap some/folder/path/kong.conf
```

Finally, **start kong** using the `kong start` command, again wtih the relative path from your current folder location to the `kong.conf` file.
```bash
$ kong start some/folder/path/kong.conf
```

## Ports

Kong runs **consumer ports** `8000` and `8443` and **admin ports** on `8001` and `8444`.

## Quitting

You can **stop kong running** using the `kong stop` command.
```bash
$ kong stop
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzI2OTkyNjcsMjA0NDgzOTA3Niw1MTYwOD
c1MTAsLTEyNDEyNjk4NDAsLTUyOTgwMTgxMV19
-->