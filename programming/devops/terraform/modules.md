---
title: Modules
layout: page
exclude: true
---

You can **organise your terraform infrastructure into submodules** inside the *root* terraform module - represented by the `main.tf` file. Modules are referenced by a name and a `source` argument that points to the folder where the module resides. This is just another collection of terraform files.
```terraform
# main.tf
module "my_module" {
    source = "./path/to/module"
}
```

You can **pass variable declarations to the variables defined in a module** as part of the `module` block. For example, if our submodule defined `location` and `name` variables in its terraform module files these can be passed in as key-value assignments.
```terraform
# main.tf
module "my_module" {
    source = "./path/to/module"
    location = "tokyo-central-1"
    name = "Japan Air Ways"
}
```