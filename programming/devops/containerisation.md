---
title: Containerisation
layout: page
exclude: true
---

## Virtual Machines

Previously hosting applications was done using a **virtual machine (vm)**. These virtual machines would be hosted on another physical machine with its own **host operating system** as well as a **hypervisor** responsible for creating new instances of the virtual machines for new applications. Virtual machines (for example a linux host for application) would require a copy of the **guest operating system** and even some libraries to run the application as well. Even though the application being hosted in the VM might be very lite, the VM comes with extra baggage.

For example, the smallest node js VM is 400mbs whereas the node app and runtime itself would only be 15mb. 😱

This means that creating a new VM will consume a fair number of system resources on the host server. Furthermore, **for each new instance of our application we have to spin up an entirely new VM** again with another copy of the guest operating system and associated libraries causing even more use of server real estate.

There are also potential problems with the target VMs hosted on a server being a different OS from that which your application was developed in leading to intractable errors that slow production.

## Containers

A **container is created in a three step process**.

 1. Create a **manifest file** to describe the form that the container takes.
 2. Create an **application image** that contains the specific code for your application
 3. Create a **container** that contains the run time environment that your image works with.

Instead of a **hypervisor** containerisation platforms use a **runtime engine** specific to them on which the containers can be hosted.

Containers **do not include a copy of the OS on which the application runs** so they are much more lightweight than virtual machines and so more of them can be deployed on a single server.

Containers are also more flexible in communicating between each other, for example if you have separate Python and Node containers they can easily communicate between each other to send data, however on a VM you would have to spin up a heavy new service for each interaction or contain bother services in a single VM which stops the application from being scalable.

Containers also have the advantage of **sharing unused system resources between themselves** making the run times faster.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMjE4OTk4MTZdfQ==
-->