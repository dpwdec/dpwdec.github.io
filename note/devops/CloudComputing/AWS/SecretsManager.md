---
layout: page
exclude: true
title: Secrets Manager
---

**Secrets Manager** is a service similar to Vault for storing sensitive credentials that needed by services.

## Manual Secret Creation

You can **create a new secret** by going to the `Secrets Manager` console and clicking `Store New Secret`.

You can **store any type of data as a set of key-value pairs** by using the "Other type of secrets" option when storing a new secret. A single secret can accomplish several pairs of data.

You can **view sample code in a range of languages that retrieves your secret** in the "sample code" section when creating your secret.

## Retrieval

You can **retrieve secret values** using the AWS CLI's `get-secret-value` command.
```bash
$ aws secretsmanager get-secret-value --secret-id <SECRET_NAME> --version-stage AWSCURRENT
```

You can **retrieve data about a secret** such as ARN, name etc. but *not* the actual encoded string using the `describe-secret` command.
```bash
$ aws secretsmanager describe-secret --secret-id <SECRET_NAME>
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNDg3NTc2ODMsLTkwNDk3MDQ2LC0xMD
Y0MTg0Mzg2XX0=
-->