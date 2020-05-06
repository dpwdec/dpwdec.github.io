---
title: SQL
layout: page
exclude: true
---

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

## Creation

You can **create a new table** using the `CREATE TABLE` command followed by the table name and set of parentheses representing the columns of the table and their types.
```sql
CREATE TABLE users(id SERIAL PRIMARY KEY, name VARCHAR(60))
```

Each element in your table should have a unique ID. Using `SERIAL PRIMARY KEY` allows you to later on to add values to the table without specifying a new ID, with this data type tied to `id` when a new record is inserted the `id` field will be automatically generated with a unique id.

The `VARCHAR` element is approximately equal to SQL's version of string. It is simply a datatype that holds characters and is of some length. You can **specify the maximum length of this field** in an argument after it.

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

### Dates

You can **perform date based comparison operations** using `>` for dates after the argument and `<` for dates before the argument and by submitting dates as strings in the form `%Y-%M-%D`. So if we wanted to match with all records with a `birth_date` after 1990 we would use the `>` operator combined with the date in string format.
```sql
SELECT name FROM users WHERE birth_date > '1990-01-01'
```

### Combining with `AND` and `OR`

You can **combine `WHERE` clauses** using the `AND` command between comparison clauses. The following query selects all users with the `name` 'Jake' with an age greater than `40`.
```sql
SELECT name FROM users WHERE age > 40 AND name = 'Jake'
```

You can **match at least one `WHERE` clause** using the `OR` operator. Any record that matches one of these clauses will be returned.
```sql
SELECT * FROM users WHERE age > 40 OR name = 'Jake'
```

Logical operators also have an order of operations. **`AND` always takes precedence over `OR`.**  In the example below the query will returns records if the `age` is great than `40` *or* if the record's `name` is `'Jake'` *and* the person was born before `2010`.
```sql
select * FROM users WHERE age > 40 OR 
name = 'Jake' AND birth_date < '2010-01-01'
```

You can **change the order of logical operations** using parentheses. The following  would first match a record the `age` of which is great than `40` *or* with a `name` that is `'Jake'` and then only return it if the `birth_date` is also before `2010`.
```sql
select * FROM users WHERE (age > 40 OR name = 'Jake') AND 
birth_date < '2010-01-01'
```

It's recommended that you use parentheses anyway even when they don't change the order of logical operators to **make the intent of your queries clear**.
```sql
select * FROM users WHERE age > 40 OR 
(name = 'Jake' AND birth_date < '2010-01-01')
```

### Negating with `NOT`

You can **negate a logical query** using the `NOT` keyword:
```sql
select * FROM users WHERE NOT name = 'Jake' 
```

Negative logical queries **can also be combined with parentheses**:
```sql
select * FROM users WHERE NOT (name = 'Jake' OR age > 40)
```

### Checking Ranges with `IN`

You can **match a several distinct of possibilities** with the `WHERE` command by combining it with `IN` command which checks if a records value matches a list of possibilities. In the below example, if the value of `name` is `IN` the list submitted in the parentheses then the `age` field of that record will be displayed. 
```sql
SELECT age FROM users WHERE name IN ('James', 'John', 'Joe', 'Jackie')
```

You can also **match number values** using `IN` by omitting the quote marks. Below, the query returns the `name`s of users with `age` exactly 25 and 34.
```sql
SELECT name FROM users WHERE age IN (25, 34)
```

You can also **negate `IN` selection queries** using the `NOT` command:
```sql
SELECT * FROM users WHERE state NOT IN ('VA', 'FL', 'TX')
```

### Filling in the gaps with `BETWEEN`

You can **match a range of numeric values** by using the `BETWEEN` command for a numeric field. The ranges are joined by the `AND` command. Range checking is **boundary inclusive**. Below, the query returns the `name` field for all records with an `age` field of value 25 - 34 inclusive. You cannot break up large numbers when submitting range queries with `,` or `_`.
```sql
SELECT name FROM users WHERE age BETWEEN 25 AND 34
```

This same query can be written using conditionals but the `BETWEEN` query makes the code much cleaner.
```sql
-- example of the above example written with conditionals
SELECT name FROM users WHERE age >= 25 AND age <= 34
```

The `BETWEEN` command can also be used with date ranges. Dates should again be submitted in their string format.
```sql
SELECT * FROM users WHERE birth_date BETWEEN '1991-01-01' AND '2000-01-01'
```

### Finding Patterns with `LIKE`

The SQL `LIKE` command is used for **matching string patterns** in your database. The match criteria for these queries should come as strings. These **matching patterns are case insensitive.**

You can **use the special character `%` percent to indicate any number of characters**. In the example below, the query selects all users whose name starts with a `'J'` followed by any number of different characters.
```sql
SELECT * FROM users WHERE name LIKE 'J%'
```

The **`%` sign can be anywhere in the `LIKE` query** and used to check endings beginnings or just letter combinations in general.
```sql
-- return records the name of which ends in s
SELECT * FROM users WHERE name LIKE '%s'
-- return records the name of which contains a g
SELECT * FROM users WHERE name LIKE '%g%'
-- return records the name of which starts with a k, contains an l and ends in an e
SELECT * FROM users WHERE name LIKE 'k%l%e'
```

You can **use the special character `_` to match any single character**. It works the same as `%` but just with singular characters. In the query below a match will be found if the name is exactly 2 characters long and ends in a `'g'`.
```sql
SELECT * FROM users WHERE name LIKE '_g'
```

`LIKE` clauses **can be concatenated** with logical operators like `AND` and `OR` and with the **negative operator** `NOT`.
```sql
-- use two possible like clauses to match user's name
SELECT * FROM users WHERE name LIKE '____k' OR name LIKE '%ani%'
-- check for users whose name does not contain e
SELECT * FROM users WHERE name NOT LIKE '%e%'
```

### Matching with `REGEXP`

You can **use regular expressions** in SQL by invoking the `REGEXP` command. This command takes a regular expression literal as a string. It **does not need to be enclosed in `/../`** like regex in Ruby or other programming languages. The query below matches names that begin with either a `g` or a `j` followed by a number of characters and then ends in `field`.
```sql
-- matches the name 'Garfield'
SELECT * FROM users WHERE name REGEXP '[gj]\w+field$'
```

### Absence with `IS NULL`

When a column field is empty for a record in SQL it is described as being `null`. You can **return record's which have specified empty fields** by using the `IS NULL` command to match with them. The query below matches all users whose `phone_number` is empty in the database.
```sql
SELECT * FROM users WHERE phone_number IS NULL
```

You can **negate the `NULL` command** by inserting `NOT` into it to find records that do contain information.
```sql
SELECT * FROM users WHERE phone_number IS NOT NULL
```

### Numeric Operations with `+ - / * %`

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

You can also **place arithmetic operations within conditional `WHERE` style clauses**:
```sql
SELECT * FROM countries
WHERE area/1000 > 500000 AND population + 100000 <= 40000000
```

You can also **execute numeric operations using table data**. For example, instead of dividing area by a fixed number of `1000` we could divide by the `population` field of each record to see how much space each person in the country gets.
```sql
SELECT area/population FROM countries
```

It's useful to use `AS` to rename numeric queries based on what the calculation actually represents.
```sql
SELECT gdp/population AS 'per capita gdp' FROM countries
```

### Sorting with `ORDER BY`

You can **sort data output** using the `ORDER BY` command followed by a column field. This will then sort the data output based on that field. Below, the query selects `name` and `age` from and then orders it by the name field. `ORDER BY` **sorts data in ascending order** by default.
```sql
SELECT name, age FROM users ORDER BY name
```

You can **reserve the sorting order** by appending the `DESC` to the end of the query.
```sql
SELECT * FROM users ORDER BY name DESC
```

To **order results based on multiple fields** separate order fields by a `,` comma. The **priority of ordering is evaluated from left to right**. 
```sql
SELECT * FROM users ORDER BY age, name
```

## Updating

You can **update a database record** using the `UPDATE` and `SET` methods. The `UPDATE` is followed by a table name and the `SET` command specifies a table column to update. This can be combined with selection methods with `WHERE` to specify particular records to update.
```sql
UPDATE users SET name = 'baby' WHERE age < 3
```

## Deletion

You can **delete a record from a table** using the `DELETE FROM` command combined with the `WHERE` command to delete a specific record.
```sql
DELETE FROM users WHERE name = 'Jim'
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


## Documentation

You can document your database changes by placing initialisations SQL code within a `migrations` directory inside a `db` folder with the `.sql` extension.

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTYyODE0MjEwLC0xNjU1NTg5OTU1LDE4NT
Q0Njk3OCw5MzM4NTUzMDYsLTE0MDAzNDA5LC0xMDI4MzUwNjE1
LC04ODU5Nzk0MjAsLTEzOTQzNjEzNzYsNTI1MzE2Nzk1LDIzNz
Q5ODY4MywxNDUyMzA5Njg3LC0yMDQ5NDI3ODM2LC01OTc2Mjc1
MDIsMTM1ODU4ODI5MiwyMTEwMTQ4OTYsNjU3MDc5NzM2LC01MD
k5NTE4MjEsLTE2ODQxNTY3NzksLTI5NzkyNzc2NiwxNDg0OTE4
NDI0XX0=
-->