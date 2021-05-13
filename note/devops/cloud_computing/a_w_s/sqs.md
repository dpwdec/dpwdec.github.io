---
layout: page
exclude: true
title: Simple Queue Service
---

You can **see how many messages are available to be consumed** on the root SQS interface.

You can **put messages into the DLQ** based on how many times the message was received. This means, the number of times an application or user polled the queue and received a message but did not delete them. This implies there was some issue with the message and so it needs to be stored in the DLQ.

The **DLQ must match the queue type for the main queue**, whether that be a **standard** queue or a **FIFO** queue.

## FIFO Queues

FIFO queues allow to **ensure all messages sent to the queue are unique** by turning on the **Content-Based Deduplication** option. The d
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU5NjY3NDI0OCwtMTk5MTYzNjk2Myw5Nz
M0OTAyOTVdfQ==
-->