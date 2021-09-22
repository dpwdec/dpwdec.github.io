---
title: Output
layout: page
exclude: true
---

You can **display configuration specific details** after `apply`ing some terraform configuration using the `output` block. This takes an output variable name in its declaration and then a `value` pointing to some property on a resource defined in your terraform file. In the example below `my_resource` does not get assigned a `platform_id` until it is deployed by `terraform apply` so by adding that property into the `output` block it will be printed afer the `apply` command is run.
```terraform
resource "resource_type" "my_resource" {
    # configuration
}

output "my_resource_platform_id" {
    value = resource_type.my_resource.platform_id
}
```