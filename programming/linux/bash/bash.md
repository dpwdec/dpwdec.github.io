---
layout: page
exclude: true
title: Bash
---

You can **assign a varaible** using the `=` equals operator. However, its *important to note in bash scripting that if you add spaces between the assignment then the variable will NOT be assigned*.
```bash
# variable is assigned correctly
MY_VAR="foo"

# variable is not assigned correctly at all
MY_VAR = "foo"
```

You can **check if a variable is null** using the `-z` operator. This **returns true if the argument IS null**.
```bash
test -z $MY_VAR # -> true
```


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

You can **get positional arguments passed when calling a bash script** by using `$<ARGUMENT_NUMBER>` to access the arguments. For example for the script
```bash
# my_script.sh
#!/bin/bash
echo $1
echo $2
```

Then passing in two arguments `Hello` and `world!` as space separated arguments will automatically be put into the `$1` and `$2` variables. This can go up arbitrarily high depdending on how mant arguments you pass in.
```bash
my_script.sh Hello world!
# Output:
# Hello
# world!
```

## Results

You can **check the outcome result of the last command run** using the `$?` variable. This will be either a `0` or `1` depending on whether the command succeeded.
```bash
echo $1
```

## Ternary

You can **create a "ternary-like" statement** by surrounding the condition of the statement with `[[]]` double square brackets and then using the `&&` and `||` symbols to separate the conditions.
```bash
[[ <CONDITION> ]] && <IF_TRUE> || <IF_FALSE>
```

For example
```bash
[[ 1 != 2 ]] && echo "Not Equal!" || echo "Equal!"
# => Not Equal!
```

## Operating System

You can **test whether a script is running in a Linux or OSX (or other?) environment** by using the `uname` property against the name of system environment.
```bash
if [ "$(uname)" == "Darwin" ]
then
  echo "We're on Mac!"
elif [ "$(uname)" == "Linux" ]
then
  echo "We're a cool kid!"
fi
```

You can also **get these values directly in the terminal** by simply typing `uname`. The *default argument for this command is `-s`*.
```bash
$ uname
Linux
```