---
layout: page
exclude: true
title: Architecture
---

# Worker Nodes

Each node hosts multiple pods. These nodes that actually serve requests and compute are called "worker" nodes.

A worker node runs 3 Kubernetes processes:

1. **Container run time** (such as Docker) for running containers
2. **Kubelet** which acts as an interface between the node and the container. It is responsible for actually starting pods and assigning system resources to it.
3. **Kube Proxy** which forwards requests from services to pods.

# Master Nodes

A **master node** is used to **control the state of a K8s cluster**. A master node is completely different from worker nodes.

A master node runs 4 Kubernetes processes:

1. **API Server** acts a **gateway to the cluster that allows for configuration, requests and updates**. It also acts as an authentication service for requests to the cluster. 
> Whenever you want to deploy new services, query the status of the cluster etc. you have to do it through the API server on the master node which validates you requests and then acts on the worker nodes.
2. **Scheduler** is responsible for ***scheduling* pods to start on different nodes once requests are authenticated by the API server**. It does this intelligently based on the resources available to it on the worker nodes.
> The scheduler sends requests to the **Kubelet** process running on workers nodes, which then starts a new pod on that node.
3. **Controller Manager** will **detect state changes in the cluster**, such as pods crashing / dying on a node in the cluster and then **makes a request to the schedule to bring the pods back up**.
4. **etcd** is a **key value store of the cluster state**. Any time that the state of the cluster changes - a pod being brought up, a pod going down etc. - this state change is stored in `etcd`.
> The Controller Manager and Scheduler processes rely on the data from etcd to make decisions. This is how the scheduler knows what resources are available, or how CM knows when a pod goes down, or how API Server returns query data to an end user about the cluster. *No application data is stored here*.

Kubernetes clusters **can have multiple master nodes**. In this case, **calls to the API Server are load balanced** and **data is distributed between the etcd processes**.