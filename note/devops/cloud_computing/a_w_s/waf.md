---
layout: page
exclude: true
title: WAF
---

AWS WAF stands for **Web Application Firewall** and is used to control how HTTP(S) requests to:

- Cloudfront Distributions
- API Gateways
- Application Load Balancers
- Amazon GraphQL API

You can **view and configure amazon's web application firewall service** by going to the `Amazon Firewall Manager` dashboard.

WAFs are (confusingly) defined using ACLs (Access Control Lists) and can limit requests based on:

- Scripts in requests
- IP Address ranges
- Geographical locations
- Requests length (such as query strings)

You can **create a WAF ACL rule that lets ALL traffic in** by using the `0.0.0.0/32` specifier for range of IP addresses that the WAF should allow.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY5NzQ1NjY4MywxMDczNTk5NDY3LC0yOD
M5ODkwNDhdfQ==
-->