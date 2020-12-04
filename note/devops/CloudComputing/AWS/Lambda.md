---
layout: page
exclude: true
title: Lambda
---

Lambda's run using an **execution role** which is just an `IAM` role that the lambda assumes the permissions of when it runs.

## Deployment

You can **deploy a lambda using the AWS CLI** by creating an execution role and creating a lambda pointing to that execution role with the code for the lambda zipped up.

You can **create a new IAM role for lambda execution** using the `iam` command line tool and the `create-role` command.
```bash
$ aws iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json
```

## SAM

SAM is a **Severless Application Model** and allows you to define the structure of complex lambda's using YAML, such as external dependencies and other integrated services (like Databases, Buckets etc.)



## S3 Access

You can **give your lambda access to an S3 bucket** by [modifying the policies](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-execution-role-s3-bucket/#:~:text=Create%20an%20AWS%20Identity%20and,the%20Lambda%20function's%20execution%20role.&text=Verify%20that%20the%20bucket%20policy,the%20Lambda%20function's%20execution%20role.) on the lambda's **execution role**. You can do this by:

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

This **works if the S3 bucket and lambda are in the same AWS account** *and* access to the S3 bucket is not explicitly denied. Otherwise you must **enable permissions in S3** as well for the execution role associated with your lambda. You can do this by editing the S3 bucket's `bucket policy` to the follwing:
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
eyJoaXN0b3J5IjpbLTI0MzczNjMwMSwxNDcwNTIzMTg4LDgxMT
kyMzcyNywzMTEyMzEwMzQsMTEzNzcxMzU1MCwxMDg2OTMxMjg4
LDE5OTU5NDY3MjJdfQ==
-->