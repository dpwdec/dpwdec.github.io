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

## Commit Tags

You can use the `HEAD` tag in a github actions job to **point to the current commit** that the CI is running on.

*However* you cannot use the `HEAD^` relative tag to point to the previous commit in the branch *even* with a fetch depth greater than 1. Instead you should use the `origin/master^` tag to point to the previous commits on the master branch.
```bash
git diff origin/master^ HEAD
```

This is also the method used to **diff pull requests with the master branch** of a project, by comparing `HEAD` and `origin/master^`.

## Scheduled Jobs

You can **run a CI job on a periodic schedule** by using the `schedule` tag with `on` and then `cron` tag followed by a valid cron string. The example below will trigger this job at `23:59` everyday.
```yaml
on:
  schedule:
  - cron: "59 23 * * *"
```

Scheduled jobs are **not guaranteed to run** *or* **guaranteed to run on time**. When a scheduled job is called a request is made to Github actions machines for the job to run and is run once a node is free. This can vary the time from 3-10 minutes but it can be as long as an hour and can sometimes not be run at all if the lag time is long enough. More information [here](https://upptime.js.org/blog/2021/01/22/github-actions-schedule-not-working/).

## Update files

You can update files that are modified during a CI job using the `test-room-7/action-update-file@v1` action.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NzIzMzU5MzUsMTc1MTE4NTExMSwxNj
U4OTU3NDUxLC03OTkxNjQ1NzMsLTExMzA4MDI0NjcsMTM5MzQ2
NjgzOSwyMTAwNTY2NTUzLC0xODAwMDEwNjcyXX0=
-->