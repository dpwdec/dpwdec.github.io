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

You can **bundle a when condition into a failure** using the `fail_when` command.
```y
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNTE4MDE5MzcsODk4ODUyNTc1XX0=
-->