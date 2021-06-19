---
title: Datamapper
layout: page
exclude: true
---

## Datamapper

Datamapper is an ORM similar to active record that allows you to use ruby objects and code to execute database queries. You can get **datamapper to work with postgres** by using the `dm-postgres-adapter` gem. To start using datamapper add the `data_mapper` gem to your gem file.
```ruby
gem 'data_mapper'
gem 'dm-postgres-adapter'
```

### Database Connection

To **connect to a postgres database** with Datamapper use the `Datamapper.setup` function in a call from your main Sinatra file. Ideally, place this code in a `configuration` block so that it can contact a different database depending on whether you are in a `:development`, `:test` or `:production` environment.
```ruby
configure :test do
  DataMapper.setup :default, 'postgres://localhost/database_name_test'
end

configure :development do
  DataMapper.setup :default, 'postgres://localhost/database_name'
end
```

### Models

A Datamapper model is a class that is defined to match the structure of a table. For example, if you had a table called `users` which stored an `id` and a `name` then you would have a corresponding object called `User` that would represent the data from that table as a singular record. As a developer **all you need to do is created the appropriate class with the properties you would like stored**. Datamapper will then automatically create the corresponding table in your database (with a pluralised name).

To set up a datamapper model `include Datamapper::Resource` at the start of your class and then use the `property` tag to **define fields using symbols in your class that will be translated into columns in your database**.  The `Serial` class is a custom `data_mapper` property that is the equivalent of setting your `id` field to be a `PRIMARY SERIAL KEY`. 

Apart from this **you can treat these class files as regular ruby classes** and define custom methods attributes and accessors as required.
```ruby
# models/user.rb
require 'data_mapper'

class User
  include DataMapper::Resource

  property :id, Serial
  property :name, String
end
```
You will also **need to `require` these model files in whatever script you are using to setup, configure and migrate your database** so that the model structure can be pushed into a table structure in your database.

### Migration

To **migrate your models to the database** i.e. automatically create and update the tables in your corresponding postgres server use `Datamapper.auto_migrate!` or `Datamapper.auto_upgrade!`. The **former will clear all data from the database** whenever it is run whereas the **latter will try and reconcile the data already in the database with changes**. I place these calls inside the same file with the `configuration` blocks that creates a connection to the database.

### Queries

To **get a record by `id`** use the `.get` class method. This returns an object that is an instance of the class which wraps the data from the database.
```ruby
# gets user with ID one.
User.get(1)
```

You can **get all records for a class** using the `.all` class method which returns an array of `User` object instances populated with the data from the database.
```ruby
# get all user records
User.all
```
You **search by non primary parameter** by combining the `.all` method with a symbol specifying which class parameter you want to search by the value to search for. This returns an array even if there is only one match.
```ruby
# get all user records with the name Dec
User.all(User.name => 'Dec')
```
To **add a new record to the database** simply create a new instance of your model class with the data you want to save and use the `.save` method to commit it to the database.
```ruby
# saves user 'John' to the database
User.new(name: 'John').save
```

You can **execute arbitrary SQL** on the database you are currently connected to by using the `.adapter.execute` method.
```ruby
# truncate the users database in the default database
DataMapper.repository(:default).adapter.execute('TRUNCATE users;')
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTc1Mjg2ODMwXX0=
-->