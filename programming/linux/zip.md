---
layout: page
exclude: true
title: Zip
---

You can **`zip` everything in a folder structure recursively** by using the `-r` flag with the `zip` command. The command takes the *destination* folder and then the *source* folder for zipping.
```bash
$ zip -r place/to/zip/file.zip source/of/content
```

If you want to **match the root directory of the resource you are zipping with zip file you are creating** you must run the zip command from *within* the folder which is being zipped. For example, given the directory structure below...
```
project
├── out
└── src
	├── my_file
    └── another_file
```

If you run the following commanding to `zip` at the top level of the `project` pointing to `src` and outputting to `out`...
```bash
$ pwd
$ > /project
$ zip -r out/code.zip src
```

Then the structure of the zip would show the `src` folder inside the root of the `.zip` file followed by the content that was zipped.
```
code.zip
└── src
	├── my_file
    └── another_file
```

However, if you `cd` *into* the `src` folder and then run the `zip` command... 
```bash
$ pwd
$ > /project
$ cd src
$ zip -r ../out/code.zip .
```

The root of the `.zip` file will exclude the containing folder.
```
code.zip
├── my_file
└── another_file
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjUwMTY0NTY0LDEyNDkxODM4OCwtMTYxND
EzNzE4OF19
-->