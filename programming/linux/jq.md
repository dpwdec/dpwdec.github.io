---
title: JQ
layout: page
exclude: true
---

JQ is a bash processor for JSON.

You can **access a property of a JSON object** by piping `|` JSON output to the `jq` command and using the `-r` flag followed by the path to data you want to extract inside `''` quote marks. For example if you had the object below and wanted to extract the `name` property...
```json
// user.json
"data": {
  "profile": {
    "name": "Patrice"
    "Age": 104
  }
  "created_at": null
}
```

...you would need to specify the path to property as `'.data.profile.name'` where the highest level `.` period indicates the root of the JSON object.
```bash
cat user.json | jq -r '.data.profile.name'
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg4MjI5NzMwOF19
-->