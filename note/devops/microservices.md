---
title: Microservices
layout: page
exclude: true
---

### Canary Deploys

A **canary deploy** is a method for testing a new part of your system with a live audience before completely commiting to that version of your system. For example, if you a current `1.0` version of your service and a new `1.1` version of your service, instead of immediately deploying the `1.1` version to all customers a **canary deploy** deploys both versions simultaneously and then routes a small percentage of traffic to the new service to confirm that it is working correctly in live.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NzE5MzgyNzldfQ==
-->