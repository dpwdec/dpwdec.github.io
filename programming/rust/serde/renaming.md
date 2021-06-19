---
title: Renaming
layout: page
exclude: true
---

You can **match fields for deserialization based on naming rules** by using the `rename_all` attribute. For example, if I have an enum for HTTP methods.
```rust
enum HttpMethod {
  Get,
  Put,
  Post
  // etc.
}
```

But the data that I want to deserialize comes in the format of HTTP verbs described with `GET`, `PUT`, `POST` etc. Serde will **not be able to automatically deserialize** these because the casing does not match. However, by adding the `rename_all` attribute with the `"UPPERCASE"` argument, we can indicate to Serde that it should parse in upper case representations of these enum name.
```rust
#[serde(rename_all = "UPPERCASE")]
enum HttpMethod {
  Get,
  Put,
  Post
  // etc.
}
```

You can even **define seperate rules for serialization and deserialization** by using the `rename_all` attribute like a function and adding `deserialize` and `serialize` kwargs to it. This allows us to deserialize our HTTP verbs from uppercase and then perhaps serialize them to a separate script in their lowercase representation where they get called by some worker service.
```rust
#[serde(rename_all(deserialize = "UPPERCASE", serialize = "lowercase")]
enum HttpMethod {
  Get,
  Put,
  Post
  // etc.
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5MzcyNDcyXX0=
-->