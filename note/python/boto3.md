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


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcxMzE4MTA1MiwxMDQzNTk2NzQ2XX0=
-->