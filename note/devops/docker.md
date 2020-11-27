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

## Images

You can **see what images are available to run in docker** by using the `images` command.
```bash
$ docker images
```

You can **also use** the `docker image ls` command, which is the **updated image listing commander**.
```bash
$ docker image ls
```

This will **show the docker image's `IMAGE ID` field** (in truncated form) which can be used to uniquely identify an image. You can **run docker images based on their `IMAGE ID`** by using the ID in place of the image's name.
```bash
$ docker run <IMAGE_ID>
```

You can see a **non truncated docker `IMAGE ID`** using the `--no-trunc` flag on the `images` command.
```bash
$ docker images --no-trunc
```


## Dockerfile

The `Dockerfile` allows you **to define a blueprint for an image**. Capatilization of docker directives like `FROM` and `RUN` is **not mandatory** however it is **best practice**.

You can **base your docker image on an existing docker image** using the `FROM` command followed by the name of the image (this can be as it appears on services like dockerhub).
```docker
FROM <IMAGE_NAME>
```

You can **customise your image** by using the `RUN` command to execute a command in the environment that the image is based on. In the example below the dockerfile starts from the ubuntu environment and installs python.
```docker
FROM ubuntu
RUN apt-get install -y python3
```

The `MAINTAINER` directive has been **deprecated**. However if you can **add meta to your dockerfile** using the `LABEL` directive which takes a key-value pair assigned with an `=`.
```docker
LABEL maintainer="my_name@some-website.com"
```

### Building

You can **build an image from your `Dockerfile`** using the `build` command. You can **pass this any filename** which contains valid docker instructions.
```bash
$ docker build Dockerfile
```

You can also use `.` syntax if you are in a folder with a valid `Dockerfile`.
```bash
$ docker build .
```

After each step of docker build **produces an intermediate docker image** that is then removed before the next step is ready to run.

## Running

You can **run a docker image** using the `docker run` command.
```bash
$ docker run <IMAGE_NAME>
```

You can **also use** `docker container run` which is the **updated docker command**.
```bash
$ docker container run <IMAGE_NAME>
```

You can **give a docker image a name as it runs** by using the `--name` flag.
```bash
$ docker container run --name some-name <IMAGE_NAME>
```

You can **run a container interactively** by using the `-it` flag. This will allow you to execute commands inside the container through a command prompt *as if* you had connected or ssh'd into the conta

## Hub

You can **find existing images to use as a base for your custom images** by using the [Docker Hub](https://hub.docker.com/) service. It is possible to **host private docker image repositories** in your own infrastructure.

The Docker Hub has a registry and repository structure for holding images.

**Official** images hosted on the hub are maintained by the creators of the service they host and should be go to for hosting docker content.

You can **pull an image down from the docker hub to run locally** using the `pull` command followed by the name of the image. By default this pulls the **latest version** of the image.
```bash
$ docker pull <IMAGE_NAME>
```

For example:
```bash
$ docker pull hello-world
```

You can **pull a particular version of a docker image** by adding a `:` colon to the name of an image followed by the version.
```bash
$ docker pull <IMAGE_NAME>:<IMAGE_VERSION>
```

For example:
```bash
$ docker pull ubuntu:16.04
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcxOTE1MjQxNywyMTE4MzE5Mzk3LDE3Mj
k1NjQ4NDcsNzgzNzMyNjQsNTQzNjU1MTU3LC04OTg0MDUxMTgs
LTEyOTQzNjMwMjQsOTA4OTYzNjM3LDE4MDYyNzYwNTYsMjAwMj
gxODQwNiwtMTgyNTA2NDQ5NCwxNDc5MDc3NTA2LDE1OTAxMjI5
NjMsLTE3Mjk0Njk5NTIsMzY2OTAwNjc5LDQwNDI5NjMwNSwtOD
U3NDM3MDM0XX0=
-->