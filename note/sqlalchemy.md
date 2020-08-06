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

### Schema

You can **create a primary key field** by setting the `primary_key` property to `True` when creating a database field. If this is an integer called `id` then SQLAlchemy will also manage auto-incrementing it when new records are added.
```py
class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  firstname = Column(String)
```

You can **set field parameters** on model properties such `String` length etc. by submitting them as arguments to the parameter type.
```py
firstname = Column(String(50))
```

You can **set fields to be unique within your database** by using the `uniqe` argument and setting it to `True` when defining a table property.
```py
username = Column(String, unique=True)
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

### Queries

You can **query a table for all records** and **return them as instances of the model class** by using the `query` method on the `session` object with the table model that you want to query as the argument. The `result` below is an iterable that contains instances of the `MyModel` class.
```py
result = session.query(MyModel)
```

You can **access the values contained in a result** through `for ... in` iteration or accessing values by index.
```py
# acess results using for ... in iteration
for model in session.query(MyModel):
  print(model.property)

# access results by index
result[0].property
```

You can **return an iterable of tuples from the database instead of objects** by submitting instance property names as the arguments to the `query` method.
```py
result = session.query(User.name, User.age)
```

You can **access destructure this tuple data in place** using `for ... in` syntax.
```py
for name, age in result:
  print(name, age)
```

You can **sort query results** by appending the `order_by` method to the end of `query` method and adding the name of an instance property to sort by.
```py
for user in session.query(User).order_by(User.name):
  # returns users sorted by name
```

### filter_by

You can **add filters to a query to match specific elements in your database** by appending the `filter_by` method to your query.
```py
# returns a list of all users called Jimothy who's age is 30
result = session.query(User).filter_by(name="Jimothy").filter_by(age=30)
```

### filter

You can **use a more general `filter` method** to create database queries with a more general structure. The `filter` method takes model properties as its parameters and evaluates them with the `==` equality operator. The example below shows the `filter_by` example re-written to use *just* `filter`.
```py
# returns a list of all users called Jimothy who's age is 30
result = session.query(User).filter(User.name == "Jimothy").filter(User.age == 30)
```

You can **write other arbitrary equality statements** queries using `filter`, for example, matching by `!=` not equal, matching by `>` great than etc.
```py
# match users who's name is not equal to clarence
result = session.query(User).filter(User.name != "Clarence")

# match users who's age is greater than 10
result = session.query(User).filter(User.age > 10)
```

You can **match filter strings by substring** using the `like` method on model properties. The example below will match `user`s who's `name` property contains the sub-string `"im"`.
```py
result = session.query(User).filter(User.name.like("%im%"))
```

The `like` operator is not consistent with case insensitivity across multiple systems. If you want to **ensure case insensitivity across systems** use the `ilike` method instead.
```py
# always case sensitive
result = session.query(User).filter(User.name.ilike("%im%"))
```

### update

You can **update a record** by retrieving it from the database, changing its contents and then committing using a session.
```py
result = session.query(User).filter(User.name == "Jimothy")
result[0].age += 2 # updat

```
	
## Dropping

You can **drop a specific table** by using the `__table__` property of a class with the `drop` method.
```py
MyModel.__table__.drop()
```

## Metadata

To **create database tables if they don't already exist** use the `create_all` method your model's base class. Importantly you **must import all the models you want to initialise into this method is executed** to ensure that all the relevant tables are added.
```py
Base.metadata.create_all(your_engine)
```

You can **drop all tables** by using `metadata` with the `drop_all` method.
```py
Base.metadata.drop_all(your_engine)
```

You can **drop a specific table** using `metadata` by specifying the table in the `tables` argument to the `drop_all` method.
```py
Base.metadata.drop_all(bind=your_engine, tables=[MyModel.__table__])
```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MjUyMjM3MDMsNzQzNjk4MzgsMTMzNz
U4ODQwOCw2NDY3MzUyMjMsMzU3MzE2MDk3LDYzMDk2ODU3MCwz
NDEyNDc1NzQsODcyNTQ1NDM4LC03NTcxNjE0ODIsLTE3NTE0Mj
M5NTksLTkwOTE1MjMzNSwtMTQwMzEyMDI1MywxNzEyNTM5Mjkx
LC04NTg3NTE3NDUsLTEzOTU0MDM0MTUsLTE3ODc5ODc4MTEsLT
I3NDg2ODE3NCwxOTMzOTk4NDQ3LC04MTM3MTc1MTcsLTEwOTQ1
MDUyMDhdfQ==
-->