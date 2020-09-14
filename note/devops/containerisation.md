---
title: Containerisation
layout: page
exclude: true
---

## Virtual Machines

Previously hosting applications was done using a **virtual machine (vm)**. These virtual machines would be hosted on another physical machine with its own **host operating system** as well as a **hypervisor** responsible for creating new instances of the virtual machines for new applications. Virtual machines (for example a linux host for application) would require a copy of the **guest operating system** and even some libraries to run the application as well. Even though the application being hosted in the VM might be very lite, the VM comes with extra baggage.

For example, the smallest node js VM is 400mbs whereas the node app and runtime itself would only be 15mb. 😱
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAwODU5ODI4XX0=
-->