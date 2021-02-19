---
title: DNS
layout: page
exclude: true
---

DNS (Domain Name System) 

When a DNS service contains a link to another DNS service this is known as a **merged** set of DNS records. For example, we might have service `A` that holds DNS records for a range of IPs on the domain `foo.com` and entry to `bar.com` which links to an upstream server `B` which holds records for a range of IPs on `bar.com`. We then have an application which needs information about `bar.com` IPs but can only send requests to service `A`. In this case `A` will propagate the request for the application upstream to service `B` which has all the records for `bar.com` and then return them down the chain to the application.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NzY1MzA2NDksLTE4MTY2ODM1OCwtMT
gxNjY4MzU4XX0=
-->