---
layout: page
exclude: true
title: Jinja
---

Jinja templating can also be used in ansible and allows you to use the more programmatic functionality of the jinja engine to processes ansible data, such as filters, templating etc.

Jinja can be used in python, template files, web pages *or* ansible templates. The examples below don't distinguish but the jinja concepts stay the same.

## Range

You can **generate a list in a range** using the `range` filter with the start and end of the list as arguments.
```yaml
- name: Create list
  set_fact:
    my_list: "{{ range(0, 10) }}"

# => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Select

You can **use comparative functions** with the `select` filter, such as `greaterthan`, `lessthan` or `equalto`. These must be passed into select inside `''` apostrophes followed by the value they are comparing against.
```yaml
- name: Greater than
  debug:
    msg: "{{ item }}"
  with_items: "{{ my_list | select('greaterthan', 5) | list }}"
  vars:
    my_list: [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

# => 6, 7, 8, 9
```

## JSON Query

You can **destructure JSON** using the `json_query` filter in jinja.

You can **match arrays of objects** using a `*` character and pull out nested properties of that array of objects into a new array. In the example below the `*` matches with every element in the `property` array property of `object` and then gets all the `x`s from those objects.
```yaml
- name: get nested json
  debug:
    msg: "{{ item }}"
  with_items: "{{ object | json_query('property[*].x') }}"
  vars:
    object: { property: [ { x: 1 }, { x: 2 } ] }
```

## If statements

You can **create if statements in a jinja template** using the `{% %}` brackets. In the example below we template a `Data` field if the `number` variable is even otherwise we don't template anything.
```
Type: {{ number }}
{% if number % 2 == 0 %}
Data: Even
{% end if %}
Environment: OS
```

You can **remove white space and new line generation** between jinja if statements that don't get templated by adding `-` signs before or after the `{% %}` statement markers to remove different amounts of white space. Differing bracket markers such as `{%- %}`, `{% -%}` mean The example below will strip out all newline and blank spaces when the if statement is not templated.
```
{% if number % 2 == 0 -%}
Data: Even
{% end if -%}
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
eyJoaXN0b3J5IjpbNjc4ODQyMTkxLDE2MjM2MjU3MjYsLTE1Mz
kzNDE5NTcsLTEwMjk2OTc5ODBdfQ==
-->