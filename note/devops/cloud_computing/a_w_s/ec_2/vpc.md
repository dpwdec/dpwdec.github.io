---
layout: page
exclude: true
title: Virtual Private Cloud
---

A **virtual private cloud** or VPC is an isolated network that spans all availability zones where a feature is deployed.

VPC allows you to isolate features into their own networks within a single AWS account, or allows for the connection of local and cloud based data centres.

The **default VPC** is the default account VPC that all features on an account are placed into.

Instances receive an **internal IP address** so that they can reached from within the virtual network. And an **external or public IP address** that allows them to be reached from outside the network.

External ingress and outgress is managed by an **internet gateway**.

Security groups are grouped under VPCs and VPC provides a convenient way to manage these security groups.

You can use **route tables** defined within a VPC to **control the routing outgoing network requests**. These route tables can control if

- traffic can leave the VPC
- traffic can travel to other instances within the VPC

Using route tables, even if the security group for the VPC is compromised then traffic can still be controlled and prevented from going where it shouldn't.

You can **control the assignment of public IP addresses** using VPC.

Through a combination of route tables and IP address type assignment you can **private subnets** and **public subnets**. This allows you to put publicly accessible resources, like web servers in a public subnet and database servers in the private subnet thus controlling access to resources and improving security.

### NAT Gateway

A **NAT Gateway** allows features in private subnet to access internet resources by redirecting outgoing requests through the VPC route table to the gateway.

**NAT** sta

## Subnets

A subnet is a **subnetwork within a VPC**.  A subnet **spans only ONE availability zone**. A subnet is made up of some subset of the IP ranges within the VPC. 

For example if the VPC range is `1.1.1.1` to `30.30.30.30` then the first subnet (of two) might use the `1.1.1.1` to `15.15.15.15` range, and the second, the `16.16.16.16` to `30.30.30.30` range within the VPC. 

An **instance added to the VPC** will then **receive an IP address from WITHIN the subnet IP range**.

### Network Access Control List

**Network Acess Control Lists** or **NACLs** are **applied at the subnet level** and work similar to security groups controlling what can access a particular subnet. This is only useful if you want differing security across subnets, *otherwise* its probably easier to use security groups applied to instances.


<!--stackedit_data:
eyJoaXN0b3J5IjpbNjg5MzM4NTc4XX0=
-->