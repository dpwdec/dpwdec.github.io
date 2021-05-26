---
title: Strings
layout: page
exclude: true
---

## Raw String Literals

You can **write non-escaped strings** using the `r` character at the beginning of a string. This allows you encode JSON objects and other complex string objects *without* the overhead of escaping. The single `r` **does not include `""` double quotes**, these will terminate the string.
```rust
let x = r"Some $#
          non escaped string"
```

You can **inclu**
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkzNTg1OTE4M119
-->