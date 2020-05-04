---
title: PostgreSQL
layout: page
exclude: true
---
## Getting Started
To install Postgresql use `homebrew`.
```
brew install postgresql
```
You can use brew to automatically run the postgres application in the background on your computer when you start your computer with the `brew services` command. This command will automatically start postgres when you log in.
```
brew services start postgresql
```
## PSQL
The **`psql` is a command line interface that allows use to interact with your database** by writing SQL. It is similar to the `irb` in Ruby. To start `psql` type the `psql` command followed by the name of a database you want to access. Postgres also comes with a default built in database called `postgres` which allows you to test queries on.
```
psql <database name>
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEyMDMwMjQ1NV19
-->