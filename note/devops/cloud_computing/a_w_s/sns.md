---
layout: page
exclude: true
title: Simple Notification Service
---

SNS uses a "PubSub" model - a single *publisher* sends a message and many *subscribers* consumer that message.

The publisher **publishes there message** to a **topic**. A topic is a just a type of message that can be consumed. For example, a topic could be an order triggered on an e-commerce website and then many services could listen to that topic for when new messages are published.

SNS can work **application to application** OR **application to person**.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzODY1OTY3OTVdfQ==
-->