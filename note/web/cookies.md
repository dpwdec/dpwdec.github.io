---
title: Cookies
layout: page
exclude: true
---

**Cookies** are **key-value pairs of information** stored locally in a browser. 

### Cookie Setting and the Set-Cookie Header

Cookies are **set by the server** using the `Set-Cookie` header in the HTTP response object. When the browser receives the `Set-Cookie` header it stores a cookie locally
```
Set-Cookie: foo=bar;
```

Cookie properties are set by appending a `;` semi-colon separated list of key-value paired properties to the cookie name assignment. 
```
Set-Cookie: foo=bar; max-age=60; secure
```

You can **set multiple cookies** by including multiple `Set-Cookie` headers in the server response.

Most servers will include some friendly API for setting cookies on a HTTP response. But, at the base level all they are doing is  manipulating the `Set-Cookie` header.

A cookie is **updated** when a server sends a new cookie. This **can happen asynchronously** if you have a page that makes asynchronous calls to a server that update cookie then that will be displayed in the browser.

When a cookie **expires** it is deleted by the browser and *not* sent to the server.

If a user leaves a website for some time the cookie will remain stored on their machine so that when they return to a website their cookie (if not expired) can be sent back to the server to retrieve a information about the user. This is essentially the technology that allows user sessions to function. 

### Cookie Types

There are **session cookies** and **persistent cookies**.

- **Sessions cookies** are stored in RAM and never saved to the hard-drive. These are generally cookies that don't have a `Max-Age` or  or `expires` property set so that they are deleted when you leave a website. They are generally used for maintaining user privacy.
- **Persistent cookies** are saved and automatically removed when their expiration date is reached. These are primarily used for **authentication** and **personalisation**.

**Third party cookies** are cookies created by applications not directly linked the website that the user is on. *How can this happen?* One common way is adverts. Adverts loaded onto a webpage by third party advertisers have permission to add cookies to your browser even if you never click on the adverts. These cookies can harvest analytics information and history and then use this to collect information.


### HTTP Only

Cookies that are marked with `httponly` **cannot be edited by the client side scripts**. They are not visible to client side scripts and manipulation and can only be edited when sent to the server. Attempts by client side scripts to read cookies marked with `httpOnly` will cause the browser to simply return an empty string.

You can **see a list of cookies that can be edited client side in your browser** by using the `cookie` property of the `document` object. It returns a list of cookies in a string as key-value pairs, with each pair separated by a `;` semi-colon and single white space.
```js
document.cookie // => 'foo=baz; bar=qux'
```

### Path

The `path` attribute on a cookie is a security feature that **controls where a cookie can be sent**. If a cookie's `path` attribute matches the path which is requested by the client then the cookie will be sent with the request otherwise it will not be sent. For example if we had a cookie with the `/about` path.
```
Cookie: foo=bar; Path=/about
```

If this cookie was sent to the `http://some-website.com/about` then *the cookie will be passed through* and will be accessible by the server from the request. However, if the cookie was sent to `http://some-website.com/contact` (or any other url path that does not match the cookie's path property)  then *the cookie will not be sent by the browser*.

If **no path is set** then the cookie defaults to an empty `/` path. 

A **cookie with an empty path will be sent to any path** by the client.

### Domain

Cookies **are scoped by a `domain` property**. A cookie can **only be sent to a domain that matches the domain it was created on**, thus stopping cookies from being sent cross site. Browsers will block cookies from being sent to any domain other than the domain the cookie was created on.

Browsers also do not allow you access the `domain` property of a cookie directly in scripts etc.

Browsers will **block cookies that come with a different domain than domain on which they are received**.
```
Set-Cookie: foo=bar; domain=another-
```
 

## Client Side Cookie Editing

You can **update a cookie client side** by simply setting a key-value pair string on the `document.cookie` property. This *does not* overwrite the entire list of cookies and is intelligent enough to simply add or modify a cookie.
```js
//retrieve existing cookies
document.cookie // => 'foo=baz; bar=qux'
// modify existing cookie
document.cookie = 'foo=eggs'
document.cookie // => 'foo=eggs; bar=qux'
// add new cookie
document.cookie = 'spam=ham'
document.cookie // => 'foo=eggs; bar=qux; spam=ham'
```

You can **only set one cookie at a time** using this method.

**Updating cookies on the client side** is **not used especially often** with the preference being to update on the server side instead.

You can **set properties on cookies** in the same way as as the `Set-Cookie` header, by appending a `;` semi-colon separated list of key-value paired properties to the cookie name assignment. The example below creates a cookie that lives for `60` seconds and is `secure` so that it can only be sent over the https protocol. *You can set boolean cookie properties to true simply by including the property keyword*.
```js
document.cookie = 'foo=bar; max-age=60; secure'
```

To curtail the malicious editing of cookies, cookie meta-data like `path`, `domain` and `expires` are not visible on client side scripts, like Javascript's `document.cookie`. 




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NjU3ODMwMzAsMjEyOTExMDI1OSwtMT
A0MTkxNDM1OSwxODM0MjYwMTkyLC0xODQzMTgwMDAyLDU5ODM5
NjM5NiwtMTk5MjUxOTMyMSwtMzkxMzY4Njc1LC0xNDc2NzQ4Mj
c2LDYzNTEwNjU2OSwxNjA0ODUwMzc1LC05NzA5NzA2MzIsLTc3
NzI3OTQ3MCwtMTQ2NDMwMTc5MiwxMjEyNDM3OTA3LDkwODc2Nz
czNCwtMzMwNTkwNDcxLDg2Mjc3MjM0Nyw5Nzk1NTQzNzYsNjA2
OTcyMDU5XX0=
-->