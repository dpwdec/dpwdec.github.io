---
title: For Each
layout: page
exclude: true
---

You can **provision a resource based on a list of variables** by using the `for_each` block with the `toset` function applied to the list. The value of each element in the list is that accessible using the `each` object. Using `toset` the `value` and `key` properties of `each` will be the same.
```terraform
resource "some_resource" "my_resource_group" {
    for_each = toset(["a", "b", "c"])
    name = each.value
}
```