---
title: Project Structure
layout: page
exclude: true
---

The `.terraform` file is created when the `init` command is run and holds project specific provider plugin installation files.

The `terraform.tfstate` file contains a record of all the infrastructure that the terraform project has created. This is how terraform knows what it has and has not done and how it can declaritvely match the `.tf` files' state by checking what its done. *Should this file be committed?*
