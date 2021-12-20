---
layout: page
exclude: true
title: Credentials
---

You can **get AWS credentials from credentials configured in your environment** using the `EnvironmentVariablesAWSCredentials` object from the `Amazon.Runtime` library. This allows you to easily instantiate AWS credentials which include session tokens.
```csharp
var awsCredentials = new Amazon.Runtime.EnvironmentVariablesAwsCredentials();
```

You can **create assume role credentials** using the `AssumeRoleAwsCredentials` from the `Amazon.Runtime` library with the credentials that *can assume* that role, the ARN of the role and a session name.
```csharp
var assumeRoleCredentials = new Amazon.Runtime.AssumeRoleAwsCredentials(
    awsCredentials, // credentials object created from environment or other means
    "arn_of_role_to_assume",
    "some_session_name");
)
```