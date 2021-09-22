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

Some resources in terraform are **purely associative**. For example, you may need to link two separate resources after they are created, for this you would use an *associative* resource, such as `aws_route_table_association` to associciate a subnet and route table using the `id` of each separately created resource.

## Dependencies

*Some* resources **must be defined** in order of the things they depend on. On example of this is an AWS Elastic IP requiring a Network Gateway to be defined *before* its declaration so that it can work. If a resource does have a dependency its reccommended to use the `depends_on` key inside the resource. This should point to the entire dependency as an object in a list.
```terraform
resource "some_resource" "name" {
    # resource config
}

resource "dependent_resource" "dependent_name" {
    # resource config
    depends_on = [
        some_resource
    ]
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

If you **do not specify an availability zone on a resource** then a random AZ will be picked. This can be problematic if you have multiple components that depend on one another so its **better to specify your availability zone on resources** with the `availability_zone` key.

You can **run a bash script** on your an AWS instance at start up by using the `user_data` key with the `<<-EOF` pipe and the script.
```terraform
resource "aws_instance" "myInstance" {
    ami = "<AMI_ID>"
    instance_type = "t3.medium"

    user_data = <<-EOF
                #!/bin/bash
                sudo apt update -y
                sudo apt install apache2 -y
}
```