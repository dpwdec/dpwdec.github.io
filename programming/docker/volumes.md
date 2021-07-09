---
title: Volumes
layout: page
exclude: true
---

Docker volumes allow you to **persist data between container executions**. They are docker's preferred way of working with data.

**Importantly!** docker volumes are **entirely managed by docker**. This means that they are not directly accessible or reachable on your host machines file system and are instead sequestered in a linux VM. This can be useful, as it means *the data persisted by docker is entirely separate from the file system that the container is running on*.

**Multiple containers can access a single volume at once** while they are running.

## Volume Management

You can **create a volume** using the `volume create` command.
```bash
docker volume create <VOLUME_NAME>
```

You can **list existing volumes** with the `ls` command.
```bash
docker volume ls
```

You can **view data about a volume** using the `inspect` command.
```bash
docker volume inspect <VOLUME_NAME>
```

## Container Volumes

You can **link a container to a volume when it starts** with the `run` command by using the `-v` / `--volume` flags or the `--mount` flag.

If using the `-v or `--volume` flag you **submit a list of three `:` colon separated fields**. These are

1. The name of the volume *If you want to specify a hosted path on your OS then you want bind mounts which can also be specified by submitting the path in place here*
2. The path where the volume is mounted on the container
3. Optional comma-separated configuration settings

```bash
docker run --volume <VOLUME_NAME>:<PATH_ON_CONTAINER> <IMAGE_ID>
```

If using the `--mount` flag you can submit options as key value pairs after the flag. There are

- `type`: can be `bind`, `volume` or `tmpfs` *This is also the default type across other invocations of the `--mount` command*
- `source` or `src`: the name of the volume
- `destination`, `dst` or `target`: the path on the container to be mounted to
- `readonly`: allows you to control whether the container has write permissions to the volume
- `volume-opt`: allows you to define other volume specific options as further key pairs

docker run --mount type=volume,src=<VOLUME_NAME>,destination=<CONTAINER_PATH>

You can **access data in a volume** by spinning up a docker container with that volume mounted in the file system of the container. In the example below, if I had already added data to the `my-vol` volume, then when the container starts it will have access to any data in that volume in the `/data` folder at the root of the container. *The mounted folder is always the same as the root of the volume*.
```bash
docker run -it --mount src=my-vol,destination=/data ubuntu:16.04
```

If you **specify a volume that has not been create** it will be created automatically when starting the container.

You can **get files out from a volume onto your local file system** by using the `docker cp` command in conjunction with a container that has access to that volume.

1. Spin up a container with the desired volume mounted to its file system
2. Copy the files out of the container onto your local file system using the `cp` command.

The example below starts a container with `my-vol` mounted (which contains some previously created data in the form of `.txt` file) and then the `cp` command is used to copy that file out.

```bash
docker run --mount src=my-vol,destination=/data --name data-container ubuntu:16.04
docker cp data-container:/data/my_file.txt .
```

You can **run a volume as read only** simply by including the `readonly` flag with no value, or `ro` when using the `--volume` command.
```bash
# using mount
docker run --mount src=my-vol,destination=/data,readonly --name data-container ubuntu:16.04
# using volume
docker run --volume my-vol:/data:ro --name data-container ubuntu:16.04
```

You can **see how a mount is working with a container** from the `Mounts` section of the output from running `docker inspect`.

You can **populate data from a container to a volume** by mounting a *new* volume to a folder on a container that contains data. *This only works if it is a brand new volume*, otherwise the data will not populate and the existing volume will overwrite the container's internal volume. For example, if I have a container with an `internal` directory with some data in and I run...
```bash
docker run --mount src=new-volume,destination=/internal ubuntu:16.04
```

Then the data that was in the `internal` folder on the container will be avialable on the volume.
