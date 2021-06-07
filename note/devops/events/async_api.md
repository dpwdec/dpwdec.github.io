---
title: Async APIs
layout: page
exclude: true
---

A **message broker** usually refers to a piece of infrastructure that is responsible for sending a receiving messages. Asynchronous APIs are generally **message broker centric**.

A subscriber or consumer manifests and interest in a certain type of message and then **leaves a connection open** to the message broker so that it can have messages pushed to them.

## Messages

Messages are often catalogued as *either* **events** or **commands**.

- Events communicate that something happened
- Commands indicate to the subscribe that it should do something

## Channels

B
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM0Mjk2MTQ1N119
-->