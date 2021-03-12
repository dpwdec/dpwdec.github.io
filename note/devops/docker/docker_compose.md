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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgxMTc2NTc3NCwxNzY0NzY1NTE5XX0=
-->