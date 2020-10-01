---
layout: page
exclude: true
title: Ansible
---

Ansible uses **playbooks** which contain the instructions used to set up nodes. Ansible is essentially just a way of converting bash commands into a nicely written `YAML` format.

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

The `hosts` tag **interacts with the `inventory` file** to find named hosts.

You can **create a set of tasks for a play** by using the `tasks` tag. Tasks can also use the `name` for each individual task within the play, these tasks then use specific bash commands followed by their arguments.
```yaml
- name: my play
  tasks:
    - name: do something
      # task here
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYwMDA3MjQwMSwtMzM2MzcyMzQ0XX0=
-->