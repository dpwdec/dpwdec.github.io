---
layout: page
exclude: true
title: When
---

You can **evaluate a single command against multiple conditions** by listing boolean expressions under the `when` command with `-` hyphens, the command will **only run if all conditions evaluate to true**.  In the example below the `debug` command will *not* execute because not all conditions are true.
```yaml
- name: Do something
  debug:
    msg: Some message
  when:
    - true
    - false
```

There is also a subtlety in the order of evaluation. This process stops evaluation of `when` as soon
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MDAxMTA1ODJdfQ==
-->