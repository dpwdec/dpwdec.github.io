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

You can **execute arbitrary SQL statements** on your database by using the `db` object's `execute` method with an string formatted SQL as its argument.
```py
db.execute("CREATE TABLE user")
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgwOTQwMjYxNF19
-->