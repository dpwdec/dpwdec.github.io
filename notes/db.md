---
title: Databases
layout: page
exclude: true
---
## Relational Databases
A relational database is a type of database that stores data so that it can be accessed in *relation* to other pieces of data. Each row in a table is called a **record** and has its own unique index, called a **key**. By mapping these keys as fields into other tables databases can be made to act in a relational manner.

Relational databases arose from a need to standardise how developers stored data. Previously each company or team of developers might have their own method of storing data making interface between programs time consuming and difficult to maintain. Relational databases standardised this interaction. The **Standard Query Language** also arose as a result of this, the regular syntax of which can be highly optimised leading to fast and reliable performance.

Relational databases' physical storage and logical storage are separated. This means that databases files can be moved and renamed without effecting the name of tables inside the database and not interfering with how people access the database information.

| Physical storage | Logical storage |
| ---  | --- 
| the name of the databases | database tables |
| how users connect to the databases | table indexes |
| | table views

Relational databases also follow a set of **integrity rules** that ensure data is kept consistent. For example, one integrity rule might be that you cannot have a duplicated row in a table.



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUwMjYzOTk5NV19
-->