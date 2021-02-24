---
title: DNS
layout: page
exclude: true
---

DNS or **Domain Name System** is a service that holds IP address records for domains. You can query a DNS service with a human readable domain name path and it will return the IP address of that the calling service can then route to.

When a DNS service contains a link to another DNS service this is known as a **merged** set of DNS records. For example, we might have service `A` that holds DNS records for a range of IPs on the domain `foo.com` and entry to `bar.com` which links to an upstream server `B` which holds records for a range of IPs on `bar.com`. We then have an application which needs information about `bar.com` IPs but can only send requests to service `A`. In this case `A` will propagate the request for the application upstream to service `B` which has all the records for `bar.com` and then return them down the chain to the application.

DNS services run on port 53 of whatever IP address they point to. Does DNSMasq work by acting as the server on the local host and then forwarding requests when an nslookup is called?

On linux machines `resolv.conf` also factors into this in some way?
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MTUwMDMzM119
-->