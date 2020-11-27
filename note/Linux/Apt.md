---
layout: page
exclude: true
title: Apt
---

APT stands for **Advanced Package Tool** and is a command line system build on top of the Debian Linux **dpkg** system to allowing you install packages.

## Get

You can **update the APT system** using the `update` command. APT knows what packages are available for install based on its own database of potential installations., if its not updated you won't be able to find packages or know if newer versions are available.
```bash
$ apt-get update
```

You can **update all packages managed by APT to the latest version** by using the `upgrade` command.
```bash
$ apt-get upgrade
```

You can **update a specific package** by submitting the package name *after* the `upgrade` command.
```bash
$ apt-get upgrade <PACKAGE_NAME>
```

## Cache

You can **search through the database of packages** using the `search` command. This will search package names and descriptions about the packages. This is a looser search method that can allow you to **search for packages without knowing the exact name of what you're looking for**.
```bash
$ apt-cache search <SEARCH_TERM>
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbNTk3NTI2NDE5LC03OTg1MDQ2NzUsMTY1NT
U1MzE4NF19
-->