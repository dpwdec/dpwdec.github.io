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

You can **define a new database model** by inheriting from the `declarative_base` class of `sqlalchemy`. The `declarative_base` class is used for defining the model class and table in place, there are however options to define them separately. You also need to define the `__tablename__` attribute.
```py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
  __tablename__ = "users"
```

You can **define database columns and class properties** by importing the `Column` function from `sqlalchemy`, if you want to **specify column data types** you will also need to import those datatypes from `sqlalchemy`.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgxMzcxNzUxNywtMTA5NDUwNTIwOCwtMT
QzNTQ5OTAzNV19
-->