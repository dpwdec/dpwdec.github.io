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

You can **save a new instance of model class to the database** by using the `session` object to `add` the object to a list of database execution procedures and then `commit` to execute those procedures. Data does not get committed to the database until `commit` is called.
```py
session.add(new_user)
session.commit()
```

You can **save multiple instances of a model class to the database** by using the `add_all` method on the `session` object with an array of instance objects.
```py
session.add_all([
  User(firstname="Leonardo", lastname="Davinci", age=412),
  User(firstname="Vincent", lastname="Vangogh", age=102)
  User(firstname="Marcus", lastname="Aurelius", age=944)
])
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

You can **get the first element from a query result** by using the `first` method.
```py
user = session.query(User).first()
```

You can **get the length of a query result** by using the `count` method on the result object. The standard python `len` function does not work.
```py
result = session.query(User)
result.count()
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
user = session.query(User).filter(User.name == "Jimothy").first()
user.age += 2 # update Jimothy's age by 2 years
session.commit() # save the changes the database
```

You can **update records using `setattr` syntax**, this is [somewhat recommended][up] because it results in changes at a database level with verification.
```py
user = session.query(User).filter(User.name == "Jimothy").first()
setattr(user, 'age', user.age + 2)
session.commit()
```
[up]: https://stackoverflow.com/questions/9667138/how-to-update-sqlalchemy-row-entry

You can also **update records in place** by chaining the `filter` function with an `update` function that takes a `dict` as an argument with the target property as a key and the new property as the value of that key. If you want to **use existing record information during the update** you can access this from the class name. In the example below, the `User.age` property refers to the current record instance.
```py
session.query(User).filter(User.name == "Jimothy").update({"age": (User.age + 2)})
session.commit()
```

## Relationships

### One to Many

You can **define a basic one to many relationship between tables** by setting up a `Column` in your child class that uses the `ForeignKey` field with the argument being the parent table and the `id` of that table. 

You also **can also define a `relationship`** which describes the link between the two tables. The `relationship` defines a field on the classes that are created by submitting the name of the linked class as a string and then using the `back_populates` argument to link with the field in the linked class. The advantage of describing a `relationship` allows the `SQLAlchemy` ORM to track relationships explicitly so that you can load connected objects as part of queries on the parent class and also adds some protection against dropping tables that are dependent on one another.

The example below defines an `Address` class, a user can have many addresses. To define this relationship we create a `user_id` field in the `Address` class and set its `ForeignKey` to be equal to `TABLE_NAME.id` in this case `users.id`. Then we define a `user` field with a relationship to the `User` class (the first argument) and then a `back_populates` link to the `addresses` property in the `User` class which needs to be defined at the same time with a link to the `Address` class and another `back_populates` link to the `user` field. Both child and parent schemas are linked in this way.
```py
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

# --snip-- set up declaritive base

class  User(Base):
  __tablename__ =  'users'  

  id  =  Column(Integer,  primary_key=True)
  name =  Column(String)
  age =  Column(Integer)

  # define a relationship from user to address
  addresses =  relationship("Address",  back_populates="user")

class Address(Base):
  __tablename__ = 'addresses'

  id = Column(Integer, primary_key=True)
  email = Column(String)
  # foreign key link to user table defined here
  user_id = Column(Integer, ForeignKey('users.id')

  # define a relationship from address to user
  user = relationship("User", back_populates="addresses")
```

You can **add related child schemas to a model** by accessing them as a property on the model and adding the associated model into that field. The example below defines a new `User` and adds two `Address` objects which are automatically added to the corresponding table.
```py
lomothy = User(name="Lomothy", age=25)
lomothy.addresses = [
  Address(email="lomothy@lom-world.net"),
  Address(email="lomothy_lommington@googlemail.co.uk")
]
session.add(lomothy)
session.commit()
```

You can **retrieve related child records** by retrieving the parent model that has a relationship with those records and then accessing them as a property on that object. Under the hood a SQL query is issued when you access the `addresses` on an instance of the `User` class.
```py
lomothy = session.query(User).filter(User.name == "Lomothy").first()
lomothy.addresses # => ["lomothy@lom-world.net", "lomothy_lommington@googlemail.co.uk"]
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

## Testing

When testing your SQLAlchemy database across a module scope you **must close database sessions after testing** otherwise tests will hang forever. In `Pytest` this can be done with a `fixture` that `yield`s to the database tests with a `session` connection and then closes the `session` after the tests have run.
```py
@pytest.fixture
def  db_session():
  session =  Session()
  yield session
  session.close()
```

You can also **set the scope of the fixture** so that the fixture `yield`s to all tests in the assigned scope and then closes after that scope finishes.
```py
@pytest.fixture(scope="module")
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDY4NDE3ODksLTExNTcwOTA3MDQsLT
Q5NDM1MjgyMCwxNjQxNzQ2MzExLDgwODE4MjY2OSwtMjA0MTU5
OTMzMSw1NTAyODcyMTgsNzQzNjk4MzgsMTMzNzU4ODQwOCw2ND
Y3MzUyMjMsMzU3MzE2MDk3LDYzMDk2ODU3MCwzNDEyNDc1NzQs
ODcyNTQ1NDM4LC03NTcxNjE0ODIsLTE3NTE0MjM5NTksLTkwOT
E1MjMzNSwtMTQwMzEyMDI1MywxNzEyNTM5MjkxLC04NTg3NTE3
NDVdfQ==
-->