
You can **permanently** add environment variables to all future bash terminal sessions for a user by editing the `bash.rc` file in the user's `$HOME` directory. This is done using the `export` keyword.
```
/.bash.rc
export MY_VAR="50m3 c0nt3nt"
```
You will **need to reload your terminal** before you can use these new environment variables. You can check if environment variables have loaded with the `grep` command.
```
env | grep MY_VAR
```
If the environment **still don't load after restarting** you can force the terminal re-read the `bash.rc` file using the `source ~/.bashrc` command.

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjM5MDQ0Njg2XX0=
-->