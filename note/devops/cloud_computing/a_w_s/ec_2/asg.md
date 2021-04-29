---
layout: page
exclude: true
title: Auto Scaling Groups
---

You can **access the auto scaling console** from the side bar on the **EC2** dashboard page.

Auto scaling groups scale based on **target groups** (which in turn link to load balancers) or *sometimes* directly with load balancers. Essentially the ASG defines a set of policies to trigger instance scaling on for a specific load balancer so that when conditions are met instances can be spun up or down with the attending ALB distributing traffic across the new set of instances.

You can **scale up a family instances** by setting the `desired capacity` property.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk1ODYxMDQyMCwxNTE0NDcxNjgwXX0=
-->