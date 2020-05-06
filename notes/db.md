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

A big advantages of relational databases are their ability to offer **data consistency** across multiple copies of the database. These copies are called database **instances**. Relational databases can immediately propagate changes in the data in one instance to other instances. This can take longer or not be possible at all with non-relational databases.

Relational databases also implement a form of **commitment**. This means that the database has rules on how to manage data. For example, there may be pieces of information that can only be retrieved and committed together, such that database will refuse to retrieve or commit data to its records if all information is not present. This linking of multiple complex records is called **atomicty**.

Relational databases also follow a set of **integrity rules** that ensure data is kept consistent. For example, one integrity rule might be that you cannot have a duplicated row in a table. Furthermore relational databases can **store access procedures** so that need not be re-written multiple times and can be implemented in specific ways.

To manage multiple applications or user accessing data simultaneously relational databases have a **locking** function that stops users from accessing database elements if they are being updated. If the database locks an entire table this can be detrimental to performance, however, some databases offer individual record level locking. There is also a **concurrency** system manages this access from multiple users to the same table ensuring that each user or application receives the correct information.

## Entity Relationships

There are three main types of relationship that data can have:

- One to one
- One to many
- Many to many

### One to one relationship

A **one to one** relationship encompasses direct relationships between an object and the data it stores. For example, a `class` will have one official `group page` and the `group page` will have a one `class` associated with it. In this case the `id` field of one object's database representation can be used as the `id` for another object's database because the relationship is unique.

`class` table:

| id | class_name |
| --- | --- |
| 1 | april_2020
| 2 | may_2020 |

`group page` table:

| class_id | url |
| --- | --- |
| 1 | http://www.group-page-april.com |
| 2 | http://www.group-page-may.com |

### One to many relationship

A **one to many relationship** describes a situation in which one record in a table can be associated with *one or more* records in another table. An example of this would be a `class` and its `students`. You will only have one `april_2020` class but that class might encompass many students who are all *members* of that class. In this case we would place a **foreign key in the table with the many relationship** so that in our table that tracks `students` each member would have a field that records the `class` they are a member of as a foreign key that points to the singular class. This way the key that points to the unique class can be duplicated in the `students` table while continuing to point to a single entity in the `class` table.

`class` table:

| id | class_name |
| --- | --- |
| 1 | april_2020
| 2 | may_2020 |

`students` table:

| id | name | class_id |
| --- | --- | --- |
| 1 | Dec | 1 |
| 2 | Dan | 1 |
| 3 | Dely | 2 |

### Many to many relationship

A **many to many relationship** occurs when one record can be associated with many other records and many other records can be associated with that record. For example, we could have a system for tagging students so that teachers can keep track of how the students are progressing with tags like `'needs improvement'` or `'requires more support`'. A single tag could be applied to many students and like wise a single student could have many tags applied to them thus resul

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTgzNjYwNDAwLDIzMzEwODE2OCwzNTM0NT
MyNjddfQ==
-->