---
layout: page
exclude: true
title: Virtual Private Cloud
---

A **virtual private cloud** or VPC is an isolated network that spans all availability zones where a feature is deployed.

VPC allows you to isolate features into their own networks within a single AWS account, or allows for the connection of local and cloud based data centres.

The **default VPC** is the default account VPC that all features on an account are placed into.

Instances receive an **internal IP address** so that they can reached from within the virtual network. And an **external or public IP address** that allows them to be reached from outside the network.

## Subnets

A subnet is a **subnetwork within a VPC**. 

A subnet **spans only ONE availability zone**.

A subnet is made up of some subset of the IP ranges within the 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNTIzODg3NDhdfQ==
-->