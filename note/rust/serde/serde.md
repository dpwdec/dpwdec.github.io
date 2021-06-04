---
title: Serde
layout: page
exclude: true
---

Serde is a **ser**ialisation  and **de**serialisation framework for rust that uses trait bounds to convert between many different data formats.

If you want to **use the derive macros** for serde serialization and other features you must **add them as feature flags** in your `cargo.toml` file.
```yaml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
```

## Convert between formats


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NTc0MDI0MzYsLTEwOTk0OTI4NzFdfQ
==
-->