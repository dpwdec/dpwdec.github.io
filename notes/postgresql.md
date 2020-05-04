---
title: PostgreSQL
layout: page
exclude: true
---
## Getting Started
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

## Table Commands

### Insertion
To **insert a value into a table** use the `INSERT INTO` command.

## Case Sensitivity

Most **SQL commands and case insensitive**. This means you can  

## Quote Mark Rules


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MTU4OTY4MjYsMzExNzY1NDU4LDE3Nj
cwMzQ0MDUsLTMwNzc4NzIzNiw2Njg4NjA2ODFdfQ==
-->