---
layout: page
exclude: true
title: Jinja
---

Jinja templating in ansible allows you to use the more programmatic functionality of the jinja engine to processes ansible data, such as filters, templating etc.

## Range

You can **generate a list in a range** using the `range` filter with the start and end of the list as arguments.
```yaml
- name: Create list
  set_fact:
    my_list: "{{ range(0, 10) }}"

# => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Defining Custom Filters

You can **define custom jinja filters** using python code. To do this.

1. Create a folder in the top level of your ansible project called `filter_plugins`.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE1MjMwNzk2NCwxNTgzNTQwNTE4LC0xOD
U1MDIyMjQ3XX0=
-->