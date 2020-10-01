---
layout: page
exclude: true
title: Ansible
---

Ansible uses **playbooks** which contain the instructions used to set up nodes. These are written `YAML`.

Ansible files **must start with three `---` dashes**.
```yaml
---
# rest of my ansible playbook
```

You can **create instructions a new play** by using the `name` tag. A new play contains a set of a tasks and actions that are indented below it.
```yaml
- name: my play
```

You can **create a set of tasks for a play** by using the `tasks` tag. Tasks can also use the `name` for each individual task within the play, these tasks then use specific indicator
```yaml
- name: my play
  tasks:
    - name: do something
      # task here
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg5MzI3ODQ1NiwtMzM2MzcyMzQ0XX0=
-->