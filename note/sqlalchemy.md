---
title: SQL Alchemy
layout: page
exclude: true
---

SQL Alchemy is a multi-abstraction SQL database wrapper for python.

You can **connect to a database** using the `create_engine` command. If you are **connecting to a PostgreSQL database** you must also `pip3 install psycopg2` to facilitate connection.
```py
db = create_engine("postgres://username:password@host/database_name")
```

## Raw SQL

You can **execute arbitrary SQL statements** on your database by using the `db` object's `execute` method with an string formatted SQL as its argument.
```py
db.execute("CREATE TABLE users (name text, age text, height text)")
```

## ORM

You can use the SQLAlchemy ORM for a much higher level database abstraction. In this workflow you define classes that map to database tables and then connect to them using `sessions`. 


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNjM0MTM2MjMsLTEwOTQ1MDUyMDgsLT
E0MzU0OTkwMzVdfQ==
-->