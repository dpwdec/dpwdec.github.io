---
title: Docker Compose
layout: page
exclude: true
---

You can **network together multiple containers** to create a single service using the **docker compose** utility. Docker composition is defined using a `docker-compose.yml` file.

You can **point a docker compose service at a `Dockerfile` on the local file system to `build` from** by using the `build` command and a path to the directory containing the target `Dockerfile`.
```yaml
services:
  my_service:
    build: ./path/to/directory/
```

You can **build all images associated with a docker service composition** by using the `build` command. This will build all `Dockerfile`s that are referenced in the `docker-compose.yaml` file.
```bash
$ docker compose build
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTkxMDM2OTEzLDE3NjQ3NjU1MTldfQ==
-->