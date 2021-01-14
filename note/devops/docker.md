---
title: Docker
layout: page
exclude: true
---

Docker is an application containerisation system.

Applicatons are **deployed in three steps**:

 1. Creating a `Dockerfile` that describes how a docker image is built
 2. Building a docker image file
 3. Running the docker image file in docker as a container

A `Dockerfile` creates an image an image file is then `run` to create a container and a container can be started stopped and interacted with *after* creation.

## Images

You can **see what images are available to run in docker** by using the `images` command. This list is added to when you build a new container.
```bash
$ docker images
```

You can **also use** the `docker image ls` command, which is the **updated image listing command**.
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

## Containers

You can **run a docker image** using the `docker run` command.
```bash
$ docker run <IMAGE_NAME>
```

When you run an image you **create a container** which is the interactable, concrete version of an image.

You can **also use** `docker container run` which is the **updated docker command**.
```bash
$ docker container run <IMAGE_NAME>
```

You can **give a docker container a name as it runs** by using the `--name` flag. If you don't give your container a name, then a name will be generated using the `names-generator.go` repo from the [`moby` project](https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go) that docker maintains.
```bash
$ docker container run --name some-name <IMAGE_NAME>
```

You can **run a container interactively** by using the `-it` flag. This will allow you to execute commands inside the container through a command prompt *as if* you had connected or ssh'd into the container.
```bash
$ docker container run -it <IMAGE_NAME>
```

You can **view a list of containers currently running on a system** using the `ls` command with the `container` command. This **does not show containers that are stopped**.
```bash
$ docker container ls
```

You can **view a list of ALL containers** whether they are **stopped or running** by using the `-a` flag with the `ls` command.
```bash
$ docker container ls -a
```

A running docker image will simply **`exit` once it has run** unless there is some process keeping it open such as the `-it` interactive process. When a container exits it does not disappear but goes into a stopped state.

You can **view a list of ALL containers, running or otherwise** and information about them using the `ps -a` command.
```bash
$ docker container ps -a
```

You can **delete a container** using the `rm` command followed by the id of the container or the container name
```bash
$ docker container rm <CONTAINER_ID/CONTAINER_NAME>
```

You can **remove multiple containers simultaneously** by space separat

You can **start a container that has stopped** using the `start` command. You can use the container name here or the `CONTAINER ID` (which is displayed when using the `ps` command.
```bash
$ docker container start <CONTAINER_NAME>
```

You can **enter a running container from outside** using the `attach` command and the name or id of the running container.
```bash
$ docker attach <CONTAINER_NAME>
```

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
eyJoaXN0b3J5IjpbLTM5MjcyMjQ5MywxNDkyODMzMTAsNDE1Nj
cyOTIwLDk5ODY3MTQzMiwxNzUzMTI5ODkyLDYxNzMxNjEwLC02
OTAzNzIwNTgsLTI4MjU0NzAxOSwxNTI1MTc1NzAwLDYwNjExNz
Y4NiwtMTM5ODAxMTk2LDIxMTgzMTkzOTcsMTcyOTU2NDg0Nyw3
ODM3MzI2NCw1NDM2NTUxNTcsLTg5ODQwNTExOCwtMTI5NDM2Mz
AyNCw5MDg5NjM2MzcsMTgwNjI3NjA1NiwyMDAyODE4NDA2XX0=

-->