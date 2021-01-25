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

You can **uninstall a package** using the `remove` command,
```bash
$ apt-get remove <PACKAGE_NAME>
```

You can **uninstall a package AND remove any configuration files** using the `purge` command. This is useful if you've messed up the configuration of a file and want to completely start from scratch.
```bash
$ apt-get purge <PACKAGE_NAME>
```

You can **automatically say "yes" to all installation prompts when installing** by using the `-y`, `--yes` or `--assume-yes` flags.
```bash
$ apt-get purge <PACKAGE_NAME>
```

## Cache

You can **search through the database of packages** using the `search` command. This will search package names and descriptions about the packages. This is a looser search method that can allow you to **search for packages without knowing the exact name of what you're looking for**.
```bash
$ apt-cache search <SEARCH_TERM>
```

You can **search only package names specifically** using the `pkgnames` command.
```bash
$ apt-cache pkgnames <SEARCH_TERM>
```

You can **see data about a package** such as version, dependencies etc. using the `showpkg` command,
```bash
$ apt-cache showpkg
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUyNzAyMzIzOCwtNDI0OTU5NzE2LC05MT
Y1NTczNjUsLTc5ODUwNDY3NSwxNjU1NTUzMTg0XX0=
-->