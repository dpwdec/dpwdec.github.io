---
layout: page
exclude: true
title: SNS
---

You can **create an SNS client that can send messages** using the `AmazonSimpleNotificationServiceClient` in the `Amazon.SimpleNotificationService` library. The client takes credentials from accessing the topic and an region where the topic is configured. You need to also import the `Amazon` namespace to use the `RegionEndpoint` enum.
```csharp
var snsClient = new AmazonSimpleNotificationServiceClient(awsCredentials, RegionEndpoint.EUWest1);
```

You can **send a message to an SNS topic** using the `PublicAsync` method on your SNS client. This takes a `PublishRequest` object that requires a message and an ARN of the topic the message is being sent to.
```csharp
var response = await snsClient.PublishAsync(
    new PublishRequest
    {
        Message = "Message",
        TopicArn = "<ARN_OF_TOPIC>"
    }
);
```

