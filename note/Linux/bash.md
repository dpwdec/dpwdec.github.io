---
layout: page
exclude: true
title: Bash
---

## Scripts

You can **create a bash script** by giving a file the `.sh` extension.
```
my_script.sh
```

To **start writing a script** you must open it with a shebang that points to the bash interpreter so that the script can run. The first line of the script will always be a path to the interpreter for bash to use. You can then use any bash command you would normally use in the console inside your script and the commands will be executed procedural with bash waiting for each command to finish before executing another.
```bash
#!/bin/bash
```

You can **run a bash script** by simply typing the name of the script file (or path to the file prepended by a `./`).
```bash
$ ./my_script.sh
```

You can also **execute bash scripts** using the `sh` or `bash` commands.
```bash
$ sh my_script.sh
$ bash my_script.sh
```

Your script may not have execution privileges. To **make your script executable** use the `chmod +x` command.
```bash
$ chmod +x my_script.sh
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY5NTc4OTcxNF19
-->