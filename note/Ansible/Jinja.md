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


<!--stackedit_data:
eyJoaXN0b3J5IjpbODkzNTM0NTc5LDE1ODM1NDA1MTgsLTE4NT
UwMjIyNDddfQ==
-->