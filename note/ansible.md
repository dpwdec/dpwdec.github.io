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
- name: name of my task
```

You can **create a set of tasks for a play** by using the `tasks` tag.
```yaml

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMzNjM3MjM0NF19
-->