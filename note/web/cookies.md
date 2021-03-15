---
title: Cookies
layout: page
exclude: true
---

**Cookies** are **key-value pairs of information** stored locally in a browser. 

If a user leaves a website for some time the cookie will remain stored on their machine so that when they return to a website their cookie (if not expired) can be sent back to the server to retrieve a information about the user. This is essentially the technology that allows user sessions to function. 

A cookie is **updated** when a server sends a new cookie. This **can happen asynchronously** if you have a page that makes asynchronous calls to a server that update cookie then that will be displayed in the browser.

When a cookie **expires** it is deleted by the browser and *not* sent to the server.

There are **session cookies** and **persistent cookies**.

- **Sessions cookies** are stored in RAM and never saved to the hard-drive. They are deleted when you leave a website and used for maintaining user privacy.
- **Persistent cookies** are saved and automatically removed when their expiration date is reached. These are primarily used for **authentication** and **personalisation**.

**Third party cookies** are cookies created by applications not directly linked the website that the user is on. *How can this happen?* One common way is adverts. Adverts loaded onto a webpage by third party advertisers have permission to add cookies to your browser even if you never click on the adverts. These cookies can harvest analytics information and history and then use this to collect information.

### HTTP Only

Cookies that are marked with `httponly` **cannot be edited by the client**. They are not visible to client side scripts and manipulation and can only be edited when sent to the server.




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEwMTk3NTIzOCwtMzMwNTkwNDcxLDg2Mj
c3MjM0Nyw5Nzk1NTQzNzYsNjA2OTcyMDU5LC03MTExNTY1OTcs
MTE3ODA5NzU0NF19
-->