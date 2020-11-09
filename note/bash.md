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

## Tee

You can **use `tee` instead of double redirection modifier `>>`** as the implementation of the redirection modifier `>>` on different linux distributions is inconsistent.

You can **append to a file** by using the `tee` command with the `echo` of what you want to append piped `|` to the command. The **`-a` flag indicates that the text you should appended** to the target file.
```bash
$ echo "some text" | tee -a file.txt
``` 

If you have **problems with user permissions** you can `sudo` the `tee` part of the command.
```bash
$ echo "some text" | sudo tee -a file.txt
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMTE3NDk3NDgsNjk2OTM5ODgyLC02Mj
c1NDYyMjMsMTY5NTc4OTcxNF19
-->