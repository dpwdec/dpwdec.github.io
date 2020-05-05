---
title: SQL
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

## Table Commands

### Insertion

To **insert a value into a table** use the `INSERT INTO` command combined with the `VALUES` command. There are two ways to accomplish this insertion. The first uses **implicit column order** to insert values. In the example below the arguments in `VALUES` will be inserted into `my_table` with the first argument of `4` going into column 1 of the table and second argument of `'some value'` into column 2.

```sql
INSERT INTO my_table
VALUES (4, 'some value');
```

### Retrieval

You can use the `SELECT` command to **specify a column of data to retrieve** from a table and the `FROM` command to **specify which table you want to retrieve data from**. This can be combined with the `WHERE` command which is used **specify a value in a column to match** as a way to find a record.

To **select ALL columns and records from a table** use the `*` argument with `SELECT`. The `*` means "ALL" in the context of SQL.
```sql
SELECT * FROM my_table
```

To **select a specific column** from a table specify that column after the `SELECT` command. In the below example this query will display the `name` column field of each record in `my_table`.
```sql
SELECT name FROM my_table
``` 

You can **select multiple columns** by submitting them as a list to `SELECT`:
```sql
SELECT name, age FROM my_table
```

To **select a specific record based on a column value** use the `WHERE` command with `=` and then the value. In the below example this query will display every column for each record the `name` value of which is "James".
```sql
SELECT * WHERE name = 'James'
```

You can **combine column and record selection**. Below example shows he ages of all records with the `name` of "James".
```sql
SELECT age WHERE name = 'James'
```

You can **combine `WHERE` with other logical operators** like `>` greater than and `<` less than. Below, the query selects all records with an `age` field greater than 20.
```sql
SELECT name WHERE age > 20
```

You can **match a several distinct of possibilities** with the `WHERE` command by combining it with `IN` command which checks if a records value matches a list of possibilities. In the below example, if the value of `name` is `IN` the list submitted in the parentheses then the `age` field of that record will be displayed. 
```sql
SELECT age WHERE name IN ('James', 'John', 'Joe', 'Jackie')
```

You can also **match number values** using `IN` by omitting the quote marks. Below, the query returns the `name`s of users with `age` exactly 25 and 34.
```sql
SELECT name WHERE age IN (25, 34)
```

You can **match a range of numeric values** by using the `BETWEEN` command for a numeric field. The ranges are joined by the `AND` command. Range checking is **boundary inclusive**. Below, the query returns the `name` field for all records with an `age` field of value 25 - 34 inclusive. You cannot break up large numbers when submitting range queries with `,` or `_`.
```sql
SELECT name WHERE age BETWEEN 25 AND 34
```

You can **execute numeric operations on output data** by including calculations as part of the `SELECT` query. For example, if you were getting the areas of some countries that where thousands of kilometers square, you could rational those numbers by dividing them by `1000` within your query. This will then return the areas divided by that number.
```sql
SELECT area/1000 FROM countries 
```

## Case Sensitivity

Most **SQL commands and case insensitive**. This means you *can* write your SQL queries using lowercase, however, its recommended to avoid this as it makes your queries much less readable and creates difficulties when you do have to deal with the case sensitivity of table names and values.

```
# both of these are valid queries, however the latter is more readable
$ select * from my_table
$ SELECT * FROM my_table
``` 

## Quote Mark Rules

You should **submit `varchar` string type values inside single `'` quote marks**. For example, when using an `INSERT` query

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ5MTQ4NDY1NSwxNDg0OTE4NDI0LDE3MT
kxNzgzNDAsLTYzODM3MjUxNSwtMTkyMDIwODBdfQ==
-->