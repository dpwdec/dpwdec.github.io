---
layout: page
exclude: true
title: Kubectl
---

Kubectl is the main tool used to interact with any Kubernetes cluster.

You can **access kubectl config** from the `~/.kube/config` file.

You can **check that kubectl is properly configured** using the `cluster-info` command.
```bash
kubectl cluster-info
```

You can **create a range of different resources** using the `create` command. You **cannot create pods directly** with the create command, instead you should use the abstraction of a deployment to create pods.
```bash
kubectl create <RESOURCE>
```

You can **create a deployment** using by specifying `deployment` with `create` and then passing in a name for your deployment and a container `--image` that will act as the blueprint for your pods. *It seems that `kubectl` will automatically find and download the latest version of the image from dockerhub based on the image name provided.*
```bash
kubectl create deployment <NAME> --image=<IMAGE_NAME>
```

For example, the command below will find the latest version of `nginx` as its deployment image from dockerhub.
```bash
kubectl create deployment nginx-deploy --image=nginx
```