---
title: Linux 
layout: page
exclude: true
---

`systemctl` can be used to start and stop services based on configuration in `systemd`.

`ps` shows running processes

`ps -ef` shows extra running process detail

## JQ

JQ is a bash processor for JSON.

You can **access a property of a JSON object** by piping `|` JSON output to the `jq` command and using the `-r` flag followed by the path to data you want to extract inside `''` quote marks.
```json
"data": {
  "profile": {
    "name": "Patrice"
    "Age": 104
  }
  "created_at": 
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwOTY5Mjc2MjEsMTY3NDMwNjM5NywxMz
I3OTg0ODA0LDE5MDYyMDU2NTldfQ==
-->