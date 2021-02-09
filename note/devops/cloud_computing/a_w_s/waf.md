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

WAFs are defined using Web ACLs (Web  Control Lists) and can limit requests based on:

- Scripts in requests
- IP Address ranges
- Geographical locations
- Requests length (such as query strings)

These Web ACLs are different from the ACLs that are used to configure 

You can **create a WAF ACL rule that lets ALL traffic in** by using the `0.0.0.0/32` specifier for range of IP addresses that the WAF should allow.
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTY0MDExNzU5LDEwNzM1OTk0NjcsLTI4Mz
k4OTA0OF19
-->