---
layout: page
exclude: true
title: STS
---

You can **display the ARN of your current AWS user** by using the `--get-caller-identity` flag.
```bash
aws sts --get-caller-identity
```

For one role to assume another role there **only needs to be assumption permissions on the target role**. As long as the role you want to role says its ok for another role to assume it, the role you are assuming from does not require any additional permissions to allow it to take assumption activities.