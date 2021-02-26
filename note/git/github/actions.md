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

You can update files that are modified during a CI job using the `test-room-7/action-update-file@v1` action. This takes a path to the `file-path` to the file that has changed, a commit message and a `github-token` for committing that can be loaded directly from the actions environment. The changed file will then be changed on the current branch. The `file-path` is loaded relative to the root directory of the project and should not have `/` or `./` appended to it for loading.
```yaml
- name: Update a file
  uses: test-room-7/action-update-file@v1
  with:
    file-path: path/to/file.txt
    commit-msg: Update file.txt
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

You can **update multiple files** by using the multi-line yaml block with the `|` indicator.
```yaml
file-path: |
  path/to/file_1.txt
  path/to/file_2.txt
  path/to/file_3.txt
```

## Needs

You can **make a job dependent on another job** using the `needs` tag. This should specify the name of a job that should complete successfully before the current job runs.
```yaml
jobs:
  job_1:
    # body of job
  job_2:
    needs: job_1
    # body of job
```

## Outputs

You can **output the result of a step from a job** by using the `outputs` tag and specifying the `steps`, `id` and `outputs` parameter with a name. The output parameter and the name of the property being output should match. You can set an output using a bash block that `echo`s the `set-output` command. 
```yaml
my_job:
  - name: Job that outputs a value
    outputs:
      my_output: ${{ steps.output_value.outputs.my_output }}
    runs_on: ubuntu-latest
    steps:
      - name: Set output
        id: output_value # set step id so it can be referenced at the job level
        run: |
          echo "::set-output name=my_output::true"

another_job:
  - nam
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNTU3NzA2NjEsMTAwNjA1OTk0NiwtOT
MyMjAwMjQ0LDE3NTExODUxMTEsMTY1ODk1NzQ1MSwtNzk5MTY0
NTczLC0xMTMwODAyNDY3LDEzOTM0NjY4MzksMjEwMDU2NjU1My
wtMTgwMDAxMDY3Ml19
-->