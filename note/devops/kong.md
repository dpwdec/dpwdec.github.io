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

Kong runs **consumer ports** on `8000` for standard requests and `8443` for SSL requests and **admin ports** on `8001` for standard requests and `8444` for SSL requests. Kong is **configured by making HTTP requests to the admin ports**.

## Commands

You can **reload kong** with the `reload` command.
```bash
$ kong reload
```

You can **stop kong running** using the `kong stop` command.
```bash
$ kong stop
```

## Services

**Services** are the name given to **upstream microservice APIs** that kong acts as a gateway to. A service can contain many **routes** which specify *how* requests that reach kong are sent to upstream services.

You can **c**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyODM3NDE0MywxNzUyMjMyNjksLTQwNz
A0NzU1MywyMDQ0ODM5MDc2LDUxNjA4NzUxMCwtMTI0MTI2OTg0
MCwtNTI5ODAxODExXX0=
-->