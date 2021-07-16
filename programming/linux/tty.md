---
layout: page
exclude: true
title: TTY
---

You can **display which terminal the user is currently logged into** using the `tty`.

The `tty` command stands for **T**ele**TY**pewriter.

On contemporary linux machines or in linux running on containers this will print the location of terminal as something like `/dev/pts/<TERMINAL_NUMBER>`.

The **`pts` stands for pseudo terminal slave** and is an emulated terminal that is piping input from another location to display virtually. For example, when ssh-ing you don't have access to the actual terminal of the infrstructure you are controlling. Instead the terminal information is being broadcast via a pseudo terminal to your remote location.