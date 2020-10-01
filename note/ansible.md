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

You can **create instructions for new task or play** by using the `name` tag. The instructions contained in this task should be indented beneath it, to indicate they are part of the this task.
```yaml
- name: name of my task
  some_other_command: do something
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc3MTgzNDM5M119
-->