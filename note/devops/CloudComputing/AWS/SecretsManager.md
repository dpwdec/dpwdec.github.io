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

You can **retrieve secret values** using the AWS CLI's `get-secret-value` command. There can be multiple versions of a secret curretnly
```bash
aws secretsmanager get-secret-value --secret-id <SECRET_NAME> --version-stage AWSCURRENT
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNzk5NDA5ODQsLTkwNDk3MDQ2LC0xMD
Y0MTg0Mzg2XX0=
-->