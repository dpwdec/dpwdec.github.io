---
layout: page
exclude: true
title: Ansible
---

Ansible uses **playbooks** which contain the instructions used to set up nodes. Ansible is essentially just a way of converting bash commands into a nicely written `YAML` format.

Ansible **uses `ssh` to connect with instances** that it manages keeping it very **secure**.

## Overview

Below is an **example Ansible file** which sets out the basic structure of an Ansible play book.
```yaml
---
- name: my play # name of the play
  hosts: webserver # name of the host to execute these tasks on
  tasks: # list of tasks be execute by this play
    - name: copy information # name of a the first task
      copy: # task command -> same as the bash copy command
        src: source/data/path
        dest: /destination/path/to
    - name: move information # name of the second task
      command: mv src/of/file /path/to/move # bash command for the second command
```

## Playbook Structure

Ansible files **must start with three `---` dashes**.
```yaml
---
# rest of my ansible playbook
```

You can **create instructions a new play** by using the `name` tag. A new play contains a set of a tasks and actions that are indented below it.
```yaml
- name: my play
```

You can **specify a host for your command** by using the `hosts` tag at the top of a play.
```yaml
- name: my play
  hosts: myserver
```

The `hosts` tag **interacts with the project's `inventory` file** which keeps a list of named managed machines in different categories. For example, the `inventory` file below sets up a `[webserver]` and `[databaseserver]` category and then points to *real* instances of those servers in an environment, for the `tasks` in a particular play to be executed on. So when the playbook specifies `hosts: webserver` any following `tasks` will be executed on all the machines in `webserver`.
```yaml
# inventory file
[webserver]
mymachine1.extension.path
mymachine2.extension.path
mymachine3.extension.path

[databaseserver]
mydvmachine1.extension.path
```

You can **create a set of tasks for a play** by using the `tasks` tag. Tasks can also use the `name` for each individual task within the play, these tasks then use specific bash commands followed by their arguments.
```yaml
- name: my play
  tasks:
    - name: do something
      # task here
```

## Commands

### Template

The `template` command is used for templating linux `.conf` 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzA2MjcxNTcxLDIxNjQ0MTc2NSwtMzM2Mz
cyMzQ0XX0=
-->