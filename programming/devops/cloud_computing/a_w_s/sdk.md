---
layout: page
exclude: true
title: SDK
---

## Credentials

You can find information about SDK credentials [here](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/loading-node-credentials-shared.html).

You can **give the AWS SDK automatic access to AWS credentials** by saving your AWS account credentials in a `.aws` folder in your home directory in a file called `credentials`.
```yaml
[default]  
aws_access_key_id = <YOUR_ACCESS_KEY_ID>` 
aws_secret_access_key = <YOUR_SECRET_ACCESS_KEY>
```

You also **may need a to add a session token** if you are using session based AWS access which you can do by adding the `aws_session_token` property to the `credentials` file as well as the key and secret key properties.
```yaml
aws_session_token = <YOUR_SESSION_TOKEN>
```

## S3

### Javascript

You can **load a resource from S3 using the AWS SDK** with the `S3` object.
```js
var AWS = require('aws-sdk');

getS3Content = () => {
  var s3 = new AWS.S3();
  var params = { Bucket: "my-bucket", Key: "my-file.txt" };
  var data = await s3.getObject(params).promise();
  try {
    data = await s3.getObject(params).promise();
  } catch (e){
    data = e.toString();
  }
  return data.Body.toString();
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMxNTcxMjQzLC0xMDY3ODQyMzk1LDY0OD
IzNTQ1NCwtMTQ3MDg1ODY0MV19
-->