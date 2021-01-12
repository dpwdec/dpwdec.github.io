---
layout: page
exclude: true
title: Loops
---



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
eyJoaXN0b3J5IjpbLTYzNTk5NTEwOSwxOTM2MjkzNzUxLDE0Mj
AwNjc3MTMsMTc3NzgxOTAxOCwxNTI5NTczMjIsMzU5MzM0OTY0
LC0xMDc0MTk4MzY0LC0zNTMxMjQyMTYsMTQyOTg2MDkwOCwtMT
Y0NzM3OTU3MSwxNTA4MzM2MjkwLC03NTkwNjY5ODEsMTIwNDk3
NTEyOV19
-->