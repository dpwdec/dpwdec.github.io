---
title: json
layout: page
exclude: true
---

You can **parse a stringified json object into a python dict** using the `loads` method on the `json` object.
```python
import json
x = '{ "name":"John", "age":30, "city":"New York"}'
json.loads(x)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQxMTcxNTI1NF19
-->