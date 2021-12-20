---
layout: page
exclude: true
title: SQS
---

You can **create an SQS client that can receive messages in a queue** using the `AmazonSQSClient` in the `Amazon.SQS` library. The client takes credentials from accessing the topic and a region where the topic is configured. You need to also import the `Amazon` namespace to use the `RegionEndpoint` enum.
```csharp
var sqsClient = new AmazonSQSClient(awsCredentials, RegionEndpoint.EUWest1);
```

You can **recieve a message from an SQS queue** using the `RecieveMessagesAsync` method which takes a `ReviewMessageRequest` that takes a URL to the queue as well as the max number of messages to receive the number of seconds to wait while polling.
```csharp
var sqsResponse = await sqsClient.ReceiveMessageAsync(
    new ReceiveMessageRequest
    {
        QueueUrl = "<URL_FOR_THE_QUEUE>"
        MaxNumberOfMessages = 1,
        WaitTimeSeconds = 10
    }
);
```

You can **access the messages that were received** from the `Messages` property on the response. This is a list even if only one message is returned.
```csharp
foreach (var message in sqsResponse.Messages)
{
    // print body of message
    Console.WriteLine(message.Body);
}
```

You can **delete a specific message from the queue** once its been read by using the `DeleteMessagesAsync` with the url of the SQS queue and the `ReceiptHandle` property of the message you want to delete.
```csharp
await sqsClient.DeleteMessageAsync(
    "<URL_OF_THE_QUEUE>",
    sqsResponse.Messages[0].ReceiptHandle // delete first messages from those polled
);
```

You can **drain a queue** by continually polling and deleting messages from the queue until the queue is empty.
```csharp
do
{
    sqsResponse = await sqsClient.ReceiveMessageAsync(
        new ReceiveMessageRequest
        {
            QueueUrl = "<URL_OF_THE_QUEUE>"
            MaxNumberOfMessages = 1,
            WaitTimeSeconds = 10
        }
    );

    // break if the queue is empty of messages
    if (sqsResponse.Messages.Count == 0) break;

    sqsClient.DeleteMessageAsync(
        "<URL_OF_THE_QUEUE>",
        sqsResponse.Messages.First().ReceiptHandle // delete first messages from those polled
    );

    // sleep to not overload API and keep consistency of deletions and access to queue
    Thread.Sleep(1000);
} while(true)
```