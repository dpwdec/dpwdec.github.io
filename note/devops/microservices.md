---
title: Microservices
layout: page
exclude: true
---

### Canary Deploys

A **canary deploy** is a method for testing a new part of your system with a live audience before completely commiting to that version of your system. For example, if you a current `1.0` version of your service and a new `1.1` version of your service, instead of immediately deploying the `1.1` version to all customers a **canary deploy** deploys both versions simultaneously and then routes a small percentage of traffic to the new service to confirm that it is working correctly in live.

![Canary Deploys](https://drive.google.com/file/d/11exwptVKHnL1KJUzt_XWJTwYpolmeO5_/preview)

### Trace Ids

Another potential problem of a microservices architecture is debugging failing requests effectively as a request may be going through a huge number of services to produce the desired output. When way to solve this problem is using **trace ids** which assigns a unique id to each request to the system.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTc2MDE0Njk2LC01NjcxNTgyNjFdfQ==
-->