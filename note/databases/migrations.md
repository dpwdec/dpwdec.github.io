---
title: Migrations
layout: page
exclude: true
---

The rise of modern ORM frameworks that mapped database structures to database tables and entries meant that data became bound up to a degree with code structure. Database migrations are a way of **keeping the schema that define your database version controlled** in the same manner that the code that describes those structures are version controlled.

Database migration files are **granular scripted files which describe your data**, these are different depending on the tool you use. These migration files **evaluate to SQL format migrations files**. Indeed, you can write your migrations directly in SQL but this gives much more scope to introduce bugs and is more difficult.

Most popular languages and frameworks will have **automated support for generating migration files** but might require a small amount of manual changing. There are also **third party migrations tools**, such as Liquidbase or Flyaway that allow you to accomplish these tasks without being locked into a specific framework.

There are some **migration tasks that are hard to reverse**:
- Deleting columns
- Renaming columns
- Changing the datatype of columns that already contain data






<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAyNjQ1NDE2NCwxMDk4NDQ4MjUyLC0yMD
g4NzQ2NjEyXX0=
-->