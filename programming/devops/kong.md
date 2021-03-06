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

## Paths

By **default kong strips out path extensions** with the `strip_path` property. This means, any matched path will just go to the root `/` path on the upstream API. Set `strip_path` to false if you want the path information to be preserved when it reaches the upstream.

## Commands

You can **start kong with a debug log at set up** by using the `vv` flag.
```bash
$ kong start --vv
```

You can **reload kong** with the `reload` command.
```bash
$ kong reload
```

You can **stop kong running** using the `kong stop` command.
```bash
$ kong stop
```

## HTTP/S

Kong defaults to forwarding requests to upstream URIs using the HTTP protocol *on* port 80. This can be an **issue if the upstream service that Kong is forwarding to is designed to working using HTTPS traffic** (for example, a cloudfront distribution). 

When **configuring Kong to use HTTPS** you should bear in mind that Kong keeps the port and protocol configuration separate, so, if the protocol is set to HTTPS the port will *still* default to 80 even though the correct port for HTTPS traffic is port 403. Because of this you **must set both the port and protocol to the appropriate values** when configuring Kong to forward HTTPS traffic.

## Redirection and Kong Browser URLs

When returning web content to a browser for display from an upstream URI, **the URL of the page should NOT change**, matching the initial URL that the user made a request to and the URL that was matched and handled by Kong. 

However, **if the content that Kong receives back is in some way redirected then this can cause browser URL to display a different location from the initial Kong request**. 

For example, if I visit `www.yolo-42.com` in my browser, but have set up a Kong instance to manage ingress traffic to my site that forwards requests for web content for the homepage to an upstream S3 service with its own url (whatever that may be), the URL I see in my browser still remains as `www.yolo-42.com` because Kong simply returns this content itself. *However*, if the content that Kong forwards to has instead been moved in some way and returns a redirection response, such as a `301`, then the browser will receive that redirection notice from Kong after the initial request and follow the redirection link to return the content from the new location, in the process changing the URL displayed in the browser (because its now visiting a new location not tied to Kong) to whatever the redirect location is and then returns that content.

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

You can **add a preinstalled plug in to a kong service** by using the `plugins` extension with the data set to the `name` of the plugin you want to install on that service.
```bash
$ curl -X POST http://<admin-hostname>:8001/services/<service>/plugins \  
  --data  "name=<plugin-name>"
```

## DecK

DecK is a **desired state synchronisation tool** that allows you to set kong's configuration using a configuration file (defined in `yaml`).

You can **output the current configuration of kong** using the `dump` command. This will output the configuration as `.yaml` file from the `localhost:8001` port that hosts the current instance of kong.
```bash
$ deck dump
```

You **cannot run the `dump` command on an ALB or general cluster of deployed kong instances** you must run the dump directly on a single running kong instance.

You **can apply a `.yaml` configuration to kong** using the `sync` command. By default this will post to the `localhost:8001` port for kong and set the kong's configuration so that it matches source file provided. The `-s` flag specifies the *source* file to use.
```bash
$ deck sync -s path/to/config.yaml
```

You can **run deck commands on remote deployments of kong** by using the `--kong-addr` flag. In the example below the `sync` command will post to a remote version of kong hosted at `my-kong.com`.
```bash
$ deck sync --kong-addr http://my-kong.com:8001 -s path/to/config.yaml
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc4MTY2MzUxLDU1NjEzMDM0Myw1MzA3Nj
gyNzIsLTE0ODgyOTA3OTIsLTEwMjczMDA4MDAsNDY1NTI0Mjk3
LC0xMzY4MTE1ODk0LC0xOTQ5NDQyMTQzLDE1NzUxMDU5NjcsLT
IwNTQ0MTE3NzksLTkwNzk0Mjg5OSwxNzUyMjMyNjksLTQwNzA0
NzU1MywyMDQ0ODM5MDc2LDUxNjA4NzUxMCwtMTI0MTI2OTg0MC
wtNTI5ODAxODExXX0=
-->