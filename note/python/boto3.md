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


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MzExNDMyMTBdfQ==
-->