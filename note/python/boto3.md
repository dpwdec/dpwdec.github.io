---
title: Boto 3
layout: page
exclude: true
---

## SQS

You can **start using SQS** by referencing the `"sqs"` boto3 `resource` and adding a region with the `region_name` field.
```py
import boto3
sqs = boto3.resource("sqs", region_name="eu-west-1")
```

You can **access an SQS queue** using the `get_queue_by_name` method on the `sqs` resource object. It seems that you can only access SQS queues using the resource's name.
```py
queue = sqs.get_queue_by_name(QueueName="your-queue-name")
```

You can **access messages from the queue** using the `receive_messages` method on the `queue` object. It seems that there is no guarantee on the number of the messages that will be consumed and most of the times it seems to be 1.
```py
for message in queue.receive_messages():
  print(f"{message.body}")
```

You can **delete a message from the queue** using the `delete` method on the `message`.
```py
for message in queue.receive_messages():
  message.delete()
```

You can **load a message into a dictionary** using `json.loads` on the `body` of the message.
```py

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQxODkxNDQ4LDc5MTMzNzU0OCwtNzc2Mj
kzNTQ0LDEwNDM1OTY3NDZdfQ==
-->