---
title: AWS CLI
layout: page
exclude: true
---

You can **use the AWS CLI to send requests to your mock AWS account** by using the `--endpoint-url` flag followed by the localhost endpoint of your localstack and then any commands. *The default localhost port for localstack is 4566.*
```bash
aws --endpoint-url=http://localhost:4566 <AWS_COMMAND> <ARGUMENTS>
```

For example, you could **create an SNS topic this way** using the `sns` command after the `--endpoint-url` flag.
```bash
aws --endpoint-url=http://localhost:4566 sns create-topic --name my-topic
```