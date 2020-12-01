---
layout: page
exclude: true
title: Lambda
---

Lambda's run using an **execution role** which is just an `IAM` role that the lambda assumes the permissions of when it runs.

## S3

You can **give your lambda access to an S3 bucket** by modifying the policies on the lambda's **execution role**. You can do this by:

1. Going the execution roles `Permissions` tab in `IAM`
2. Choose `Add inline policy` and then the `JSON` tab
3. Add the following code into the policy and `Create Policy`

```json
{ 
  "Version": "2012-10-17", 
  "Statement": [ 
    { 
       "Sid": "ExampleStmt", 
       "Action": [ "s3:GetObject" ], 
       "Effect": "Allow", 
       "Resource": [ "arn:aws:s3:::AWSDOC-EXAMPLE-BUCKET/*" ] 
     } 
   ]
 }
```

This **works if the S3 bucket and lambda are in the same AWS account** otherwise you must **enable permissions in S3** as well.
```

```

## AWS SDK

You **do not need to package the AWS SDK** with a lambda. The SDK is automatically installed on the default lambda run times.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxOTc3NTkyNSwxMTM3NzEzNTUwLDEwOD
Y5MzEyODgsMTk5NTk0NjcyMl19
-->