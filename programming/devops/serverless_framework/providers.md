---
title: Providers
layout: page
exclude: true
---

## AWS

You can **configure where your infrastructure is deployed** using the `region` property of the `provider` object.
```yaml
provider:
  name: aws
  region: eu-west-1
```

You can **configure AWS permissions for all lambdas in a serverless deployment** using the `iamRoleStatements` property of the `provider` object. You can create roles manually for your lambdas using policy statements in the `resources` section of the serverless file but this is generally only advisable if you special role cases within the lambdas you are deploying. Generally if you have a set of lambdas that all need permissions to similar stuff it's better to just use the `iamRoleStatements` section and then may override the role for a single lambda in a special case. In the example below a role that allows dynamodb access to a specific table is created for *all* lambdas in the deployment.
```yaml
provider:
  name: aws
  iamRoleStatements:
    - Effect: Allow
      Action:
        - dynamodb:*
      Resources:
        - some:arn:here
        
```