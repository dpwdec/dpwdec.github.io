---
title: Microservices
layout: page
exclude: true
---

## API Gateway

### Canary Deploys

A **canary deploy** is a method for testing a new part of your system with a live audience before completely commiting to that version of your system. For example, if you a current `1.0` version of your service and a new `1.1` version of your service, instead of immediately deploying the `1.1` version to all customers a **canary deploy** deploys both versions simultaneously and then routes a small percentage of traffic to the new service to confirm that it is working correctly in live.

![Canary Deploys](https://i.imgur.com/2vnL1M4.png)

### Trace Ids

Another potential problem of a microservices architecture is debugging failing requests effectively as a request may be going through a huge number of services to produce the desired output. When way to solve this problem is using **trace ids** which assigns a unique id to each request to the system. Each unique request will be logged on each microservice allowing you to identify where in a system a request might be failing.

Whitelisting - which service can talk to which other service
TLS? Security and HTTPS


## Mesh

The motto of a **microservice mesh** is:

> "Do not burden my code with all these infrastructure related decisions"

A mesh follows a `sidecar` and `controller` pattern. Each microservice in your system will be fitted with a `sidecar`, the job of which is communicate with other `sidecar`s on other microservices as needed.

![enter image description here](https://i.imgur.com/0ajWAdQ.png)


Next the system is also outfitted with a `controller`, the job of which is to manage metadata and utilities about the sidecars such as authentication, locations etc.

![enter image description here](https://i.imgur.com/1AY5T70.png)


gRPC
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDA0MDg1MSw3NTczNzAzMTUsMTg1MD
c1MDUwOCwtMTI2NTUxNDYxOCwtMTU2NjI2Mzk4MCwtMTE0ODMw
MTM0MiwxNDAwMzg5NTM4LC01NjcxNTgyNjFdfQ==
-->