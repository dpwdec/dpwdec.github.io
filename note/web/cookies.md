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
- **Persistent cookies** are saved and automatically removed when their expiration date is reached. 




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMjY5NTQxNDMsODYyNzcyMzQ3LDk3OT
U1NDM3Niw2MDY5NzIwNTksLTcxMTE1NjU5NywxMTc4MDk3NTQ0
XX0=
-->