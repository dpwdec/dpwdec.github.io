---
title: Bind Mounts
layout: page
exclude: true
---

**Bind Mounts** allow you to link locations on the host file system with desinations inside the container and persist data between them.

You can **link a container to a bind mount when it starts** with the `run` command by using the `-v` / `--volume` flags or the `--mount` flag.

The **bind mount takes an absolute path on the host machine** to specify the location of the mount. You can **easily get this location** by interpolating the `pwd` command into the path.

If using the `-v` or `--volume` flag you can specify the exact path, separated by a `:` with where to point that path on the container. The example below will mount a `data` folder on the host file system to a `data` folder inside the root of the container. *The CLI will infer that you want a mount if you pass a valid host file system path to this command*.
```bash
docker run -it --volume "$(pwd)"/data:/data
```

If using the `--mount` flag you **must specify the `type` of the container** as `bind` - otherwise the CLI will complain because it will assume you want a volume and try to parse the path as a volume name instead of a filesystem location - along with the `source` and `destination` values.
```bash
docker run -it --mount type=bind,source="$(pwd)"/data,destination=/data
```

You can **set a bind mount as read only** using the `readonly` flag.

You **cannot populate a bind mount from a container** - the host file system will always take precedence. For example, if I create a container with a folder, called `internal`, on it that contains some files, then create another empty folder on my host machine's file system, called `external`, and mount that folder to the container, then the contents of `internal` will be entirely obscured inside the container. *It is possible to achieve populating a data store from a container using volumes however, see the volumes section for info*.