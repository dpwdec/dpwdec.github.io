---
title: PostgreSQL
layout: page
exclude: true
---

## Installing PostgreSQL

To install Postgresql use `homebrew`.
```
$ brew install postgresql
```
You can use brew to automatically run the postgres application in the background on your computer when you start your computer with the `brew services` command. This command will automatically start postgres when you log in.
```
brew services start postgresql
```
## PSQL
The **`psql` is a command line interface that allows use to interact with your database** by writing SQL. It is similar to the `irb` in Ruby. To start `psql` type the `psql` command followed by the name of a database you want to access. 

```
$ psql <database name>
```
Postgres also comes with a default built in database called `postgres` which allows you to test queries on. If you are successful at accessing the database to write queries you will get a console input with a `#`.
```
$ psql postgres
postgres=#
```
You can **display a list of all databases** using the `\l` command. This prints a table displaying `Owner`s, `Access Privileges` among other database information.
```
$ \l
```

To **exit `psql`** use the `\q` command.
```
$ \q
```

To **create a new database** use the `CREATE DATABASE` command. It is optional whether you contain your database name inside `"` double quote marks.

```
$ CREATE DATABASE "name_of_database";
```

You can **connect to a database** using the `\c` command.
```
$ \c database_name
```

You can **display a list of tables in your database** using `\dt`
```
$ \dt
```

To **display a list of columns from your table** use the `\d+` command followed by the name of the table who's columns you want to show.
```
$ \d+ <table name>
```

## Connecting to Postgres with Ruby

Ruby requires the `PG` library to connect to a postgres database. You can do this by:
- Using the `require 'pg'` (useful for `irb` code)
- Using the `gem 'pg'` in your gem file.

Using the `pg` gem gives you access to the `PG` class which is wrapper the methods of which can be used to access and manipulate a postgres database running on your machine. The database must be up and running for the `PG` class to interact with it and yield results.

To **connect to a database** use the `connect` method with the symbol `dbname` and the name of the database you want to connect to. This method yields a `PG::Connection` object that represents a connection to your database.
```ruby
connection = PG.connect(dbname: 'my_database')
```

You can **execute arbitrary SQL commands on your database** using the `PG:Connection` object's `exec` method. This takes a SQL in 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzODMzMzk3XX0=
-->