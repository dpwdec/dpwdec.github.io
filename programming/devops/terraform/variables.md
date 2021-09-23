---
title: Variables
layout: page
exclude: true
---

You can **define changeable and reusable values in a terraform file** by using the `variable` block. This block has three properties.

- `description`
- `default`
- `type`: this can be `any`, `string` etc.

```terraform
variable "my_variable" {
    description = "A variable"
    default = "Corbusier"
    type = string
}
```

You can **reference a variable** using the `var` object followed by the variable name after a period.
```terraform
resource "some_resource" "my_resource" {
    some_property = var.my_variable
}
```

You can **assigned terraform variables in the command line** using the `-var` flag.
```bash
terraform apply -var "<VARIABLE_NAME>=<VARIABLE_VALUE>"
```

You can **assign terraform variables from a file** by creating a `terraform.tfvars` file. Terraform will automatically read this file when running an `apply`. This file represents key-value pairs of defined variables.
```terraform
# terraform.tfvars
my_variable = "Corbusier"
```

You can **pass in other `tfvars` files** by using the `-var-file` flag when using the terraform CLI.
```bash
terraform apply -var-file <FILE_NAME>.tfvars
```

You can **assign objects as terraform variables** using standard object syntax.
```terraform
my_variable = {
    Name = "Corbusier"
    Age = 104
}
```