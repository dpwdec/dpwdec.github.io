---
title: Migrations
layout: page
exclude: true
---

The rise of modern ORM frameworks that mapped database structures to database tables and entries meant that data became bound up to a degree with code structure. Database migrations are a way of **keeping the schema that define your database version controlled** in the same manner that the code that describes those structures are version controlled.

Database migration files are **granular scripted files which describe your data**, these are different depending on the tool you use. These migration files **evaluate to SQL format migrations files**. Indeed, you can write your migrations directly in SQL but this gives much more scope to introduce bugs and is more difficult.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYzODYwMjIyNSwxMDk4NDQ4MjUyLC0yMD
g4NzQ2NjEyXX0=
-->