---
layout: page
exclude: true
title: Ansible
---

Ansible uses **playbooks** which contain the instructions used to set up nodes. Ansible is essentially just a way of converting series of commands (such as bash commands) into a nicely written `YAML` format that can be executed on multiple hosts and replicated easily.

Ansible **uses `ssh` to connect with instances** that it manages keeping it very **secure**.

## Installation

You can **install ansible** on OSX using `pip` or `pip3`.
```bash
$ pip install ansible
```

## Overview

Below is an **example Ansible file** which sets out the basic structure of an Ansible play book.
```yaml
---
- name: my play # name of the play
  hosts: webserver # name of the host to execute these tasks on
  tasks: # list of tasks be execute by this play
    - name: copy information # name of a the first task
      copy: # task command -> same as the bash copy command
        src: source/data/path
        dest: /destination/path/to
    - name: move information # name of the second task
      command: mv src/of/file /path/to/move # bash command for the second command
```

## Playbook Structure

Ansible files **must start with three `---` dashes**.
```yaml
---
# rest of my ansible playbook
```

You can **create instructions a new play** by using the `name` tag. A new play contains a set of a tasks and actions that are indented below it.
```yaml
- name: my play
```

You can **specify a host for your command** by using the `hosts` tag at the top of a play.
```yaml
- name: my play
  hosts: myserver
```

The `hosts` tag **interacts with the project's `inventory` file** which keeps a list of named managed machines in different categories. For example, the `inventory` file below sets up a `[webserver]` and `[databaseserver]` category and then points to *real* instances of those servers in an environment, for the `tasks` in a particular play to be executed on. So when the playbook specifies `hosts: webserver` any following `tasks` will be executed on all the machines in `webserver`.
```yaml
# inventory file
[webserver]
mymachine1.extension.path
mymachine2.extension.path
mymachine3.extension.path

[databaseserver]
mydvmachine1.extension.path
```

You can **create a set of tasks for a play** by using the `tasks` tag. Tasks can also use the `name` for each individual task within the play, these tasks then use specific bash commands followed by their arguments.
```yaml
- name: my play
  tasks:
    - name: do something
      # task here
```

## Local Testing

You can **create an ansible playbook that will run locally** by creating the playbook with the `hosts` pointing to your local machine.

```yaml
# my_local_playbook.yml
---

- hosts: 127.0.0.1
  tasks:
    # tasks here
```

You can **run the local playbook** using the `ansible-playbook` command.
```bash
$ ansible-playbook my_local_playbook.yml
```

## Modules

Modules are Ansible dependencies that can be used to execute functionality.

### Template

The `template` command is used for **templating files that need to be generated dynamically when deploying**.

The `template` command uses the `Jinja2` templating engine, which uses the `.j2` extension for source template files.

You **can generate a basic output from a template** by using the `src` command to load the `Jinja2` template pointing to a `dest`ination folder on the server where the file is output to.
```yaml
- name: Create /etc/file.conf from template
  template:
    src: /templates/file.j2
    dest: /etc/file.conf
```

### Command vs Shell

The `shell` and `command` modules are very similar and can often be interchangeably, *however* a key difference is that the **`command` module is not run through the shell** and so **does not have access to environment** and **cannot use bash operators** such as `>`, `<`, `|` and `&` and therefore is not much use for things like modifying files.

`shell`, however, is **less secure** than the `command` module because it runs through the `bin/sh` and is therefore influenced by the user's environment settings.
```yaml
- name: Change file (does not work)
  command: echo "some text" | tee -a file.txt
 
- name: Change file (works)
  shell: echo "some text" | tee -a file.txt
```

### Debug

When **printing the value of a variable using the `debug` module** you **must use the templated version of the variable** otherwise ansible will simply output the literal string variable name.
```yaml
- name: Set my_var
  set_fact:
    my_var: Hello

- debug:
    msg: my_var # outputs my_var literal

- debug:
    msg: "{{ my_var }}" # outputs the value of my_var
```

The output for this would be:
```
TASK [debug] ***************************************************************************************************************************************************************************
ok: [127.0.0.1] => {
    "msg": "my_var"
}

TASK [debug] **************************************
ok: [127.0.0.1] => {
    "msg": "Hello"
}
```

### Async

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

You can **check a list of asynchronous tasks for completion of all task** with a set number of overall retries by using a recursive looping solution with a task check after retrieving the `async_status` of each task in the list.
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

- name: Include recursive async check loop
  include: check_async_results.yml
```

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
eyJoaXN0b3J5IjpbLTI1NzMxMDg4NywtMjAyNDExODIxLDk4OD
Q2ODE2MiwtNTIyMjgxNjU0LDIxMjk0NzE0NCw2OTg1OTkxLDEz
NjUyNzgwMTUsMTMwNTM1Nzc2NSwtMzE1ODAzNDg4LDE4NDY2OT
M5NDAsNTcyMjU4OTIsOTAyODA3NTk3LDMwNjI3MTU3MSwyMTY0
NDE3NjUsLTMzNjM3MjM0NF19
-->