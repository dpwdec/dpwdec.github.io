---
title: Structs
layout: page
exclude: true
---

You can **define an anonymous Tuple Struct** by using the `struct` keyword, followed by the name of the tuple struct and the value types that the struct should hold in brackets. These **Tuple Structs** are useful if you want to give a particular tuple a name and differentiate them by type.
```rust
struct Color(u16, u16, u16);
struct IdCode(String, String, i32);
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk2MDM0MTM3LDE3OTk0ODI0MTVdfQ==
-->