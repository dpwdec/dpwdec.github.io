---
title: Files
layout: page
exclude: true
---

You can **write to a file** by using the `open` function with the `"w"` argument as the operation flag. You can then use the `write` method to write data to the file. Doing this using the `with` context command closes the file automatically once writing is complete.
```python
with open('output.txt', 'w') as output_file:
  output_file.write('Here is some text')
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDI4Nzg4NTU0XX0=
-->