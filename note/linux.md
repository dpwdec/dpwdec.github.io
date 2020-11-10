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

You can **access a property of a JSON object** by piping `|` JSON output to the `jq` command and using the `-r` flag followed by the path to data you want to extract inside `''` quote marks. For example if you had the object below and wanted to extract the `name` property
```json
"data": {
  "profile": {
    "name": "Patrice"
    "Age": 104
  }
  "created_at": null
}
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMzE4ODQ2OTYwLDg2MTY3OTQwOCwxNjc0Mz
A2Mzk3LDEzMjc5ODQ4MDQsMTkwNjIwNTY1OV19
-->