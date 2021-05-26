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

You can **include double quotes** in the raw string literals by adding a number of hashes `#` after the `r` to the beginning of the string and then ending with the same number of hashes.
```rust
let x = r#"Some string with a "quote" in it"#
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ3Njk0NTM0XX0=
-->