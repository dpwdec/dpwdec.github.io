---
title: Containerisation
layout: page
exclude: true
---

## Virtual Machines

Previously hosting applications was done using a **virtual machine (vm)**. These virtual machines would be hosted on another physical machine with its own **host operating system** as well as a **hypervisor** responsible for creating new instances of the virtual machines for new applications. Virtual machines (for example a linux host for application) would require a copy of the **guest operating system** and even some libraries to run the application as well. Even though the application being hosted in the VM might be very lite, the VM comes with extra baggage.

For example, the smallest node js VM is 400mbs whereas the node app and runtime itself would only be 15mb. 😱

This means that creating a new VM will consume a fair number of system resources on the host server. Furthermore, **for each new instance of our application we have to spin up an entirely new VM** again with another copy of the guest operating system and associated libraries causing even more use of server real estate.

There are also potential problems with the target VMs hosted on a server being different
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk4MzI5MDg3OF19
-->