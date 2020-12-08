---
layout: page
exclude: true
title: Cloudfront
---

Cloudfront in Amazon's CDN or **Content Delivery Network** which is a system of servers distributed geographically that serves content to users based on:

- user location
- webpage origin
- delivery server

Cloud is a **network and content delivery** feature.

An **edge location** is a located server which caches content to be delivered. Files are cached at edge locations according to a `TTL` or **Time to Live**. A `TTL` is given is seconds and is typically around 48 hours. The default Amazon TTL is 24 hours or 86400 seconds.

An **origin** is the location of the S3 bucket where the content was originally placed and which will be distributed by the CDN.

A **distribution** is a collection of edge locations that serve content.

Cloudfront **automatically roots user requests** to the fastest location to get content.

There are two types of cloudfront distribution:

- **Web Distribution** (fort websites)
- **RMTP** (for streaming adobe flash media RMTP media)

You can setup cloudfront to distribute S3 content when creating a new distribution.

You can use **restrict bucket access** to only allow users to access S3 content hosted via cloudfront through the CDN by changing the `Restrict Bucket Access` option to `Yes` when creating a distribution.

New cloudfront distributions typically take quite a while to set up at 30 minutes to an hour of creation time.

You can access cloudfront content by visiting the `Domain Name` of the cloudfront content which will be a random string followed by `.cloudfront.net`.

You can **use edge locations for writing and uploading files**.

You will be **charged for clearing cached objects**.

You can **delete a cloudfront distribution** by first selecting it and using the `Disable` option. It will take a while to be taken down and it can then be deleted.

## Caching

You can **disable cloudfront caching** (usually for the purposes of prototyping. By:

1. Navigating to the Cloudfront distribution you want to modify.
2. 





<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcyNTUwMDg5OCwtMTc4MzkxMjM4NywxNj
IxODkwNjczLDExNTk0OTgxNDBdfQ==
-->