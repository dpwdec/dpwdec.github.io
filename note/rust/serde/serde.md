---
title: Serde
layout: page
exclude: true
---

Serde is a **ser**ialisation  and **de**serialisation framework for rust.

If you want to **use the derive macros** for serde serialization and other features you must **add them as feature flags** in your `cargo.toml` file.
```yaml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg2NjE1MzA3NywtMTA5OTQ5Mjg3MV19
-->