---
layout: page
exclude: true
title: Simple Queue Service
---

You can **see how many messages are available to be consumed** on the root SQS interface.

You can **put messages into the DLQ** based on how many times the message was received. This means, the number of times an application or user polled the queue and received a message but did not delete them. This implies there was some issue with the message and so it needs to be stored in the DLQ.

The **DLQ must match the queue type for the main queue**, whether that be a **standard** queue or a **FIFO** queue.

## FIFO Queues

FIFO messages are grouped under a `Message Group ID` which ensures that messages of the same group are delivered in a FIFO manner. Presumably this means that you could be delivering two different groups of messages to a FIFO queue - *a* and *b* where you care about the ordering of messages relative to their own group but don't care about what order *a* and *b* messages came in with respect to each other.

FIFO queues allow to **ensure all messages sent to the queue are unique** by turning on the `Content-Based Deduplication` option. The deduplication option is controlled by the `Message Deduplication ID`.

## Max Receive Count

The max receive count for a queue must be between 1 and 1000.

## Visibility Timeout

The visibility time out controls how long a message is held after being viewed before it goes back into the queue and its receive count is incremented. Once a message is opened by a consumer, the consumer can either delete that message or leave it, the visibility time out is how long that consumer has to do that. During that time the message will not be moved out of the queue and other queue consumers will not be able to pick up the message.

The **default visibility timeout** is 30 seconds and the maximum is 12 hours.