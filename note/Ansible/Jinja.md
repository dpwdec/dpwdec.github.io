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

## Select

You can **use comparative functions** with the `select` filter, such as `greaterthan` or `equalto`. T
```yaml
- name: Select greaterthan
  debug:
    msg:
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

You **can then use the filter in your ansible code** as you would any other jinja filter.
```yaml
- name: Use my filter
  debug:
    msg: "{{ item | my_filter }}"
  with_items: [ 'a', 'b', 'c' ]

# => a this is my filter 
# => b this is my filter
# => c this is my filter
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk5MTk4NTM5OSwzMzE0OTEyMywtMTE3ND
cwOTAxMiwxMTUyMzA3OTY0LDE1ODM1NDA1MTgsLTE4NTUwMjIy
NDddfQ==
-->