---
title: OAuth
layout: page
exclude: true
---

OAuth2.0 is used for **authorization** *NOT* authentication. The purpose of the technology is not authenticate the user as real to one service, its to authorize one service to 

When a user **gives permission to one application to access another application on their behalf** this called **delegated access**.

## OAuth Flow

The target service returns a `authorization token` that only allows for the limited permissions that the user approved.

The source service save the `auth token` and uses it every time the user wants it to access the target service.

## Access Token

The access token is a JWT token
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NzIwMTEyNTZdfQ==
-->