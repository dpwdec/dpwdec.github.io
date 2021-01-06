---
layout: page
exclude: true
title: Ansible
---

Ansible uses **playbooks** which contain the instructions used to set up nodes. Ansible is essentially just a way of converting series of commands (such as bash commands) into a nicely written `YAML` format that can be executed on multiple hosts and replicated easily.

Ansible **uses `ssh` to connect with instances** that it manages keeping it very **secure**.

## Installation

You can **install ansible** on OSX using `pip` or `pip3`.
```bash
$ pip install ansible
```

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

## Local Testing

You can **create an ansible playbook that will run locally** by creating the playbook with the `hosts` pointing to your local machine.

```yaml
# my_local_playbook.yaml
---

- hosts: 127.0.0.1
  tasks:
    # tasks here
```



## Modules

Modules are Ansible dependencies that can be used to execute functionality.

### Template

The `template` command is used for **templating files that need to be generated dynamically when deploying**.

The `template` command uses the `Jinja2` templating engine, which uses the `.j2` extension for source template files.

You **can generate a basic output from a template** by using the `src` command to load the `Jinja2` template pointing to a `dest`ination folder on the server where the file is output to.
```yaml
- name: Create /etc/file.conf from template
  template:
    src: /templates/file.j2
    dest: /etc/file.conf
```

### Command vs Shell

The `shell` and `command` modules are very similar and can often be interchangeably, *however* a key difference is that the **`command` module is not run through the shell** and so **does not have access to environment** and **cannot use bash operators** such as `>`, `<`, `|` and `&` and therefore is not much use for things like modifying files.

`shell`, however, is **less secure** than the `command` module because it runs through the `bin/sh` and is therefore influenced by the user's environment settings.
```yaml
- name: Change file (does not work)
  command: echo "some text" | tee -a file.txt
 
- name: Change file (works)
  shell: echo "some text" | tee -a file.txt
```



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMjMxODUyMjksNTcyMjU4OTIsOTAyOD
A3NTk3LDMwNjI3MTU3MSwyMTY0NDE3NjUsLTMzNjM3MjM0NF19

-->