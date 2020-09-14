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

You can **create a new kong service** by `POST`ing to the `services` extension on kong's admin port with two pieces of data: a `name` that will describe the kong extension for the service, and a `url` where the upstreasm service is located.
```bash
$ curl -i -X POST \
  --url http://localhost:8001/services/ \  
  --data  'name=example-service' \  
  --data  'url=https://website.com/'
```

You can **create a route to your service** by making a `POST` request to your new service url followed by the `/routes` extension and setting a `host` that kong should route to when it receives requests with that `host` in the header.
```bash
$ curl -i -X POST \
  --url http://localhost:8001/services/example-service/routes \  
  --data  'hosts[]=example.com'
```

## Plugins

You can **add a preinstalled plug in to a kong service** by using the `plugin
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU3NTEwNTk2NywtMjA1NDQxMTc3OSwtOT
A3OTQyODk5LDE3NTIyMzI2OSwtNDA3MDQ3NTUzLDIwNDQ4Mzkw
NzYsNTE2MDg3NTEwLC0xMjQxMjY5ODQwLC01Mjk4MDE4MTFdfQ
==
-->