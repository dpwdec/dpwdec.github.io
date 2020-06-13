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


If you want to specify in your `.gitignore` that you want to **commit a folder to git but NOT the contents of that folder**

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NzM0NDU2MywtMjA2MzU5ODY2Nl19
-->