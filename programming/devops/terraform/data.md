---
title: Data
layout: page
exclude: true
---

Data resource blocks allow you **query external information about existing resources** not created by your terraform project. The `data` resource is just like any other `resource` - most things that you can define with a `resource` will have a corresponding `data` versioning for querying. Terraform considers those resources that you define yourself with `resource` to be a *managed resource* by terraform and those things defined using `data` to be external.

The `data` block will match resources in your `provider` against the configuration supplied. Whatever properties are supplied terraform will match and return resources that exist in your provider that match up to those properties.
```terraform
data "some_resource" "data_name" {
    # data resource match configuration here
}
```

