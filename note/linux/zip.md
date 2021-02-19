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

If yo
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQ5MDE5MTgsMTI0OTE4Mzg4LC0xNjE0MT
M3MTg4XX0=
-->