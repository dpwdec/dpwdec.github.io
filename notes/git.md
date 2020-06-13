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

## gitignore
If you want to specify in your `.gitignore` that you want to **commit a folder to git but NOT the contents of that folder** you should use the `*` all and `!` exception flags. You **cannot commit empty folders to git** so you need to add at least one file to the folder, its recommended that this is a `.gitkeep` file which will allow you to commit the folder but won't effect your project.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NjUwODQwMzIsLTIwNjM1OTg2NjZdfQ
==
-->