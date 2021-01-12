---
layout: page
exclude: true
title: Loops
---

## Sequence

You can **run a loop with a traditional start and end sequence** without the use of a list by using the `with_sequence` command with the `start` and `end` of the loop defined using `=` assignment.
```yaml
- name: Run sequence
  debug:
    msg: "{{ item }}"
  with_sequence: start=0 end=10
```

## Loop Vars

You can **rename the default name of items in an iterated list** which is `item` by default using the `loop_control` and `loop_var` properties. In the example below the name `item` is changed to `my_loop_var` instead.
```yaml
- name: Rename loop
  debug:
    msg: "{{ my_loop_var }}"
  with_items: [1, 2, 3, 4, 5]
  loop_control:
    loop_var: my_loop_var
```

## Ignore Loop Cases

You can **ignore cases in a loop** using the `failed_when` command. This works with a range of conditional operators, such as `>`, `==` etc. and will ignore any cases in iteration that meet the `failed_when` condition.
```yaml
- name: Create list
  set_fact:
    my_list: [1, 2, 3, 4, 5]

# Prints every item apart from 2

- name: Ignore 2
  debug:
    msg: "{{ item }}"
  failed_when: item == 2
```

The output for this will be:
```
TASK [debug] ***************************************************************************************************************************************************************************
ok: [127.0.0.1] => {
    "msg": "my_var"
}

TASK [debug] **************************************
ok: [127.0.0.1] => {
    "msg": "1"
}

TASK [debug] **************************************
failed: [127.0.0.1] => {
    "msg": "2"
}

TASK [debug] **************************************
ok: [127.0.0.1] => {
    "msg": "3"
}

... etc.

fatal: [127.0.0.1]: FAILED! => {"msg": "All items completed"}
```

If you **don't want the entire playbook to fail once the loop completes** you must append `ignore_errors` to these loop case command.
```yaml
- name: Ignore 2
  debug:
    msg: "{{ item }}"
  failed_when: item == 2
  ignore_errors: yes
```

## Nested Loops

You can **take the cartesian product of two sets of lists** (by nesting them) using the `with_nested` command. You can specify which component of the nested element you want to access by appending a `.` to the `item` variable. This specification is zero indexed. So items in the first list are indexed at `.0` in the second list at `.1` and so on.
```yaml
- name: create files
  debug:
    msg: "{{ item.0 }} : {{ item.1 }}"
  with_nested:
    - [1, 2, 3]
    - ["a", "b", "c"]

# => "1 : a", "1 : b", "1 : c", "2 : a", "2 : b" etc...
```



## Looping over a set of tasks

You can **loop over a set of multiple tasks with a collection** by placing the tasks you want to loop over in a separate file and using an `include` on them with the `loop` command. The items of the collection will be available inside the included file as `{{ item }}` and each item from the collection will be subbed into the included on each iteration of the loop. The outer run task would be:
```yaml
- name: Create list
  set_fact:
    my_list:
      - a
      - b
      - c

- name: Run set of tasks
  include: tasks.yml
  loop: "{{ my_list }}"
```

And the corresponding `include`d task would be:
```yaml
# tasks.yml
- name: Do something with the list items
  some_command: "{{ item }}"

- name: Do something else with list items
  another_command: "{{ item }}"

- debug:
    msg: "List item is {{ item }}"
```

You can **replace the `loop` command with the `with_items` command** and the **functionality will be identical**.

You can also **alias the names of items that you pass into the `include`d playbook** so that you don't *have* to use item by including an assignment after the name of file that is to be `include`d with the `item` property from the list assigned to a new name.
```yaml
- name: Create list
  set_fact:
    my_list:
      - a
      - b
      - c

- name: Run set of tasks
  # assignment to a new name here
  include: tasks.yml letter={{ item }}
  loop: "{{ my_list }}"
```

The corresponding include file (truncated for ease of reading):
```yaml
# tasks.yml
- debug:
    msg: "List item is {{ letter }}"
```


## Looping over tightly coupled tasks using retries

You can **loop over a group of tightly coupled tasks that may fail using retries delay** by recursively calling an `include` on a task using the `block` and `failure` commands. The example below is taken from [Jeff Martin's blog](https://dev.to/nodeselector/retrying-groups-of-tightly-coupled-tasks-in-ansible-579d). You can also define the `max_retries`, `retry_delay` and `retry_count` as facts *outside* of original recursive include.
```yaml
- name: Group of tasks that are tightly coupled
  vars:
    max_retries: "{{ 5 if max_retries is undefined else max_retries | int }}"
    retry_delay: "{{ 10 if retry_delay is undefined else retry_delay | int }}"
  block:
  - name: Increment the retry count
    set_fact:
      retry_count: "{{ 0 if retry_count is undefined else retry_count | int + 1 }}"

  - name: Some task
    setting_up:
        do_something: prerequisite action
  
    - name: Some other task
      setting_up:
        do_something: prerequisite action

  - name: Some task that might fail
    failing_task:
        some: setting

  rescue:
    - fail:
        msg: Maximum retries of grouped tasks reached
      when: retry_count | int == max_retries | int

    - debug:
        msg: "Task Group failed, let's give it another shot"

    - name: Sleep between retries
      wait_for:
        timeout: "{{ retry_delay }}" # seconds
      delegate_to: localhost
      become: false

    - include_tasks: coupled_task_group.yml
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNjg4ODQ2NjQsMTI4NTcwNTE0MywxND
U0MDc5NDYyLDE5MzYyOTM3NTEsMTQyMDA2NzcxMywxNzc3ODE5
MDE4LDE1Mjk1NzMyMiwzNTkzMzQ5NjQsLTEwNzQxOTgzNjQsLT
M1MzEyNDIxNiwxNDI5ODYwOTA4LC0xNjQ3Mzc5NTcxLDE1MDgz
MzYyOTAsLTc1OTA2Njk4MSwxMjA0OTc1MTI5XX0=
-->