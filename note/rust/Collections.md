---
title: Collections
layout: page
exclude: true
---

## HashMap

You can **mutate the values in a hashmap** by using the `get_mut` method.
```rust
let mut map: HashMap<char, Vec<u32>> = HashMap::new();
map.insert('a', vec![0]);
match map.get_mut('a') {
  Some(v) => v += 1,
  None => println!("None!")
}
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA0MDM4NDIwNyw1NTUyMjQ3OTYsLTE3Mj
c1NTU4XX0=
-->