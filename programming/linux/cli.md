---
layout: page
exclude: true
title: CLI
---

You can **create a simple CLI** with long and short flags using a `while` loop over the `$1` input and `case` statements which match against input flags and then `shift` arguments left to consume them.
```bash
while true; do
  case "$1" in
    -a | --add ) X="Add"; shift ;;
    -s | subtract ) X="Subtract"; shift ;;
    * ) break ;;
  esac
done
```

You can **create a simple help menu** using the `EOF` and `cat` commands integrated with the previous CLI selections, you should use the `exit` command after the help is called.
```bash
showHelp() {
cat << EOF
--- HELP MENU ---
-a  --add           Adds stuff
-s  --subtract      Subtracts stuff
EOF
}

while true; do
  case "$1" in
    -a | --add ) X="Add"; shift ;;
    -s | subtract ) X="Subtract"; shift ;;
    -h | --help ) showHelp; exit 0 ;;
    * ) break ;;
  esac
done
```