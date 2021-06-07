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

Brokers generally contain a set of **channels** that hold **different sorts of messages**, one channel for user sign ups, one channel for new purchases etc. These are sometimes can *topics, routing keys* or *event types*.

## Structure

The `info` section of the spec contains a `title` object. *However*, it's not clear how this interacts with the broker, channels model. Is this just a convenient way of grouping different channels?

### Servers


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyNjU2Mjg1MCwtODYwODMxOTE5LC05OD
UwMTIyNTZdfQ==
-->