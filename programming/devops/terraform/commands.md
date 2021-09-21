---
title: Commands
layout: page
exclude: true
---

To run a terraform project you first run the `init` command. This initializes and downloads provider plugins for the infrastructure.
```bash
terraform init
```

You can **see a preview of the actions a terraform template will take** by using the `plan` command. This color codes actions based on what they do, such as creating, deleting or modifying infrastructure.
```bash
terraform plan
```

To actually run the terraform code and **provision infrastructure** use the `apply` command.
```bash
terraform apply
```

You can **tear down the entirety of your provisioned infrastructure** using the `destroy` command.
```bash
terraform destroy
```

Terraform will also destroy instances that don't match the state of the target `.tf` file it is running.

Terraform is structured to work **declaratively** *not* **imperatively**. This means that the infrastructure described by a `.tf` is the final state of the infrastructure. This is why running `apply` multiple times won't result in provisioning multiple instances because terraform keeps track of the pieces of infrastructure deployed using it so if it runs again it will check that that infrastructure is there before creating it again or modifying it, and if all the pieces *are* there it will do nothing.

You can **automatically run a terraform command** without having to approve the plan with a `yes` by using the `--auto-approve` flag.
```bash
terraform apply --auto-approve
```