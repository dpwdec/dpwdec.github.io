---
layout: page
exclude: true
title: File Descriptors
---

File descriptors are **a list of entries that the kernel maintains that point to open files**. Processes attach to file descriptors to allow them to read / write from / to the system.

By convention, **file descriptor 0 is mapped to STDIN**, **file descriptor 1 is mapped to STDOUT** and **file descriptor 2 is mapped to STDERR** allowing to automatically attach and give output or take input to / from the user.