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

You can **bundle a when condition into a failure** using the `failed_when` command. However, this is less elegant as it needs to be bundled with an actual command to work, you can't just use `failed_when` on its own.
```yaml
- name: Fail
  debug: # redundant debug to allow failed_when to run
    msg: Fail
  failed_when: true
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxNzUyNzg4MCw5Njc0NDcxNTUsODk4OD
UyNTc1XX0=
-->