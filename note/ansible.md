---
layout: page
exclude: true
title: Ansible
---

Ansible uses **playbooks** which contain the instructions used to set up nodes. These are written `YAML`.

Below is an **example Ansible file** which sets out the basic structure of an Ansible play book.
```yaml
---
- name: my play # name of the play
  tasks: # list of tasks be execute by this play
    - name: copy information # name of a the first task
      copy: # task command -> same as the bash copy command
        src: source/data/path
        dest: /destination/path/to
    - name: 
```

Ansible files **must start with three `---` dashes**.
```yaml
---
# rest of my ansible playbook
```

You can **create instructions a new play** by using the `name` tag. A new play contains a set of a tasks and actions that are indented below it.
```yaml
- name: my play
```

You can **create a set of tasks for a play** by using the `tasks` tag. Tasks can also use the `name` for each individual task within the play, these tasks then use specific bash commands followed by their arguments.
```yaml
- name: my play
  tasks:
    - name: do something
      # task here
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbNDQ5NDIyODEwLC0zMzYzNzIzNDRdfQ==
-->