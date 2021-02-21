---
title: Github Actions
layout: page
exclude: true
---

## Checkout

Checkout properties and documentation can be found [here](https://github.com/actions/checkout).

You can **checkout the code from the repo on which your github action CI job is running** using the `checkout` action. This adds the repos content to the containerized file system that is running the CI job. You can call subsequent actions on the code *as if* you were in the root of that file system. The `checkout` action downloads the code in a **detached head** state, so **commands like `git diff` with previous commits do not work by default** because of this detached head state.
```yaml
- name: checkout code
  uses: actions/checkout@v2
```

You can **include previous commit history in your checkout** by using the `fetch-depth` property on `checkout`. This defaults to `1`, hence the detached head behavior observed above. If set it `0` it will **checkout ALL commits for all branches**. For example, if you wanted to checkout the current commit and the previous commit - to `git diff` them - you would use a `fetch-depth` of `2`.
```yaml
- name: checkout HEAD^ and HEAD
  uses: actions/checkout@v2
  with:
    fetch-depth: 2
```

## Scheduled Jobs

Scheduled jobs are **not guaranteed to run** *or* **guaranteed to run on time**. When a scheduled job is called a request is made to Github actions machines for the job to run and is run once a node is free. This can vary the time from 3-10 minutes but it can be as long as an hour and can sometimes not be run at all if the lag time is long enough. More information [here](https://upptime.js.org/blog/2021/01/22/github-actions-schedule-not-working/).


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYzNjI2ODAzMCwxMzkzNDY2ODM5LDIxMD
A1NjY1NTMsLTE4MDAwMTA2NzJdfQ==
-->