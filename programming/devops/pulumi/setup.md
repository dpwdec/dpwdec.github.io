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