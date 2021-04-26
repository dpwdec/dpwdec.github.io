---
layout: page
exclude: true
title: Simple Notification Service
---

SNS uses a "PubSub" model - a single *publisher* sends a message and many *subscribers* consumer that message.

The publisher **publishes there message** to a **topic**. A topic is a just a type of message that can be consumed. For example, a topic could be an order triggered on an e-commerce website and then many services could listen to that topic for when new messages are published.

SNS topics can be consumed by:
- HTTP Endpoints
- SQS
- Texts
- Email

SNS can work **application to application** (HTTP / SQS) OR **application to person** (Email / Texts).

`disableSubscriptionsoverrides` property in retries can allow subscribers to the topic to set overrides on how they want to consume an SNS topic.

You can **filter which subscribers get a message** from a topic by using a **subscription filter policy**. This usually relates to contextual data published along with the message to the topic by the publisher. For example, an order topic that marks messages as either "games" or "movies" type purchases.

By default SNS will try and send messages to subscribers for 48 hours. After that period the message will be lost unless **dead letter queue** or **DLQ** is enabled which is a store of messages that were not received successfully. The DLQ is just an SQS service that you specify.

It seems like this queue needs to be checked manually and republished back to SNS if you want to try and get the messages out to the subscribers that couldn't reach them. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjUwNjE3MTI0LDEwNTMyODc2NzgsMjU3NT
QxMjExLDE3NjUzMjEwMTcsLTEzODY1OTY3OTVdfQ==
-->