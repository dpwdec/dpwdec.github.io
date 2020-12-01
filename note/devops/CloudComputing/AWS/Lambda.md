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

This **works if the S3 bucket and lambda are in the same AWS account** *and* access to the S3 bucket is not explicitly denied. Otherwise you must **enable permissions in S3** as well for the execution role associated with your lambda. You can do this by editing the S3 bucket's `bucket policy`.
```json
{
   "Id":"ExamplePolicy",
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"ExampleStmt",
         "Action":[
            "s3:GetObject"
         ],
         "Effect":"Allow",
         "Resource":[
            "arn:aws:s3:::AWSDOC-EXAMPLE-BUCKET/*"
         ],
         "Principal":{
            "AWS":[
               "arn:aws:iam::123456789012:role/ExampleLambdaRoleFor123456789012"
            ]
         }
      }
   ]
}
```

## AWS SDK

You **do not need to package the AWS SDK** with a lambda. The SDK is automatically installed on the default lambda run times.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MDI4ODczNzcsMzExMjMxMDM0LDExMz
c3MTM1NTAsMTA4NjkzMTI4OCwxOTk1OTQ2NzIyXX0=
-->