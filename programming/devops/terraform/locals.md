---
title: Locals
layout: page
exclude: true
---

You can **assign local variables** using the `locals` block. This takes a set of key-value pairs and expressions that can be re-used throughout the terraform file with the `local` namespace. This is very similarly to defining a `variables` block with a default but makes it explicit that this value is not passed in by computed and used within the file based on information already provided.
```terraform
locals {
    foo = "bar"
}

resource "some_resource" "my_resource" {
    property = local.foo
}
```

