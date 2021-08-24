---
title: Kafka
layout: page
exclude: true
---

Events are small, typically `<1mb~` in size.

Events are represented in a structured format (JSON, Protocol Buffers etc.)

Kafka is structured as a Key/Value pair commit log. 

The Value data in Kafka is serialized as a complex object and can then deserialized when accessed by a consuming piece of software.

Keys are usually primitive types. They are not necessarily unique but usually identify some entity in the system, like a user or order number.

