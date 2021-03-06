---
title: Microservices
layout: page
exclude: true
---


## API Gateway

Orchestration - Stitch multiple services together, create a single API from multiple backend systems
Mediation - Convert to an approriate output -> REST JSON
Message Security - ensure end to end security of the user
Authorisation
DDOS Protection - A lot of security concerns like firewalls etc.
One leg in the outside world, one leg in the inside world, a bridge between the dangerous open internet and internal security.

ESB (Enterprise Service Bus) - Exists *between* individual microservices (this could be the "sidecar" concept in a service mesh pattern). Generally this service may include some orchestration and mediation but its unlike to have much sercurity as its generally designed to be behind the DMZ and not exposed publicly.

EAI (Enterprise Application Integration) - This is just a name for a piece of software that manages the integration of multiple services within an organisation. *Importantly* this specifically refers to an *internal* piece of software.

DMZ (Demilitarised Zone) - The part of your application stack which is publicly available on the internet.

Another advantage of API gateways is that they can essentially act as a proxy when needed. For example if they are just directly exposing Rest Api they can simply add in the necessary proxy functionality without slowing things down by heaping extra unecessary functions.

## API Proxy

A **proxy** is essentially a more limited **API gateway**. It can accomplish some of things that a **gateway** can in supporting a microservices architecture, such as **security**, **monitoring** and **access quotas**. *However* the key weakness of a proxy is that it **does not any functionality to APIs**. It can only **re-expose** existing APIs and cannot collate and bundle a set of disparate requests like a gateway does which is not so useful when you are dealing with a very distributed system of microservices with potentially hundreds of components. Often a **proxy will be wrapped in a gateway** and not used separatel with modern microservices architectures.
```
┏━━━━━━━━━━━━━━━┓
  Internal API: GET /users
┗━━━━━━━━━━━━━━━┛
		┇
┏━━━━━━━━┓
      Proxy
┗━━━━━━━━┛
		┇
┏━━━━━━━━━━━━━━━┓
  External API: GET /users
┗━━━━━━━━━━━━━━━┛
```

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
eyJoaXN0b3J5IjpbLTE5NTkzMzEyMDQsNzU3MzcwMzE1LDE4NT
A3NTA1MDgsLTEyNjU1MTQ2MTgsLTE1NjYyNjM5ODAsLTExNDgz
MDEzNDIsMTQwMDM4OTUzOCwtNTY3MTU4MjYxXX0=
-->