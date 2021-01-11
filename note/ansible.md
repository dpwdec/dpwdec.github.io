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

You can **check the status of asynchronous tasks** using the `async_status` module. You can use this like you would promise resolution of asynchronous tasks in other languages. For example, you may want to send a `poll = 0` asynchronous task off, execute some further ansible tasks while the original asynchronous task is executing and then poll the result 


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMjYyODUzNjgsMTMwNTM1Nzc2NSwtMz
E1ODAzNDg4LDE4NDY2OTM5NDAsNTcyMjU4OTIsOTAyODA3NTk3
LDMwNjI3MTU3MSwyMTY0NDE3NjUsLTMzNjM3MjM0NF19
-->