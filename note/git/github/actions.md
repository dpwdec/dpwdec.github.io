---
title: Github Actions
layout: page
exclude: true
---

## Checkout

You can **checkout the repos code upon which your code is running** using the `checkout` action.
```yaml
- name: checkout code
  uses: actions/checkout@v2
```

## Scheduled Jobs

Scheduled jobs are **not guaranteed to run** *or* **guaranteed to run on time**. When a scheduled job is called a request is made to Github actions machines for the job to run and is run once a node is free. This can vary the time from 3-10 minutes but it can be as long as an hour and can sometimes not be run at all if the lag time is long enough. More information [here](https://upptime.js.org/blog/2021/01/22/github-actions-schedule-not-working/).


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEwMDU2NjU1MywtMTgwMDAxMDY3Ml19
-->