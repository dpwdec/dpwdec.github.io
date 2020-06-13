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
└── views
    ├── index.hbs
    └── layouts
        └── main.hbs
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYwNjY0ODc2OSwtMjA2MzU5ODY2Nl19
-->