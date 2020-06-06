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

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNjM1OTg2NjZdfQ==
-->