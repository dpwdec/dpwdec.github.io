
---
title: Web Structures
layout: page
exclude: true
---
## Request Response Cycle
The request-response cycle is a **message exchange pattern** used widely on the web in which a caller "requests" something from an answerer who then "responds" with an answer to their request. There may be many intermediaries in this cycle that pass the request or response between themselves before returning it to the original caller. This cycle allows intermediaries to perform value-added functions on the request, such as encryption or compression while still ensuring that the caller with eventually receive a response.

## HTTP
HTTP or **Hyper Text Transfer Protocol** is a protocol that allows two applications to communicate across the web. HTTP is structured to on a **client** and **server** relationship in which hypertext documents are exchanged between the two parties. 

A **client** can be an application such as a web browser, but it can also be another server or API call requesting data for some other purpose or even the command line, such as in the case of the `cURL` command. The essential structuring distinction here is that [one party requests and the other responds](#request-response-cycle).

When sending an HTTP request the client sends a text string containing a request for a specific resource to a URL as well as information about how they want to interact with the resource.

How the client interacts with a particularly resource is communicated using the **request method**. There are several different types of **request method**, however the most common four are `GET`, `POST`, `PUT` and `DELETE`:

You can **view the HTTP request method for a particular resource** by using the Chrome Development Tools in the `network` tab and viewing the 

HTTP resources are identified using a **URL** or **Uniform Resource Locator** that points to where the Hypertext is stored over the internet.

Hypertext is a structured document that uses **hyperlinks** between nodes. HTML or **Hyper Text Markup Language** is used to manipulate the hypertext so that the `client` can request different types of media (such as images, text or data) from the server.


HTTP is an **application protocol** and is based on TCP/IP which is a **communication protocol** or **transport protocol**. It is important to keep this distinction in mind as TCP/IP is designed for transferring data whereas HTTP is designed to allow applications to format data in an effective way and share it between each other.


network tabe chrome dev tools

200 --> ok
404 --> error

http status dogs

### Telnet
You can install `telnet` to check HTTP connections using `brew install telnet`.
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAxNDcxNzIxMiwyMTE2NjU5NjU3LC02Mj
gyMDY3NDYsNjQyMDcwMzY1LDE3OTE0ODc4MTAsOTMwNjc2NDQ3
LDE2NDAyNzkxNywtMjE0NDIwMDkyN119
-->