---
title: Count
layout: page
exclude: true
---

You can **create an arbitrary number of a resource** by using the `count` property. You can **access the resource index as it is created** by using the `index` property on `count`.
```terraform
resource "some_resource" "my_resource_group" {
    count = 5
    name = "Resource ${count.index}"
}

```