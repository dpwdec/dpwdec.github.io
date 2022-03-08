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

A docker build will fail if the command that `RUN` called `exit`s with a non-zero return code. *However*, this can be problematic when you include nested scripts as part of your docker file. For example `RUN my-complex-script.sh`. If there are points in the script where script failure should fail the build these needed to be tested and an `exit 1` called to return the correct failing exit code, otherwise the script will simply run, even with failures and return a success code of `0`. 

The example below shows an extract of a test command being run as part of a script, if this was run with the docker `RUN` command directly then its failure would stop the build, *however*, because of its inclusion inside the script this
won't happen unless the result of the `test` command is checked with the `$?` variable and an `exit 1` command called if it is non-zero.
```bash
# my-complex-script.sh
# --- snip other complex script stuff ---

npm test
if [ $? -e 1 ]; then exit 1; fi
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

If the **directory does not already exist** then `WORKDIR` will **create a new directory** on the images file system.

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

## ENV

You can **set environment variables that persist in the container environment** by using the `ENV` command. There are a number of rules for what is valid as environment variables which can be found in the [main docs](https://docs.docker.com/engine/reference/builder/#env) for `ENV`. Anything defined with `ENV` in the `Dockerfile` can be used as an environment variable by services running inside the container
```docker
ENV MY_VAR="Some variable data"
```

## ARG

You can **pass run time environment variables into a docker container during the build process** by using the `--build-arg` flag in conjunction with the `ARG` keyword in your `Dockerfile`. *Note that if you pass in a `--build-arg` without the `ARG` property defined in the file then it won't be picked up, a confusing quirk that can make you wonder why the args you are passing in are not working.* 
```bash
docker build . --build-arg MY_ARG=my_value
```

The corresponding `Dockerfile` would be:
```docker
FROM ubuntu

ARG MY_ARG

# stuff that uses the MY_ARG context down here such as a script or test run
```

You can **pass in multiple arguments** by using multiple `--build-arg` flags.
```bash
docker build . --build-arg FOO=bar --build-arg BAZ=qux --build-arg EGGS=spam
```