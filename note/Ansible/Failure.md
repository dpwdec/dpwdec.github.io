---
layout: page
exclude: true
title: Failure
---

You can **make an ansible playbook throw an exception** and fail using the `fail` command. You can use the `msg` field to output an error message on failure.
```yaml
- name: Make playbook fail
  fail:
    msg: This task failed
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbODk4ODUyNTc1XX0=
-->