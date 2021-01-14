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

There is also a subtlety in the order of evaluation. The evaluation process of `when` stops as soon as a false condition is found. In the example below the second `true` condition does *not* get evaluated because the `when` commands evaluation stops being evaluated when it encounters its first `false`. This allows you to do useful things with uninitialised variables that might break upon evaluation which also rely on conditions further up the chain. 
```yaml
- name: Do something
  debug:
    msg: Some message
  when:
    - false    
    - true # this never gets evaluated
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQxNzQ2ODIzN119
-->