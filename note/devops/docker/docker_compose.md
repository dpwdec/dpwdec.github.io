---
title: Docker Compose
layout: page
exclude: true
---

You can **network together multiple containers** to create a single service using the **docker compose** utility. Docker composition is defined using a `docker-compose.yml` file.

You can **point a docker compose service at a `Dockerfile` on the local file system to `build` from** by using the `build` command and a path to the directory containing the target `Dockerfile`.
```yaml
# docker-compose.yml
services:
  my_service:
    build: ./path/to/directory/
```

You can **build all images associated with a docker service composition** by using the `build` command. This will build all `Dockerfile`s that are referenced in the `docker-compose.yaml` file. It's important to note that you **must re-run this command before starting your service** each time a `Dockerfile` changes.
```bash
$ docker compose build
```

You can **start a service composed of docker containers** (and spin up / network all the associated containers) using the `up` command. This command **does NOT rebuild docker images** when run.
```bash
$ docker compose up
```

You can **keep a container that is initialised using docker compose running** by using the `tail` command as an initial execution task for the container.
```yaml
  my_service:
    image: ubuntu
    command: tail -F anything
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcwNTQ5NTQ1MCwxMzcyODI1OTUyLDE3Nj
Q3NjU1MTldfQ==
-->