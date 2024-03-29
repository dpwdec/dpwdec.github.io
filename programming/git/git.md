---
title: Git
layout: page
exclude: true
---
If you find yourself working on a project branch having **not made a commit and wanting to delete all the changes you've made** to the that branch and revert to the last commit.
```
$ git fetch origin
$ git reset --hard origin/master
$ git clean -f
```

## staging

You can **unstage a file** using the `git reset` command.
```bash 
$ git reset HEAD -- <file>
```

If you want to **unstage a file** but it doesn't have previous commits *or* you don't want to lose changes to it use a plain `reset` command.
```bash
$ git reset <file>
```

## Remotes

You can **show current remotes on a project** by using the `show origin` command.
```bash
$ git remote show origin
```

You can **add a git remote** using the `add` command followed by the name of the remote and then a link to the repo that the remote should point to.
```bash
$ git remote add <REMOTE_NAME> <LINK_TO_REMOTE>
```

You can **remove a git remote** using the `rm` command followed by the name of the remote.
```bash
$ git remote rm <REMOTE_NAME>
```

## Rebasing
You can **merge the current version of the master branch into another branch** by checking out your branch then using the `pull` command with `origin master`. This known as *rebasing* your branch with the project.
```bash
$ git pull origin master
```

You **exit the rebasing commit window** that appears after running a `pull origin master` by using the `vim` quit command.
```vim
:wq
```

## Branches

You can **create a branch from a branch** by using the `checkout` command to create a new branch with second argument being the name of the branch off of which to branch. *If this second argument is left blank you just branch from master.*
```bash
git checkout -b <NEW_BRANCH_NAME> <BRANCH_TO_BRANCH_FROM_NAME>
```


## gitignore

If you want to specify in your `.gitignore` that you want to **commit a folder to git but NOT the contents of that folder** you should use the `*` all and `!` exception flags. You **cannot commit empty folders to git** so you need to add at least one file to the folder, its recommended that this is a `.gitkeep` file which will allow you to commit the folder but won't effect your project. You then need to set up your `.gitignore` so that the contents of folder is ignored, using the `*` all matcher and then create an exception to that rule using the `!` exception flag that specifies that you *CAN* upload the `.gitkeep` file.
```git
# .gitignore
# ignore everything in this folder
some_folder/*
# apart from my .gitkeep file
!some_folder/.gitkeep
```
The associated file structure would look something like the example below.
```
.
├── .gitignore
└── some_folder
    └── .gitkeep
```

If you want to **ignore a file or folder that you have already committed to git** you must use the `rm` function to removed cache folders before doing a commit. Git will not register a folders inclusion in `.gitignore` until this is done.
```bash
$ git rm -r --cached <path/to/folder>
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbNzA0OTY0MjI2LDY0OTU0MjMwMSwtMTc0MT
I0MzU0LC02ODI2NTk3ODAsMTU1MTkyMDk0MSwtMTYwMDUzMzI0
NywtODE4MTUyODUzLC0yMDYzNTk4NjY2XX0=
-->