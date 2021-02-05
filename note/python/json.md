---
title: json
layout: page
exclude: true
---

You can **parse a stringified json object into a python dict** using the `loads` method on the `json` object.
```python
import json
json_string = '{ "name":"John", "age":30, "city":"New York"}'
json_dictionary = json.loads(json_string)

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU1ODkyMjU0Nl19
-->