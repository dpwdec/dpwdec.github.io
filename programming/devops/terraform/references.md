---
title: References
layout: page
exclude: true
---

Terraform references are **not required to be defined in order**. You can define something which has dependencies before those dependencies are declared are terraform will figure out which order to create things in.

You can **reference dependent resources within your terraform file** by using the resource type, name and property with the pattern `<RESOURCE_TYPE>.<RESOURCE_NAME>.<RESOURCE_PROPERTY>`.
```terraform
resource "some_resource" "some_name" {
    # config
}

resource "dependent_resource" "name" {
    some_property = some_resource.some_name.id
}
```