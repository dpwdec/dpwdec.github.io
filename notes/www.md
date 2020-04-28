
---
title: Web Structures
layout: page
exclude: true
---
## Request Response Cycle
The request-response cycle is a **message exchange pattern** used widely on the web in which a caller "requests" something from an answerer who then "responds" with an answer to their request. There may be many intermediaries in this cycle that pass the request or response between themselves before returning it to the original caller. This cycle allows intermediaries to perform value-added functions on the request, such as encryption or compression while still ensuring that the caller with eventually receive a response.

## Web Request Components
Several different components make up a web request. If we image the client and server that communicate through a web request as two locations, the different components are physical elements that allow you to travel to and from these locations and move goods between them.
- An **internet connection** is the basic physical basis by which a client and server can communicate. This is like the road linking them.
- **TCP/IP** are transport mechanisms that move data between a client and server.  They are like a car.
- **DNS** is used to look up where the server the client is trying to contact is. This is like an address book.
- **HTTP** is a protocol that defines how the client and server communicate with each other. This like the language you use to request goods once you reach a location.

### Web Request Sequence
Web requests work by using the above components to send information.
- First the client encodes a request with what they would like and how they would like it in an HTTP request.
- Next the client retrieves the IP address of the location of the server they are trying to send a request to from the `DNS`.
- Next the client sends their request using `TCP/IP` to the destination server.
- The server receives the request and serves a resource based on it as another response HTTP document.
- This document is sent back to the client via `TCP/IP`
- When the client receives the HTTP response it is displayed or used in some way.
![enter image description here](https://lh3.googleusercontent.com/xfaaNyJZZRn5n9H76o_Z2g9MGthn0tdN0_vhQXIdgzWhOz28VVXrLccvJEgr9_W388oTpUGT_bAMkgEnvWbO-szlpPznm3RoyDw95CT1A70m3mMBTz4-5DWxjZX2iYF5NomfwTbx4b0HAYkq51lI_SGyFi-OV2XLTdtblBLwoun6HNRVUjsc9EkY83N3TUm-6QkYbsnLRzBuHIe2tkrd2icnO381Nvy7aFiv5TWy6CJ1pRdtJCNnO8N_OV1WdpP7bgZLAzsYY9HwOX6wgujkRhcA3DXaUQao0XInYkql24fdSkmkUR0HsyUEqLWtqjOzv4MIE-vAgzUXSbx9upGU8R7D15m6PQ0qspdytWopAbY9NL-135qEw-YU_4XNPqgqnd0KgHbFSac6fkag3Ljzq6w_HTlFhw7VgzEe5JPGC1zkSTA8x-HbPu43COwLsmakTL8aHKjWFlXFATh_cIDIw4m0-xUh_lMC9taPqm3eXU9MR6eVwELVZAi6gUVCJfGQxMt5vDfVXaEfbyR3eWfvho73huiws5sLnENZ4_CUstkLOhst3CqCnNQ70WYg7BYIcobXWiV_LoVVG_SVZrgJyTvFZzKV5q5352fMUCXKgVC9BNXDVeQz-EOUCgW-WYVNtbW8UUtEPkbgcOzRuCJTrDtunke6GDZT26vKvQAsBA0bGm_Bnczvz1LoHoBY6g=w686-h406-no)

## HTTP
HTTP or **Hyper Text Transfer Protocol** is a protocol that allows two applications to communicate across the web. HTTP is structured on a **client** and **server** relationship in which hypertext documents are exchanged between the two parties. 

A **client** can be an application such as a web browser, but it can also be another server or API call requesting data for some other purpose or even the command line, such as in the case of the `cURL` command. The essential structuring distinction here is that [one party requests and the other responds](#request-response-cycle).

Hypertext is a structured document based around the use of **hyperlinks** between nodes. HTML or **Hyper Text Markup Language** is used to manipulate the hypertext so that the `client` can request different things from the server in different ways. This information about the type of request such as the **request method**, HTTP version, or resource needed is contained in the **HTTP header** for the client's request, in the body of the client request is other data that the server might use (such as when submitting a form) but often this can be empty. The server then replies with its own HTTP document containing the **status code** in the header and the resource in the body of the document. Syntactically, the only essential difference between HTTP requests and HTTP responses is the first line of the header.

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

### Headers
#### Request Header
The HTTP request header contains a **method**, a **url extension to a directory** and a **host**. There are other things in the request but these are the three most important elements. The `/` points to a directory within the host URL. A `/` without anything after it indicates the root directory. In the example the HTTP request points to the `about` directory of `some-website.com`.
```
[Example Request Header]
GET /about --> method and directory
...
Host: some-website.com --> the host
```
The request header can also contain a `Accept-Language` property that will change what language HTTP content is returned in if there is an available resource in another language.

#### Response Header
The HTTP response header contains a **status code**, a **content type**, a **content length**. The **content type** allows the server to tell the client what sort of data is incoming. For example, if an HTTP request yielded some video and image content in the body of the response then that data will need to be decoded and display differently from text code for an HTML website. The **content length** is counted in characters.
```
[Example Response Header]
200 OK --> status code
content-length: 400
content-type: text/html
```
Some **other HTTP status codes** are:
- `307` means that the resource the client is trying to access was **temporarily moved**. The HTTP response body for this code will contain a new URL pointing to where the resource is stored for the moment. Most browsers will automatically redirect to this address.
- `301` means that the resource the client is trying to access has been **permanently moved**. Its format is very similar to the `307` code and contains a new URL. However, the fact that it has permanently changed gives a single to the client to update an stores or bookmarks they have of where the information is stored.
- `401` means that the resource is **gone** and has been **deleted** permanently.
- `500` means that the HTTP part of the server doesn't really know what went wrong. This comes with the `internal server error` message and usually arises when some program on the server has been asked for a piece of information and not returned what was expected. Essentially its something that the HTTP doesn't have knowledge of why it happened, they just know they didn't get the right information to return.

There are **different families of HTTP status codes** based on the first number of the code.
-   `1xx`  (Informational): Request received, continuing process.
-   `2xx`  (Successful): The action was successfully received, understood, and accepted.
-   `3xx`  (Redirection): Further action needs to be taken in order to complete the request.
-   `4xx`  (Client Error): The request contains bad syntax or cannot be fulfilled.
-   `5xx`  (Server Error): The server failed to fulfil an apparently valid request.


### Protocol Type

HTTP is an **application protocol** and is based on TCP/IP or **Transport Control Protocol / Internet Protocol** which is a **communication protocol** or **transport protocol**. It is important to keep this distinction in mind as TCP/IP is designed for transferring data whereas HTTP is designed to allow applications to format data in an effective way and share it between each other.

### Queries
When you send an HTTP request you can submit data with your request by appending it to outgoing URL. This called a query. Queries are structured using **key-value pairs**. They are initiated with `?` question mark and multiple value pairs are separated with an `&` ampersand.
```
www.some-website.com/about?name=tog&age=300
```
The example above sends a request to the `some-website` url as well as two key-value pairs. This is method of sending data directly via the url **can only be used with a `GET` request**. When submitting from a form or other source using a `GET` request the data sent by the client will be appended to the url when sent. For example, an HTML form with `GET` as its submit method will append the data submitted with the form to the url that it points to.

By contrast the `POST` method **adds query data to the body of the HTTP request**. Usually this query body would be empty, but when using `POST`, an HTTP method designed for sending data, the data is wrapped in the body of the request. This also means that **data sent with `POST` is obscured from the destination URL**, it is entirely invisible except for what is explicitly displayed on the page by the server response.
```
[Example Post HTTP Request]
POST / HTTP/1.1
Accept: */*
...
User-Agent: HTTPie/2.1.0

name=YourNameHere --> query content submitted in the body
```

### Version


## DNS
DNS or **Domain Name Servers** are a way of translating the nice readable URL address of a website that the client wants to visit into a real, unique server IP that can be visited. Some where the website the client is visiting is running on a physical server that needs to be contacted. The DNS allows the client to look up where the server is so that they can send their request there.

## HTTPie

HTTpie can be used to make HTTP requests to urls the command line. You can **make a basic HTTP request** using the `http` command. This will return the entire HTTP document for that request including its header meta-data.
```
http https://www.google.co.uk/
```
You can make an HTTP request that also **displays the data for outgoing request** by using the `-v` flag.
```
http -v https://www.google.co.uk/
```
You can **make a `POST` request** using the `-f` flag with the `POST` keyword and submit key-value pairs after the url.
```
http -f POST https://some-website.com/ key=value
```

## Telnet
You can install `telnet` to check HTTP connections using `brew install telnet`.

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MjY4MTcwMTgsNjc3ODMyMjk1LDE2Nz
k5MjgxMDcsODc1MjcxNjg4LC04MTA5OTkyMTUsNTc0NTgwNywx
ODc3MzA2ODgwLC02NTAyNDY1MDMsLTE2MjI5MzgzMjUsODYxMT
k2NDIyLDE3NTkyODY1MjgsNzYwOTY4NTU3LC0xNDkwOTY2Mjks
MjExNjY1OTY1NywtNjI4MjA2NzQ2LDY0MjA3MDM2NSwxNzkxND
g3ODEwLDkzMDY3NjQ0NywxNjQwMjc5MTcsLTIxNDQyMDA5Mjdd
fQ==
-->