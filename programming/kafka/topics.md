---
title: Topics
layout: page
exclude: true
---

Topics are Kafka's **most fundamental unit of organisation**. Different topics hold different types of events.

You can **create new topics to hold filtered versions of existing events**.

A Topic is **structured as event log**. This gives it several key properties:

- Logs are **append only**
- Logs are **immutable**
- Logs can be read at any position using an **arbitrary offset** combined with **sequential scanning**.

Topics are durable and can be stored as if they were database data.

# Partioning

Topics are partitioned across multiple clusters to improve performance.

Events with no Key are distributed round-robin to topic partitions. This **does not preserve the ordering of these events**.

If an Event does have a Key associated with it, such as an order ID, the Key **guarantees that all events associated with a specific Key will arrive in order** and so events associated with that Key are distributed to a specific node on the cluster that holds that Key.

Where data is sent to partitions is **controlled by the `Producer` object** when creating code to send events to Kafka.

# Brokers

Topics are **partitioned between brokers**. These are just individual machines (virtual, containerized or otherwise) running the Kafka broker process.

The data in brokers is replicated to several other brokers to keep it safe. These replicas are called **follower replicas** and the main partition - which handles reading, writing etc. - is called the **leader replica**. Changes are replicated to the followers as they happen.

