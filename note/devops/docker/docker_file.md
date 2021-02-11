---
title: Dockerfile
layout: page
exclude: true
---

The `Dockerfile` allows you **to define a blueprint for an image**. Capatilization of docker directives like `FROM` and `RUN` is **not mandatory** however it is **best practice**.

You can **base your docker image on an existing docker image** using the `FROM` command followed by the name of the image (this can be as it appears on services like dockerhub).
```docker
FROM <IMAGE_NAME>
```

## Run

You can **customise your image** by using the `RUN` command to execute a command in the environment that the image is based on. In the example below the dockerfile starts from the ubuntu environment and installs python.
```docker
FROM ubuntu
RUN apt-get install -y python3
```

## Label

You can **add metadata to your docker image** by using the `LABEL` directive.
```docker
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

The `MAINTAINER` directive has been **deprecated**. However if you can **add meta to your dockerfile** using the `LABEL` directive which takes a key-value pair assigned with an `=`.
```docker
LABEL maintainer="my_name@some-website.com"
```

## Copy

You can use the **copy files from an external source to your docker container** using the `COPY` directive. This takes the file source on the machine building the image followed by the destination *inside* the targeted container image.
```docker
COPY my/local/file.txt some/container/directory
```

`COPY` will not copy the `Dockerfile` into the image.

## Workdir

You can **set a working directory inside a container** using the `WORKDIR` command. This takes a path as an argument which subsequent `RUN`, `COPY`, `CMD` etc. commands will run from. If the directory specified doesn't exist it in the container it will be created.
```docker
WORKDIR /usr/my/working/directory
```

You can **call the `WORKDIR` command multiple times**, each time it will create the new working directory *relative* to the last call. The example below outputs the working directory `/usr/working/directory/`.
```docker
WORKDIR /usr
WORKDIR working
WORKDIR directory
```

## Expose

You can **expose ports on your docker container** so that it can listen for external traffic using the `EXPOSE` directive.
```docker
EXPOSE 8080
```

The intention of `EXPOSE` is as documentation for the user of the image to show them which ports this docker image will output data from. It is the system that starts a container based on this image that will have to link one of its internal ports to the port on the container to listen for information.

## CMD

You can **run a command when your docker image starts** by using the `CMD` directive. There can **only be one** of these in a `Dockerfile`. This command only runs once the docker image actually starts, where as the `RUN` command is committed to the image as it builds. `CMD` can be written using `shell` form *or* `json` form.
```docker
CMD sh my_script.sh        # shell form
CMD ["sh", "my_script.sh"] # json form
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkxMTUxNDA5MiwxODQ3Nzg0ODQwLC0xMz
Y4NjA4NTQ0XX0=
-->