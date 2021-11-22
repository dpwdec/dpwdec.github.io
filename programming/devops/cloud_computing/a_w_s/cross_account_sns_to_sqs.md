---
layout: page
exclude: true
title: Cross Account SNS to SQS
---

To **programatically subscribe a queue to a topic in another account**, you must

- Subscribe *from* the account where the queue exists (*this is to avoid the need to "confirm" the subscription manually, if you create the subscription from the account where the queue exists no confirmation is required*)
- Create a policy on the account where the queue exists to have `sns:Subscrtibe` permissions on the account where the topic exists (*so that the account with the queue can link across the two accounts*) this can be done by creating a role in the queue's account with permissions for SNS on the topci account
- Create a policy on the queue to allow `SQS:SendMessage` permissions from the topic the queue subscribes to (*if this is not configured the queue and topic will be linked but the queue won't actually recieve any messages because it hasn't given the topic permission to actually send it anything, this is the most error prone step when setting up as the functionality fails silently*)