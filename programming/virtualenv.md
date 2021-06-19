---
title: Virtual Env
layout: page
exclude: true
---

You can **create a new virtual environment** by using the `virtualenv` command followed by the name of the environment you want to create. By convention this is simply called `env`.
```bash
$ virtualenv env
```

To **create a new virtual environment using python3** you need to use the `python3` command with the `-m` switch.
```bash
$ python3 -m virtualenv env
```

To **activate your virtual environment** use the `source` command with the path of the `ENV_NAME/bin/activate` file. This will change your console so that you are working in the virtual directory environment for your project. Once inside the virtual environment you can install dependencies and they will remain locally scoped to the directory which the environment covers.
```bash
$ source env/bin/activate
```

You can **exit a virtual environment** using the `deactivate` command.
```bash
$ deactivate
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA2NTc1NjIxNiwtMTQzMjA1MzM3MCwtMT
EzMjE2MTQ0N119
-->