---
title: Docker
layout: page
exclude: true
---

Docker is an application containerisation system.

Applicatons are **deployed in three steps**:

 1. Creating a `Dockerfile` that describes how a docker image is built
 2. Building a docker image file
 3. Running the docker image file in docker

You can **see what images are available to run in docker** by using the `images` command.
```bash
$ docker images
```

## Hub

You can **find existing images to use as a base for your custom images** by using the [Docker Hub](https://hub.docker.com/) service. It is possible to **host private docker image repositories** in your own infrastructure.

The Docker Hub has a registry and repository structure for holding images.

**Official** images hosted on the hub are maintained by the creators of the service they host and should be go to for hosting docker content.

You can **pull an image down from the docker hub to run locally** using the `pull` command followed by the name of the image.
```bash
$ docker pull <IMAGE_NAME>
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk0ODM0MzA3NywxNDc5MDc3NTA2LDE1OT
AxMjI5NjMsLTE3Mjk0Njk5NTIsMzY2OTAwNjc5LDQwNDI5NjMw
NSwtODU3NDM3MDM0XX0=
-->