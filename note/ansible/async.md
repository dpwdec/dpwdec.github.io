---
layout: page
exclude: true
title: Async
---

Ansible executes in synchronous single threaded manner by default. *However*, it *is* possible to write **asynchronous style tasks in ansible** that send a set of requests off in a "fire and forget" manner, or `poll` the results of the requests for completion.

You can **send an asynchronous requests** by adding the `async` and `poll` properties to `command`s. The `async` property takes a number in seconds that represents the time which the request will run before timing out. The `poll` property represents a time interval in seconds to wait and check the status of the request repeatedly until it times out. Confusingly **ansible will block execution until the request times out or is completed** so its not entirely clear what the advantage of making a request like this asynchronously is apart from perhaps freeing up load on the machine which is executing it by sleeping.
```yaml
- name: Make async request
  command: example-long-running-api-request
  async: 30
  poll: 3
```

You can **run tasks in a truly asynchronous fashion** by setting the `poll` property to `0`. Ansible will the immediately move onto the next task and the tasks will just run until they complete, fail or timeout.
```yaml
- name: Make async request
  command: example-long-running-api-request
  async: 30
  poll: 0

- name: Some other task
  ...
```

You can **check the status of asynchronous tasks** using the `async_status` module. You can use this like you would promise resolution of asynchronous tasks in other languages. For example, you may want to send a `poll = 0` asynchronous task off, execute some further ansible tasks while the original asynchronous task is executing and then poll the result of that original task at the later point when it is needed. The `async_status` command takes an `ansible_job_id` from the original async request command which means the command needs to be logged with `register` when it is executed. When `async_status` executes it will run synchronously, blocking execution for the number of `retries` and the `delay` interval between retries until the asynchronous task times out, fails or completes.
```yaml
- name: Make async request
  command: example-long-running-api-request
  async: 30
  poll: 0
  register: async_task

- name: Some other task
  debug:
    msg: Imagine I am executing another task

# more tasks here

- name: Poll async task result
  async_status:
    jid: "{{ async_task.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 100
  delay: 10
```

If you want to **poll a list of asynchronous tasks until all of them complete** you can use the `with_items` command with `async_status` and wait until each registered job completes *however*, this unfortunately **executes synchronously** and so each task will be checked for the number of specified retries with the delay before moving onto the next async item in the list to check, instead of checking all items for resolution then retrying and checking all items in the list until all have resolved. However, this still can be useful for simple sets of asynchronous tasks that are expected to resolve quickly and are interdependent. In the example, if the first task does not resolve the `async_status` loop will check that task `100` times and then move onto the next task and so on, checking each one `100` times.
```yaml
- name: Set addresses
  set_fact:
    addresses:
      - 1.2.2.10
      - 6.1.3.10
      - 9.5.6.10

- name: Make multiple async requests
  command: example-long-running-api-request --with-address {{ item }}
  async: 30
  poll: 0
  register: async_tasks # list of async tasks
  with_items: "{{ addresses }}"

- name: Poll async task result
  async_status:
    jid: "{{ async_task.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 100
  delay: 10
  with_items: "{{ async_tasks }}"
```

You can **check a list of asynchronous tasks for completion of all task** with a set number of overall retries by using a recursive looping solution with a task check after retrieving the `async_status` of each task in the list. In the example below the async tasks are passed into a recursive task that retrieves the current async statuses of the tasks and then uses the jinja query language to check that all tasks are completed. It then uses the `fail` and `rescue` clauses to recursively call itself until the `max_retries` is reached. On each check it sleeps for `10` seconds.
```yaml
# main.yml
- name: Set addresses
  set_fact:
    addresses:
      - 1.2.2.10
      - 6.1.3.10
      - 9.5.6.10

- name: Make multiple async requests
  command: example-long-running-api-request --with-address {{ item }}
  async: 30
  poll: 0
  register: async_tasks # list of async tasks
  with_items: "{{ addresses }}"

- name: Initialise retries
  set_fact:
    max_retries: 10
    retry_count: 0

- name: Include recursive async check loop
  include: check_async_results.yml
```

The corresponding include file which runs the recursive loop that checks for task completion.
```yaml
# check_async_results.yml
---

- name: Group of tasks that are tightly coupled
  block:
  - name: Increment the retry count
    set_fact:
    retry_count: "{{ retry_count | int + 1 }}"

  - name: Poll async task result
    async_status:
      jid: "{{ item.ansible_job_id }}"
    with_items: "{{ async_tasks }}"
    register: async_task_result

  - name: Check all jobs finished
    set_fact:
      finished_status: "{{ async_task_result
      | to_json
      | from_json
      | json_query('results[*].finished')
      | select('equalto', 1)
      | list
      | length == async_task_result | length }}"

   - name: Fail unfinished instance status requests
     fail:
       msg: Not all instance requests returned yet
     when: finished_status == false
  rescue:
  - fail:
     msg: Maximum retries of instance status request checks reached
    when: retry_count | int > max_retries | int

  - name: Sleep between retries
    wait_for:
      timeout: 10  # seconds
    delegate_to: 127.0.0.1

  - include_tasks: check_async_results.yml
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA0Mzc3ODEwNF19
-->