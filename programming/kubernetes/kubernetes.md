---
layout: page
exclude: true
title: Kubernetes
---

Kubernetes is also called K8s. The 8 represents a contraction of the 8 characters `ubernete` between the `K` and `s`.

# Nodes

A **Node** is a physical or virtual machine that kubernetes can provision as infrastructure.

# Pods

A **Pod** is an abstraction over a container that provides of a container-platform-agnostic interface with which to interfact with the container.

Pods are **ephemeral** and can be removed at any time due to crashes, failure etc.

Usually you have **a single container per pod**. However, you can have multiple containers if you need a "side-car" application that supports the main container inside the pod.

Kubernetes has a virtual network which assigns each individual pod its own IP address which allows pods to communicate. 

When a **pod dies it is assigned a new IP address**, so **communicating via IP addresses on pods is not reccommended**.

# Service and Ingress

Pods are also assigned a **service** object that has a permanant IP address.

The **service and pod lifecycles are NOT connected**. This allows you to communicate with pods using the service IP address regardless of the underlying cycle state of the pods you are communicating with.

A **service can act as an entry for multiple underlying pods**. In this capacity it **also functions as a load balancer** routing external traffic into different pods to handle requests.

A **service has two functionalities**:

1. Prodividing a static IP address for a group of pods
2. Load balancing ingress traffic to pods

## Internal Service

An **internal service** is a service that is NOT exposed to public traffic, such as a database service.

## External Service

An **external service** allows you to expose service endpoints to public traffic.

An external service address is expressed as the IP address of the *node* on which a service is running and then a *port* which points to the service *inside* that node.

## Ingress

An **ingress** component allows you **specify a human readble ("nice") name for traffic visiting you external service**. *This solves the above problem of external service endpoints being expressed simply as an IP address and port.*

# ConfigMap and Secret

Similar to environment configuration. ConfigMap and Secret allow you to get environment variable data to your application such as connection strings or credentials.

## ConfigMap

**ConfigMap** allows you to store external configuration data about your application. 

For example, its customary to store the url for a database *inside* of an application build. Somewhere in your application code a `string` will reference the address by which to connect to database. This means that if the database address changes you will need to rebuild your application.

ConfigMap allows you to **store named variables** so that if a reference address changes the way its referenced inside a service remains consistent. This can be something as simple as just having a `DATABASE_URL` variable.
```
DATABASE_URL = my.database.url
```

You **should not put credentials or secrets** inside of **ConfigMap**. It is *not* secure.

## Secret

Secret is similar to ConfigMap but **used to store sensitive data** using base64 encoding.

# Deployment

A **deployment** is an abstraction over pods. 

A deployment makes it easier to work with pods by

- providing a blueprint for pods
- specifying how many pods to be deployed *(thus allowing for easy replication of pods)*

Generally, you don't create pods directly when working with K8s. But instead work with deployments.

## Databases

Databases **cannot be replicated using a deployment**. 

This is because multiple database components would need to access a single data volume which could quickly cause inconsistencies if this access is not correctly managed.

# StatefulSet

StatefulSet is used to **serve stateful applications with databases**.

**Databases should be created using a StatefulSet** and *not* using a deployment.

*It's not clear whether a statefulset is used for JUST databases. Or if its more entire stateful applications?*

**Databases are often hosted *outside* of the K8s cluster** due to the challenge of hosting stateful applications *fully* inside of K8s using StatefulSet.

# Volumes

Volumes **allow you to persist container data**. This can be persisted locally on the same machine as that running container, or, on a storage system.

A Kubernetes cluster **does not manage data persistence**. Instead its better to think of the K8s cluster as a single machine onto which volumes are mounted. The user is responsible for the reliability of these volumes on which data is persisted.

