---
title: REST
layout: page
exclude: true
---

## REST APIs

A **REST** API or **Representational State Transfer** API is a software routing style for handling requests to a server and returning information. REST uses several different verbs to describe how requests to a server are routed and what they are intended to do.

 1. `GET` - *Retrieve* a resource
 2. `POST` - *Create a new* resource
 3. `PUT` - *Replace* a resource *in its entiety*
 4. `PATCH` - *Update* a resource
 5. `DELETE` - *Delete* a resource

## HATEOAS

**HATEOES** stands for **Hypermedia as the Engine of Application State** and describes a REST architecture where a client requests information about a resource and then uses the response from the server to actions that are returned about the resource. Therefore the client needs no knowledge of the API beforehand to interact with it but can **use hypermedia links in the response** to find actions to take against the resource. The **actions available that can be taken by client on a resource change depending on the state of the resource**. For example, we could have an API that returns account information.
```
GET service.com/accounts/12345
```

The API could then return a **JSON response with links to the possible actions that could be taken which the client can make further requests against**.
```json
{
    "account": {
        "account_number": 12345,
        "balance": {
            "currency": "usd",
            "value": 100.00
        },
        "links": {
            "deposit": "/accounts/12345/deposit",
            "withdraw": "/accounts/12345/withdraw",
            "transfer": "/accounts/12345/transfer",
            "close": "/accounts/12345/close"
        }
    }
}
```

However if the 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI2NTQ1MTAyOSwtMTI3MjM2Mzk4M119
-->