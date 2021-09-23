---
title: Path
layout: page
exclude: true
---

You can **access paths to the file system of a terraform project** using the `path` namespace.

You can **access the root path** using the `root` property.
```terraform
# main.tf
locals {
    root_path = path.root
}
```

You can **acess a submodule's path** using the `module` property.
```terraform
# modules/my_module/main.tf
locals {
    module_path = path.module
}
```