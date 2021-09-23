---
title: Try
layout: page
exclude: true
---

The `try` function evaluates its arguments and **returns the first argument that does not raise an error**.

This is useful for producing validated objects. For example, when decoding yaml using the `yamldecode` function properties that are required are not necessarily checked as existing or being of the correct type. There for the `try` function can be used in conjugation with a new validate object declaration to default potentially error causing fields. In the example below if `name` on `raw` is undefined - thus raising an error - then the second non error raising argument of an empty string will be returned avoiding any errors.
```terraform
locals {
    raw = yamldecode(file(my_file.yaml))
    validated = {
        name = try(local.raw.name, "")
    }
}
```