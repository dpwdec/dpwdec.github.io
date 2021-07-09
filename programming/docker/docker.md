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

Use an **alpine image** if possible as they are very small.

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

You can **give a docker image a name at the same as building it** by using the `-t` or `--tag` flags. The following would create an image called `my_image` in the images list.
```bash
$ docker build . -t my_image 
```

## Images

You can **show a list of images on your system** using the `images` command.
```bash
$ docker images
```

You can **delete an image** using the `rmi` command - which stands for "remove image" - followed by the name or image ID.
```bash
$ docker rmi <IMAGE_ID>
```

You can **tag an image** with the `repository` and `tag` properties by using the `tag` command followed by the image identifier and then the repository and tag, with the tag separated by a `:` colon.
```bash
$ docker tag <IMAGE_ID> <IMAGE_REPO_NAME>:<IMAGE_TAG>
```

For example, if I wanted to push an image to the `blob` repository of the `sanchez.utsunomiya` repo with the tag `v1`.
```bash
$ docker tag <IMAGE_ID> sanchez.utsunomiya/blob:v1
```

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

You can **make your container not exit once it runs** by running it in **detached mode** using the `-d` flag.
```bash
$ docker container run -d <IMAGE_NAME>
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

You can **remove multiple containers simultaneously** by space separating the container identifiers that you want to remove.
```bash
$ docker container rm <CONTAINER_ID_1> <CONTAINER_ID_2> <CONTAINER_ID_3> # etc.
```

You can **start a container that has stopped** using the `start` command. You can use the container name here or the `CONTAINER ID` (which is displayed when using the `ps` command.
```bash
$ docker container start <CONTAINER_NAME>
```

You can **enter a running container from outside** using the `attach` command and the name or id of the running container.
```bash
$ docker attach <CONTAINER_NAME>
```

You can **go inside a container that is already running** in a similar manner to ssh logging into an external machine. This allows you access the command line of a container that is currently executing and sitting idly but not stopped by using the `exec` command.
```bash
$ docker exec -i -t <CONTAINER_NAME> bash
```

### Ports

You can **map ports on a local machine to ports on a docker container** using the `-p` flag when running the container followed by the port on your local machine and the port on the docker container separated by a `:` colon. The example below maps the ports `1234` on the local machine to port `8080` on the running container. This means that any traffic fired from your local machine to `localhost:1234` will return a response from the running container.
```bash
$ docker container run -p 1234:8080 <CONATINER_NAME>
```

The `-p` flag overrides `EXPORT` commands defined in the docker file.

You can **show the output of scripts that are run in docker** by calling them from a bash script. In the example below the `Dockerfile` would use `CMD [ "sh", "script.sh" ]` which uses the `node` command to call a script, the `console.log` commands of which will show their output.
```bash
#!/bin/bash
echo "Output from Script"
node my-script.js
```

### External Services

You can **access the localhost address of the machine hosting a container** by using the `host.docker.internal` address within the container. For example, if I was hosting a proxy service inside a container such that I make a request on my local machine that roots the request to the proxy service inside the container which then needs to make a further request to another port on the local machine outside of the container, this can be done with the `host.docker.internal` address. This can be treated as a stand in for `localhost` when referring to the host machine. The example below shows a command executed from within a container if I wanted to access a service on the host machine at `localhost:8000` from *within* the container.
```bash
$ curl http://host.docker.internal:8000
```

## Copying

You can **copy a file from your host file system to a docker container** using the `docker cp` command followed by the target file and then the container ID followed by a `:` colon and the path to the where you want the file copied to.
```bash
docker cp ./path/on/host <CONTAINER_ID>:/path/on/container/
```

You can **copy a file from inside a docker container to your host file system** by reversing the above process.
```bash
docker cp <CONTAINER_ID>:/path/on/container/ ./path/on/host 
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

You can **log in to docker hub** using the `login` command.
```bash
$ docker login
```

You can **push an image to docker hub** by using the `push` command with your username and the repository path (which should match the image name) as an argument.
```bash
$ docker push <USER_NAME>/<REPOSITORY_NAME>
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMTEyNzAzNjAsMTg2MDE2ODk3NSw5Nj
g5NDEyODcsLTIyMzUwMjI1MCwtMTc3MDg2NTI5OSwtOTA2MDQy
MTYzXX0=
-->