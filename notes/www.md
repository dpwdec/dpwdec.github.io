
---
title: Web Structures
layout: page
exclude: true
---
## Request Response Cycle
The request-response cycle is a **message exchange pattern** used widely on the web in which a caller "requests" something from an answerer who then "responds" with an answer to their request. There may be many intermediaries in this cycle that pass the request or response between themselves before returning it to the original caller. This cycle allows intermediaries to perform value-added functions on the request, such as encryption or compression while still ensuring that the caller with eventually receive a response.

## Web Request Components
Several different components make up a web request. If we image the client and server that communicate through a web request as two locations, the different components are physical elements that allow you to travel to and from these locations and move goods between them.
- An **internet connection** is the basic physical basis by which a client and server can communicate. It is like the road linking them.
- **TCP/IP** are like transport mechanisms that tel

## HTTP
HTTP or **Hyper Text Transfer Protocol** is a protocol that allows two applications to communicate across the web. HTTP is structured on a **client** and **server** relationship in which hypertext documents are exchanged between the two parties. 

A **client** can be an application such as a web browser, but it can also be another server or API call requesting data for some other purpose or even the command line, such as in the case of the `cURL` command. The essential structuring distinction here is that [one party requests and the other responds](#request-response-cycle).

Hypertext is a structured document that uses **hyperlinks** between nodes. HTML or **Hyper Text Markup Language** is used to manipulate the hypertext so that the `client` can request different types of media (such as images, text or data) from the server. This information about the type of request such as the **request method**, HTTP version, or resource needed is contained in the **HTTP header** for the client's request the body of which will be empty. The server then replies with its own HTTP document containing the **status code** in the header and the resource in the body of the document.

![enter image description here](https://mdn.mozillademos.org/files/13827/HTTPMsgStructure2.png)

When sending an HTTP request the client sends a text string containing a request for a specific resource to a URL where the server is located. HTTP resources are identified using a **URL** or **Uniform Resource Locator** that points to where the Hypertext is stored over the internet. You can also use an IP address to identify a server but URLs are much more user friendly. 

### HTTP Cycle

First the client sends a request to a URL. How the client interacts with a particularly resource when they make a request is communicated using the **request method**, stored in the HTTP header. There are several different types of **request method**, however the most common four are `GET`, `POST`, `PUT` and `DELETE`:
- `GET` requests simply return a resource unchanged. Requesting the code for a page from a URL such as [https://www.youtube.com/](https://www.youtube.com/) for example.
- `POST` requests send data new data to the server for storage. Posting a comment a cringey poorly spelt comment on a youtube video for example.
- `PUT` requests are used for updating existing resources. Editing that comment you just made to correct the basic spelling errors but not reducing its cringiness at all for example.
- `DELETE` requests are used to remove data from the server. Deleting that ill advised and poorly written youtube video comment for example.

After a client sends an HTTP request with a method, they will receive a response from the server with a **status code** which describes what happened to the request. The two most common **status codes** are `200` and `404`.
- `202` means everything went "OK" and the request was successful.
- `404` means something went wrong and the request resource was not found.

If the request worked the server also returns a **message body** which contains the resource the client requested. This could be code for an HTML page that the client's browser renders or if its an API call it could be JSON object.

You can **view the HTTP request method, status codes and body for a particular resource/request** by using the Chrome Development Tools in the `Network` tab and viewing the `Headers` section of a request. 

### Protocol Type

HTTP is an **application protocol** and is based on TCP/IP or **Transport Control Protocol / Internet Protocol** which is a **communication protocol** or **transport protocol**. It is important to keep this distinction in mind as TCP/IP is designed for transferring data whereas HTTP is designed to allow applications to format data in an effective way and share it between each other.

### Telnet
You can install `telnet` to check HTTP connections using `brew install telnet`.
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1MDI2ODcwNyw4NjExOTY0MjIsMTc1OT
I4NjUyOCw3NjA5Njg1NTcsLTE0OTA5NjYyOSwyMTE2NjU5NjU3
LC02MjgyMDY3NDYsNjQyMDcwMzY1LDE3OTE0ODc4MTAsOTMwNj
c2NDQ3LDE2NDAyNzkxNywtMjE0NDIwMDkyN119
-->