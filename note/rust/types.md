---
title: Types
layout: page
exclude: true
---

You can **set the type of a constructor IN LINE when creating a new instance of some structures** by including the type in `<>` angle brackets between an extra pair of `::` double semicolons before creating the instance. This creation method is an alternative to typing the assignment variable at declaration.
```rust
let set = HashSet::<i32>::new();
let map = HashMap::<i32, str>::new();
// old alternative
let set: HashSet<i32> =
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzODg2NDE0Nl19
-->