---
title: Set Up
layout: page
exclude: true
---

You can **entirely set up a new Pulumi application** by using the `pulumi new` in an empty directory. This will create a valid code project in your desired language - when selected as an option - to give you everything to get started.
```bash
pulumi new
```

To **store pulumi config locally** use the `login` command with the argument `file://~`. By default pulumi tries to store its config on the cloud hosted pulumi servers.
```bash
pulumi login file://~
```

You can **run a pulumi command on a different directory from your current directory** by passing in a path to the directory where you pulumi code is using the `-C` or `--cwd` flags.
```bash
pulumi up --cwd ./path/to/pulumi/project
```