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

You can **access messages from the queue** using the `receive_messages` method on the `queue` object.
```py
for message in queue.receive_messages():
  print(f"{message.body}")
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzkxMzM3NTQ4LC03NzYyOTM1NDQsMTA0Mz
U5Njc0Nl19
-->