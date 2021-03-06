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

There is also a subtlety in the order of evaluation. The evaluation process of `when` stops as soon as a false condition is found. In the example below the second `true` condition does *not* get evaluated because the `when` commands evaluation stops being evaluated when it encounters its first `false`. 
```yaml
- name: Do something
  debug:
    msg: Some message
  when:
    - false    
    - true # this never gets evaluated
```

This allows you to **do useful things with uninitialised variables that might break upon evaluation** which also rely on conditions further up the chain. In the example below, if the `some-CLI` command fails it will return an empty string, and so, when we want to `Do Something` with the `property` component of the expected JSON object it will fail when trying to evaluate that property for a specific state, in this case, `done`. By checking that `json_cli_result` is not empty first we can ensure that the evaluation on `json_cli_property` works, if `json_cli_result` is indeed empty then the value of property is never evaluated and causes no errors.
```yaml
- name: Load some JSON
  command: some-CLI-that-gets-JSON
  register: json_cli_result

- name: Get some JSON property
  set_fact:
    json_cli_property: "{{ json_cli_result.property }}"
  when: json_cli_result != ''

- name: Do something with JSON property
  command: do-something-with "{{ json_cli_property }}"
  when:
    - json_cli_result != ''
    - json_cli_property == 'done'
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1OTU1OTM5MywxNDE3NDY4MjM3XX0=
-->