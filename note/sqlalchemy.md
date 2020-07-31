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

### Database Sessions

A database `Session` represents a factory for making connections to the database. From this you can make individual `session`s on which different ORM based procedures (such as querying or committing data) can be executed. SQLAlchemy uses the **unit of work** model which means that a `session` should be opened and closed whenever there is a need to transact the database. A `session` remains open until it is closed, committed or rolled back. By extension there are two scopes here, a **transaction scope** encapsulating the individual transactions and commands to the `session` and the **session scope** which encapsulates all transactions. 

You should **make a Session ONCE** during the configuration or set up of your application and then import that session into modules as needed. To **create a new Session** use the `session_maker` function to create a `Session` object, this will be the import that other parts of your application use.
```py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine("postgres://username:password@host/database_name")

Session =  sessionmaker(db)
```

You can **open a new local session** by using the `Session` object.
```py
session = Session()
```

You can **close a local session** by using the `close` method of the `session` object.
```py
session.close()
```

### Models

You can **define a new database model** by inheriting from the `declarative_base` class of `sqlalchemy`. The `declarative_base` class is used for defining the model class and table in place, there are however options to define them separately. You also need to define the `__tablename__` attribute. You can **define database columns and class properties** by importing the `Column` function from `sqlalchemy`, if you want to **specify column data types** you will also need to import those datatypes from `sqlalchemy`.
```py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class User(Base):
  __tablename__ = "users"

  firstname = Column(String)
  lastname = Column(String)
  age = Column(Integer)
```

Similar to `sessions` **in large applications with multiple models its recommended to create you `Base` class once** and then import it from a centralised set up section to modules that need to inherit from `Base`.

You can **create a new instance of a model class** as you would with any other python class.
```py
new_user = User(firstname="Nicolas", lastname="Copernicus", age=309)
```

You can **save a model class to the database** by using the `session` object to `add` the object to a list of database execution procedures and then `commit` to execute those procedures. Data does not get committed to the database until `commit` is called.
```py
session.add(new_user)
session.commit()
```

## Metadata

To **create database tables if they don't already exist** use the `create_all` method your model's base class. Importantly you **must import all the models you want to initialise into this method is executed** to ensure that all the relevant tables are added.
```py
Base.metadata.create_all(db)
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkwOTE1MjMzNSwtMTQwMzEyMDI1MywxNz
EyNTM5MjkxLC04NTg3NTE3NDUsLTEzOTU0MDM0MTUsLTE3ODc5
ODc4MTEsLTI3NDg2ODE3NCwxOTMzOTk4NDQ3LC04MTM3MTc1MT
csLTEwOTQ1MDUyMDgsLTE0MzU0OTkwMzVdfQ==
-->