---
layout: page
exclude: true
title: Lambda
---

Lambda's run using an **execution role** which is just an `IAM` role that the lambda assumes the permissions of when it runs.

## CLI

You can find more information about Lambda deployment with the AWS CLI [here](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html).

### Deploying a new lambda

You can **deploy a lambda using the AWS CLI** by creating an execution role and creating a lambda pointing to that execution role with the code for the lambda zipped up.

You must **create a new IAM role for lambda execution** using the `iam` command line tool and the `create-role` command. This should come along with a `trust-policy.json` file in the same directory which you run the command from that defines the roles privileges.
```bash
$ aws iam create-role --role-name <LAMBDA_ROLE_NAME> --assume-role-policy-document file://trust-policy.json
```

The **associated trust policy** is:
```json
{  
"Version": "2012-10-17", 
"Statement": [ 
    {  
     "Effect": "Allow", 
     "Principal": {  
       "Service": "lambda.amazonaws.com" 
      }, 
      "Action": "sts:AssumeRole" 
    } 
  ] 
}
```

You can **also create the policy inline**:
```bash
$ aws iam create-role --role-name lambda-ex --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

You can **create a function** and **deploy it for the first time** by `zip`ping your code and then using the the `create-function` utility on `lambda` with the code and execution role ARN for the lambda passed in.
```bash
$ aws lambda create-function --function-name my-function \ 
  --zip-file fileb://function.zip --handler index.handler --runtime nodejs12.x \ 
  --role <LAMDA_ROLE_ARN>
```

### Updating

You can **update your lambda's code** using the `update-function-code` command with a zip file to the new code.
```bash
$ aws lambda update-function-code \
    --function-name  <LAMBDA_NAME> \
    --zip-file fileb://my-function.zip
```

## Dependencies

You can **package dependency code** with your lambda.

### Node

For Node based lambda's you can simply `zip` up your lambda as normal using a recursive `zip` command to also zip the `node_modules` folder. These dependencies can then be `require`d when the lambda is called. An example file structure for the lambda is shown below.
```
my-lambda
├── index.js
└── node_modules
	├── dependency.js
    └── anotherDependency.js
```

You can then **zip your lambda recursively** using the `-r` flag targeting the folder which the lambda is stored in.
```bash
$ zip -r my-function.zip .
```

## SAM

SAM is a **Severless Application Model** and allows you to define the structure of complex lambda's using YAML, such as external dependencies and other integrated services (like Databases, Buckets etc.)

## Context

The **second argument to a lambda function** is a `context` object which **contains metadata about the function**. Examples are in Javascript but similar functions exist in a range of languages.

You can **get the name of the currently running function** by using the `functionName` property, this is whatever name was set in AWS.
```js
exports.handle = async (event, context) => {
  return context.functionName // "my-function"
}
```

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

You can **load a resource from S3 using standard AWS SDK integration** in the body of your lambda once these permissions are set up.

## AWS SDK

You **do not need to package the AWS SDK** with a lambda. The SDK is automatically installed on the default lambda run times.

## SecretsManager

You can **give a lambda access to a SecretsManager secret** by modifying the lambda's associated execution role in IAM to have access to secrets manager. To do this:

1. Navigate to IAM and the Lambda's associated execution role.
2. Go to `Add Inline Policy`.
3. Use the visual editor to give the execution role access to secrets manager.

## Lambda @ Edge

The **Lambda @ Edge** service allows you to run lambda code at an edge location that is triggered by requests by to content from the CloudFront CDN.

Lambda @ Edge is **only available in the `us-east-1` region**.

Lambda @ Edge **functions like a middleware** intercepting CloudFront requests and modifying them in some way. There are four options for `CloudFront Events` that can trigger the Lambda @ Edge:

- `Origin Request` - triggers when a client makes a request (can be used for authenticating or modifying requests)
- `Origin Response` - triggers when the origin returns content (can be used for modifying data and meta-data in the response)
- `Viewer Request`
- `Viewer Response`

You can **create a Lambda @ Edge** by:

1. Creating a CloudFront distribution for some S3 content. Make sure the S3 bucket and content is set to public access. This data can be **stored in any region**.
2.  Creating a regular lambda in the `us-east-1` region with appropriate Lambda @ Edge code.
3. Go to `Add Trigger` and select `CloudFront` as the trigger type. You then need to provided the ARN of the CloudFront distribution that you want to trigger the Lambda and pick the type of event.
4. Wait for the Lambda to be deployed and then try and access a file in your distribution to check that it is running.

**BEWARE:** Lambda @ Edge code is **also cached at edge locations** so if you want to prototype a solution and tests changes you will need to temporary disable caching as part of the CloudFront distribution that triggers the lambda.

It's also important to note that **the cloudfront distribution is still considered to be the agent making the request** after the lambda @ Edge function has returned. So any authentication or access management to resources further along should be set as if they were being accessed by cloudfront.


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxMTk0MjQzNCw4MDY1ODU1NjYsLTczMz
k0OTU3MywtMTM4MTQ0ODY5NiwtODg1OTM3NDEzLDEwMzA5MjQ3
NCwxNzM3MzA4MTkxLDkxNjQ3OTIwLC0yNDM3MzYzMDEsMTQ3MD
UyMzE4OCw4MTE5MjM3MjcsMzExMjMxMDM0LDExMzc3MTM1NTAs
MTA4NjkzMTI4OCwxOTk1OTQ2NzIyXX0=
-->