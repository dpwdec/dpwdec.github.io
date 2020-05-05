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

# Table Commands

A single SQL statement can be **compressed to a single line or spread over multiple consecutive lines**. The following would be a valid query with *or* without new line breaks. Tabs and white spaces are also ignored when writing SQL queries.
```sql
SELECT name, age
FROM users
WHERE age > 20
ORDER BY age
```

Multiple SQL statements must be terminated with a `;` semi-colon.

You can **comment out SQL queries** using a set of  `--` dashes on a new line. 
```sql
SELECT name, age
FROM users
--WHERE age > 20
ORDER BY age
```

It is customary to **split long `SELECT` clause columns across new line breaks** with the **column names indented with a tab**.
```sql
SELECT
  name,
  age,
  height / 10
FROM users
```

## Insertion

To **insert a value into a table** use the `INSERT INTO` command combined with the `VALUES` command. There are two ways to accomplish this insertion. The first uses **implicit column order** to insert values. In the example below the arguments in `VALUES` will be inserted into `my_table` with the first argument of `4` going into column 1 of the table and second argument of `'some value'` into column 2.

```sql
INSERT INTO my_table
VALUES (4, 'some value')
```

## Retrieval

The main statements for SQL retrieval queries are `SELECT`, `FROM`, `WHERE` and `SORT BY` in that order. Using these clauses out of order will results in a `syntax error`.

### Selecting with `SELECT`

You can use the `SELECT` command to **specify a column of data to retrieve** from a table and the `FROM` command to **specify which table you want to retrieve data from**. This can be combined with the `WHERE` command which is used **specify a value in a column to match** as a way to find a record.

To **select ALL columns and records from a table** use the `*` argument with `SELECT`. The `*` means "ALL" in the context of SQL.
```sql
SELECT * FROM users
```

To **select a specific column** from a table specify that column after the `SELECT` command. In the below example this query will display the `name` column field of each record in `users`.
```sql
SELECT name FROM users
``` 

You can **select multiple columns** by submitting them as a list to `SELECT`.
```sql
SELECT name, age FROM users
```

The **order in which you submit column queries changes the output order**. If you switch the column `SELECT` specification the output will *also* be switched. For example, the query below will output `age` then `name` as opposed to the one above which will reverse this.
```sql
SELECT age, name FROM users
```

Although its not very useful immediately, you can **duplicate column output**. The query below which specifies `name` twice is valid. This can be useful if you wanted to compare a column directly with a column that had had some mathematical operation run on it. For example `age` and `age + 10` could be displayed next to each other with the duplicate `SELECT` query.
```sql
SELECT name, name, FROM users
```

You can **only display unique column values** by using the `DISTINCT` keyword. This will remove any duplicate values in the selected columns. In the query below even though the table might have many entries, countries only fall into a set of less than ten different continents (depending on who you ask) so the `DISTINCT` keyword will only return a unique list of possible continents from the data.
```sql
SELECT DISTINCT continent FROM countries
```

### Aliases with `AS`

You can **output a column with specified name** using the `AS` keyword. The example below will output the data from the `name` column of the `users` table but with the column name `alias` instead of `name`.
```sql
SELECT name AS alias FROM users
```

**Multiple word `AS` commands must be contained in `'` quote marks** otherwise you will get a syntax error:
```sql
SELECT name AS 'my alias' FROM users
```

### Matching with `WHERE`

The `WHERE` command supports a variety of comparison operators combined with table output values. The full list is:
- `=` - equality
- `>` - greater than
- `>=` - greater than or equal to
- `<` - less than 
- `<=` - less than or equal to
- `!=` - not equal to (this can also be communicated with `<>`)

To **select a specific record based on a column value** use the `WHERE` command with `=` and then the value. In the below example this query will display every column for each record the `name` value of which is "James". **String queries are case insensitive.**
```sql
SELECT * FROM users WHERE name = 'James'
```

You can **combine column and record selection**. Below example shows he ages of all records with the `name` of "James".
```sql
SELECT age FROM users WHERE name = 'James'
```

Here some **other examples of comparison operators** with `WHERE`:
```sql
SELECT name FROM users WHERE age > 20;
SELECT name FROM users WHERE age <= 20;
SELECT name FROM users WHERE age != 20
```

You can **perform date based comparison operations** using `>` for dates after the argument and `<` for dates before the argument and by submitting dates as strings in the form `%Y-%M-%D`. So if we wanted to match with all records with a `birth_date` after 1990 we would use the `>` operator combined with the date in string format.
```sql
SELECT name FROM users WHERE birth_date > '1990-01-01'
```

You can **combine `WHERE` clauses** using the `AND` command between comparison clauses. The following query selects all users with the `name` 'Jake' with an age greater than `40`.
```sql
SELECT name FROM users WHERE age > 40 AND name = 'Jake'
```

You can **match at least one `WHERE` clause** using the `OR` operator. Any record that matches one of these clauses will be returned.
```sql
SELECT name FROM users WHERE age > 40 OR name = 'Jake'
```

Logical operators also have an order of operations. **`AND` always takes precedence over `OR`.** 
```sql
```

You can **match a several distinct of possibilities** with the `WHERE` command by combining it with `IN` command which checks if a records value matches a list of possibilities. In the below example, if the value of `name` is `IN` the list submitted in the parentheses then the `age` field of that record will be displayed. 
```sql
SELECT age FROM users WHERE name IN ('James', 'John', 'Joe', 'Jackie')
```

You can also **match number values** using `IN` by omitting the quote marks. Below, the query returns the `name`s of users with `age` exactly 25 and 34.
```sql
SELECT name FROM users WHERE age IN (25, 34)
```

You can **match a range of numeric values** by using the `BETWEEN` command for a numeric field. The ranges are joined by the `AND` command. Range checking is **boundary inclusive**. Below, the query returns the `name` field for all records with an `age` field of value 25 - 34 inclusive. You cannot break up large numbers when submitting range queries with `,` or `_`.
```sql
SELECT name FROM users WHERE age BETWEEN 25 AND 34
```

### Numeric Operations

You can **execute numeric operations on output data** by including calculations as part of the `SELECT` query. You can use the `+`, `-`, `/`, `*` and `%` operators inside of the `SELECT` query. For example, if you were getting the areas of some countries that where thousands of kilometers square, you could rational those numbers by dividing them by `1000` within your query. This will then return the areas divided by that number.
```sql
SELECT area/1000 FROM countries 
```

You can **chain numeric operations** in a long form clause.
```sql
SELECT area * 1000 + 10 FROM countries
```

Numeric operations in SQL also **support `()` parentheses** for controlling expression order. 
```sql
SELECT (area + 10) * 1000 FROM countries
```

You can also **execute numeric operations using table data**. For example, instead of dividing area by a fixed number of `1000` we could divide by the `population` field of each record to see how much space each person in the country gets.
```sql
SELECT area/population FROM countries
```

It's useful to use `AS` to rename numeric queries based on what the calculation actually represents.
```sql
SELECT gdp/population AS 'per capita gdp' FROM countries
```

### Sorting

You can **sort data output** using the `ORDER BY` command followed by a column field. This will then sort the data output based on that field. Below, the query selects `name` and `age` from and then orders it by the name field.
```sql
SELECT name, age FROM users ORDER BY name
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
eyJoaXN0b3J5IjpbLTIxMTgyODM0NDEsLTU5NzYyNzUwMiwxMz
U4NTg4MjkyLDIxMTAxNDg5Niw2NTcwNzk3MzYsLTUwOTk1MTgy
MSwtMTY4NDE1Njc3OSwtMjk3OTI3NzY2LDE0ODQ5MTg0MjQsMT
cxOTE3ODM0MCwtNjM4MzcyNTE1LC0xOTIwMjA4MF19
-->