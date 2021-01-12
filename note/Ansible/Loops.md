---
layout: page
exclude: true
title: Loops
---

## Looping over a set of tasks

You can **loop over a set of multiple tasks with a collection** by placing the tasks you want to loop over in a separate file and using an `include` on them with the `loop` command. The items of the collection will be available in
```yaml

```

## Looping over tightly coupled tasks using reties

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
eyJoaXN0b3J5IjpbMTkzMjk3NTE1NCwxNTA4MzM2MjkwLC03NT
kwNjY5ODEsMTIwNDk3NTEyOV19
-->