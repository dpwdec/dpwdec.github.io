---
title: OIDC
layout: page
exclude: true
---

OIDC or **Open ID Connect** is a service built *on top* of the OAUTH spec to allow developers to support authentication requests using the OAUTH flow. The OAUTH protocol was designed to only support authorization. That is, giving one application authorization to access functionality on another application. In this use case, identifying tokens are unnecessary, the application simply needs an access token which it can use to perform actions on its users behalf. So, when companies started using OAUTH to perform authentication it caused issues as they all developed their own ways to developing *on top* of the OAUTH spec to provided this authentication functionality.

The OIDC spec is an attempt to **standardise authentication using the OAUTH protocol**.

Instead of transmitting a standard **bearer token** during the OAUTH flow, instead the OIDC flow transmits a JWT or **JSON Web Token** to the client which encodes identifiable information about the user, such as user ID or email address.

There is generally a `userinfo` endpoint on the OIDC client that the 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNTAxMzk5OF19
-->