---
title: Resources
layout: page
exclude: true
---

Resource bocks **represent one more infrastructure object**.

One of the advantages of terraform is that it offers resource provisioning that is *agnostic* of the provider platform. This allows you to avoid learning the underlying provider API.

You can **configure a resource** by using a `resource` block followed by the provider platform and type of resource and then a name for the resource being provisioned that can be referred in the rest of the terraform file.
```terraform
resource "<PROVIDER>_<RESOURCE_TYPE>" "<RESOURCE_NAME>" {
    # resource specific configuration
}
```

## AWS

You can deploy an Amazon EC2 instance using the `"aws_instance"` resource type and provide an AMI ID to the image that you want for the instance as well as a type for the instance size.
```terraform
resource "aws_instance" "myInstance" {
    ami = "<AMI_ID>"
    instance_type = "t3.medium"
}
```