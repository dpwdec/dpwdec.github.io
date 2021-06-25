---
title: Cargo
layout: page
exclude: true
---

You can **interact with CLI arguments for a rust application you are building, but still run using cargo** by passing a trailing `--` double hyphen to the `run` commands followed by your other CLI arguments.
```bash
cargo run -- -d -t --data file.txt
```

## Builds

You can **build a release version of your project as a binary** by using the `--release` flag with the `build` command. The executable binary will be available in the `target/release/` directory.
```bash
cargo build --release
```

### Linux

To **build a rust application in a linux environment**, for example, as part of a linux docker container. You need to install the `build-essential` package.
```bash
apt install build-essential
```

A **simple docker container for building a linux rust image** would be...
```docker
FROM ubuntu:16.04

RUn apt update

Run apt install -y curl

RUN curl https://sh.rustup.rs -sSf | bash -s -- y

ENV PATH="/root/.cargo/bin:${PATH}"

RUN apt install build-essential -y

# environment is set up for building
# do other build stuff here
```