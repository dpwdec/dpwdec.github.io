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

## Conversion between Serde Types

You can **convert between Serde data representations** by using the `from_str` function on a serde value representation you want to convert from with a type hint for the serde value representation you want to convert to.
```rust
fn main() {
    // load some yaml file as raw_yaml_data above here

    let data_as_json = serde_yaml::from_str::<serde_json::Value>(raw_yaml_data.as_str()).unwrap();
}
```

In the example above the raw yaml data (read in from a yaml file as string) is *parsed* using the `serde_yaml` module and then converted using type hints to a `serde_json::Value` type.

## Custom deserialization

You can find some **examples of custom deserialization** with Serde [here](https://damad.be/joost/blog/rust-serde-deserialization-of-an-enum-variant.html).