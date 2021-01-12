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

You can **define custom jinja filters** using python code. To do this, First create a folder in the top level of your ansible project called `filter_plugins` and create a file in the folder called `my_filters.py`.

Next define a class in the `my_filters` file called `FilterModule` that inherits from the `Object` class. This should `return` an object that contains a dictionary of the different filter names as used in jinja code aliased to the functions that execute the filters.

```py
# my_filters.py
class FilterModule(object):
  def filters(self):
    return { 'my_filter': self.my_filter }

  def my_filter(self, x):
    return x +  ' this is my filter'
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMzc4OTY2OTgsMTE1MjMwNzk2NCwxNT
gzNTQwNTE4LC0xODU1MDIyMjQ3XX0=
-->