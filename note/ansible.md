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

You can **create instructions for new task or play** (as Ansible likes to call them) by using the `name` tag. The instructions within this task should be indented to indicated
```yaml
- name: name of my task
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMzNTg2NDgyXX0=
-->